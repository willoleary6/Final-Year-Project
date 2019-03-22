import copy
import subprocess
import time

import gi
import cv2
import numpy as np
import os
from os import walk
import re
import tensorflow as tf
from Workspace.ObjectDetector.detector.Detector import Detector
from Workspace.ObjectDetector.config import Config
import datetime

# Here are the imports from the object detection module.
# in the interest of cleanliness and sanity ive updated the paths
# of the interpreter the IDE uses so we can call the object detection api from outside the
# the models directory, using models.research.object_detection will also not work....
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

from PyQt5 import QtGui

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ReaderWindowModel:
    def __init__(self):
        self.__detection_graph = tf.Graph()
        self.__stop_reading = False

    def stop_reader_now(self):
        self.__stop_reading = True

    @staticmethod
    def open_file_in_explorer(file_path):
        subprocess.check_call(['nautilus', '--', file_path])

    @staticmethod
    def check_connection_with_live_stream(signal, address_of_stream):
        successful_test = False
        cap = cv2.VideoCapture(address_of_stream)
        for i in range(5):
            # Read frame from camera
            ret, image_np = cap.read()
            if image_np is not None:
                successful_test = True

        if successful_test:
            signal.emit(
                (
                    "Connection Established",
                    "background-color: green; color: white",
                    True,
                )
            )
        else:
            signal.emit(
                (
                    "Connection Failed",
                    "background-color: red; color: white",
                    False,
                )
            )

    @staticmethod
    def check_if_file_path_is_valid(field, is_directory, desired_extension='/'):
        if is_directory and field.text().endswith(desired_extension):
            return os.path.isdir(field.text())
        elif not is_directory and field.text().endswith(desired_extension):
            return os.path.isfile(field.text())

    @staticmethod
    def get_file_path_through_nautilus(signal, is_directory, field_to_fill_in):
        window = Gtk.Window()
        if is_directory:
            dialog = Gtk.FileChooserDialog("Please choose a folder", window,
                                           Gtk.FileChooserAction.SELECT_FOLDER,
                                           (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                            "Select", Gtk.ResponseType.OK))

            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                signal.emit(
                    (
                        field_to_fill_in,
                        dialog.get_filename()
                    )
                )
            elif response == Gtk.ResponseType.CANCEL:
                pass

            dialog.destroy()
        else:
            dialog = Gtk.FileChooserDialog("Please choose a file", window,
                                           Gtk.FileChooserAction.OPEN,
                                           (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                signal.emit(
                    (
                        field_to_fill_in,
                        dialog.get_filename()
                    )
                )
            elif response == Gtk.ResponseType.CANCEL:
                pass

            dialog.destroy()

    def tensorflow_import_object_detections(self, inference_graph_path):
        with self.__detection_graph.as_default():
            object_detection_graph_definition = tf.GraphDef()
            with tf.gfile.GFile(inference_graph_path, 'rb') as file_id:
                serialized_graph = file_id.read()
                object_detection_graph_definition.ParseFromString(serialized_graph)
                tf.import_graph_def(object_detection_graph_definition, name='')

    def file_reader(self, update_video_player_signal, videos_directory_path, object_labels_path):

        # get all the video files
        files_in_directory = []
        for (directory_path, directory_names, file_names) in walk(videos_directory_path):
            files_in_directory.extend(file_names)
            break

        video_paths = []
        valid_file_extension = Config.VALID_VIDEO_FORMATS
        # filter out the non image related files and build a list of file paths to each of the images
        for i in files_in_directory:
            for j in valid_file_extension:
                if i.endswith(j):
                    video_paths.append(os.path.join(videos_directory_path, i))
                    break

        category_index = label_map_util.create_category_index_from_labelmap(object_labels_path, use_display_name=True)
        frame_number = 0
        # Detection
        detector_object = Detector()
        with self.__detection_graph.as_default():
            with tf.Session(graph=self.__detection_graph) as sess:
                break_out = False
                for video in video_paths:
                    cap = cv2.VideoCapture(video)
                    end_of_video = False
                    while end_of_video is False:
                        frame_number = frame_number + 1
                        # Read frame from camera
                        ret, image_np = cap.read()
                        if image_np is None:
                            end_of_video = True
                        else:
                            if frame_number % Config.FRAME_DELIMITER_FOR_TENSORFLOW == 0:

                                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                                image_np_expanded = np.expand_dims(image_np, axis=0)
                                # Extract image tensor
                                image_tensor = self.__detection_graph.get_tensor_by_name('image_tensor:0')
                                # Extract detection boxes
                                boxes = self.__detection_graph.get_tensor_by_name('detection_boxes:0')
                                # Extract detection scores
                                scores = self.__detection_graph.get_tensor_by_name('detection_scores:0')
                                # Extract detection classes
                                classes = self.__detection_graph.get_tensor_by_name('detection_classes:0')

                                # Extract number of detections
                                num_detections = self.__detection_graph.get_tensor_by_name(
                                    'num_detections:0')
                                # Actual detection.
                                (boxes, scores, classes, num_detections) = sess.run(
                                    [boxes, scores, classes, num_detections],
                                    feed_dict={image_tensor: image_np_expanded})
                                # Visualization of the results of a detection.

                                vis_util.visualize_boxes_and_labels_on_image_array(
                                    image_np,
                                    np.squeeze(boxes),
                                    np.squeeze(classes).astype(np.int32),
                                    np.squeeze(scores),
                                    category_index,
                                    use_normalized_coordinates=True,
                                    line_thickness=8)

                                objects = []
                                threshold = 0.5

                                for index, value in enumerate(classes[0]):
                                    object_dict = {}
                                    if scores[0, index] > threshold:
                                        object_dict[(category_index.get(value)).get('name').encode('utf8')] = \
                                            scores[0, index]
                                        object_dict = re.findall('\'([^\']*)\'', str(object_dict))[0]
                                        objects.append(object_dict)
                                if len(objects) > 0:
                                    timestamp = round(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000, 2)
                                    detector_object.new_detection(objects, video, timestamp, len(objects))
                                # formatting the rgb
                                image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
                                # converting image_np to a q image
                                new_q_image = QtGui.QImage(
                                    image_np,
                                    image_np.shape[1],
                                    image_np.shape[0],
                                    QtGui.QImage.Format_RGB888
                                )
                                # converting the QImage to pix for the label
                                pix = QtGui.QPixmap.fromImage(new_q_image)
                                update_video_player_signal.emit(pix)

                                if self.__stop_reading:
                                    break_out = True
                                    break
                    if break_out is True:
                        break
        detector_object.flush_remaining_detections()
        self.__stop_reading = False

    @staticmethod
    def derive_file_path_for_video(parent_directory, date_time, extension):
        file_path = parent_directory + '/'
        formatted_date_time = str(date_time)
        # replace spaces with underscores
        formatted_date_time = formatted_date_time.replace(" ", "_")
        # replace full stops with underscores
        formatted_date_time = formatted_date_time.replace(".", "_")
        # replace colons with dashes
        formatted_date_time = formatted_date_time.replace(":", "-")

        file_path = file_path + formatted_date_time + extension

        return file_path

    def live_stream_reader(self, update_video_player_signal, livestream_address, videos_directory_path,
                           object_labels_path):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        category_index = label_map_util.create_category_index_from_labelmap(object_labels_path, use_display_name=True)
        frame_number = 0
        # Detection
        detector_object = Detector()
        start_time = datetime.datetime.now()

        # time.sleep(10)
        # current_time = datetime.datetime.now()
        # time_subtraction = current_time - start_time
        # print(time_subtraction.seconds)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writing_to_new_video = True
        file_path_for_recording = ''
        with self.__detection_graph.as_default():
            with tf.Session(graph=self.__detection_graph) as sess:
                cap = cv2.VideoCapture(livestream_address)
                out = cv2.VideoWriter()
                while not self.__stop_reading:

                    frame_number = frame_number + 1
                    # Read frame from camera
                    ret, image_np = cap.read()
                    original_frame = copy.deepcopy(image_np)
                    if writing_to_new_video:
                        file_path_for_recording = self.derive_file_path_for_video(videos_directory_path, start_time,
                                                                                  Config.RECORDINGS_FORMAT)
                        out = cv2.VideoWriter(file_path_for_recording, fourcc, 20.0,
                                              (image_np.shape[1], image_np.shape[0]))
                        writing_to_new_video = False

                    if frame_number % Config.FRAME_DELIMITER_FOR_TENSORFLOW == 0:
                        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                        image_np_expanded = np.expand_dims(image_np, axis=0)
                        # Extract image tensor
                        image_tensor = self.__detection_graph.get_tensor_by_name('image_tensor:0')
                        # Extract detection boxes
                        boxes = self.__detection_graph.get_tensor_by_name('detection_boxes:0')
                        # Extract detection scores
                        scores = self.__detection_graph.get_tensor_by_name('detection_scores:0')
                        # Extract detection classes
                        classes = self.__detection_graph.get_tensor_by_name('detection_classes:0')

                        # Extract number of detectionsd
                        num_detections = self.__detection_graph.get_tensor_by_name(
                            'num_detections:0')
                        # Actual detection.
                        (boxes, scores, classes, num_detections) = sess.run(
                            [boxes, scores, classes, num_detections],
                            feed_dict={image_tensor: image_np_expanded})
                        # Visualization of the results of a detection.
                        vis_util.visualize_boxes_and_labels_on_image_array(
                            image_np,
                            np.squeeze(boxes),
                            np.squeeze(classes).astype(np.int32),
                            np.squeeze(scores),
                            category_index,
                            use_normalized_coordinates=True,
                            line_thickness=8)

                        objects = []
                        threshold = 0.5
                        current_time = datetime.datetime.now()
                        time_subtraction = current_time - start_time

                        for index, value in enumerate(classes[0]):
                            object_dict = {}
                            if scores[0, index] > threshold:
                                object_dict[(category_index.get(value)).get('name').encode('utf8')] = \
                                    scores[0, index]
                                object_dict = re.findall('\'([^\']*)\'', str(object_dict))[0]
                                objects.append(object_dict)
                        if len(objects) > 0:
                            # videos_directory_path
                            detector_object.new_detection(
                                objects,
                                file_path_for_recording,
                                time_subtraction.seconds,
                                len(objects)
                            )
                        # formatting the rgb
                        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
                        # converting image_np to a q image
                        new_q_image = QtGui.QImage(
                            image_np,
                            image_np.shape[1],
                            image_np.shape[0],
                            QtGui.QImage.Format_RGB888
                        )
                        # converting the QImage to pix for the label
                        pix = QtGui.QPixmap.fromImage(new_q_image)
                        update_video_player_signal.emit(pix)

                    current_time = datetime.datetime.now()
                    time_subtraction = current_time - start_time
                    out.write(original_frame)
                    if time_subtraction.seconds >= Config.SECONDS_PER_RECORDING:
                        writing_to_new_video = True
                        start_time = current_time
                        detector_object.flush_remaining_detections()
                        out.release()

        detector_object.flush_remaining_detections()
        out.release()


