import _thread
import copy
import glob
import random
import shutil
import signal
import subprocess
import sys
import time

import gi
import cv2
import numpy as np
import os
from os import walk
import re
from subprocess import Popen, PIPE
import pandas as pd
import tensorflow as tf
from PIL import Image
import webbrowser
from Workspace.ObjectDetector.detector.Detector import Detector
from Workspace.ObjectDetector.config import Config
from Workspace.labelImg.labelImg import MainWindow
from Workspace.ObjectDetector.Utilities.ScaleImagesAndCorrespondingXML import ScaleImagesAndCorrespondingXML
from Workspace.ObjectDetector.Utilities.GenerateTfRecord import GenerateTfRecord

import datetime

# Here are the imports from the object detection module.
# in the interest of cleanliness and sanity ive updated the paths
# of the interpreter the IDE uses so we can call the object detection api from outside the
# the models directory, using models.research.object_detection will also not work....
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import xml.etree.ElementTree as ET
from PyQt5 import QtGui
from subprocess import call

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TrainerWindowModel:
    def __init__(self):
        self.__label_img_instance = None
        self.process = None

    @staticmethod
    def get_file_path_through_nautilus(qt_signal, is_directory, field_to_fill_in):
        window = Gtk.Window()
        if is_directory:
            dialog = Gtk.FileChooserDialog("Please choose a folder", window,
                                           Gtk.FileChooserAction.SELECT_FOLDER,
                                           (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                            "Select", Gtk.ResponseType.OK))

            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                qt_signal.emit(
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
                qt_signal.emit(
                    (
                        field_to_fill_in,
                        dialog.get_filename()
                    )
                )
            elif response == Gtk.ResponseType.CANCEL:
                pass

            dialog.destroy()

    @staticmethod
    def check_if_file_path_is_valid(field, is_directory, desired_extension='/'):
        if is_directory and field.text().endswith(desired_extension):
            return os.path.isdir(field.text())
        elif not is_directory and field.text().endswith(desired_extension):
            return os.path.isfile(field.text())

    def move_image_data_set_to_training_directory(self, training_directory_file_path,
                                                  image_data_set_directory_file_path):
        if not training_directory_file_path.endswith('/'):
            training_directory_file_path += '/'
        training_image_data_sets_directory_path = training_directory_file_path + 'image_data_sets/'
        if not os.path.isdir(training_image_data_sets_directory_path):
            os.makedirs(training_image_data_sets_directory_path)

        image_data_set_directory_split_by_forward_slash = image_data_set_directory_file_path.split('/')
        directory_name_of_image_data_set = \
            image_data_set_directory_split_by_forward_slash[
                len(
                    image_data_set_directory_split_by_forward_slash) - 1
                ]
        training_image_data_sets_directory_path = \
            training_image_data_sets_directory_path + directory_name_of_image_data_set + '/'
        if os.path.isdir(training_image_data_sets_directory_path):
            shutil.rmtree(training_image_data_sets_directory_path)

        self.cp_dir(image_data_set_directory_file_path, training_image_data_sets_directory_path)

        return training_image_data_sets_directory_path

    @staticmethod
    def cp_dir(source, target):
        call(['cp', '-a', source, target])  # Linux

    def image_data_set_file_format_test(self, data_set_directory):
        check_result = {
            'check_outcome': True,
            'description': 'Pass',
            'invalid_files': []
        }

        list_of_files = os.listdir(data_set_directory)
        if len(list_of_files) < 1:
            check_result['check_outcome'] = False
            check_result['description'] = 'Directory is empty'
            return check_result

        for file in list_of_files:
            extension = file.split('.')[-1]
            if not self.is_valid_extension(extension):
                check_result['check_outcome'] = False
                check_result['description'] = 'Invalid files present'
                check_result['invalid_files'].append(data_set_directory + file)

        return check_result

    @staticmethod
    def is_valid_extension(extension):
        for valid_extension in Config.VALID_IMAGE_EXTENSIONS:
            if extension == valid_extension:
                return True
        return False

    def remove_invalid_files(self, invalid_files):
        for file in invalid_files:
            extension = file.split('.')[-1]
            file_name = file.split('/')[len(file.split('/')) - 1]
            if extension == 'png' or extension == 'jpeg':
                self.convert_png_to_jpg(file, file_name)

            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)

    @staticmethod
    def convert_png_to_jpg(file_path, file_name):
        img = Image.open(file_path).convert('RGB')
        x = np.array(img)
        r, g, b = np.rollaxis(x, axis=-1)
        x = np.dstack([r, g, b])
        img = Image.fromarray(x, 'RGB')
        img.save(file_path.split('.')[0] + '.jpg')
        if os.path.isfile(file_path.split('.')[0] + '.xml'):
            try:
                tree = ET.parse(file_path.split('.')[0] + '.xml')
                root = tree.getroot()
                root.find('filename').text = str(file_name.split('.')[0] + '.jpg')
                root.find('path').text = str(file_path.split('.')[0] + '.jpg')
                str_data = re.findall('\'([^\']*)\'', str(ET.tostring(root)))
                my_file = open(file_path.split('.')[0] + '.xml', "w")
                my_file.write(str_data[0])
            except Exception as e:
                pass

    @staticmethod
    def open_nautilus(file_path):
        subprocess.check_call(['nautilus', '--', file_path])

    @staticmethod
    def image_numbers_test(data_set_directory):
        check_result = {
            'check_outcome': True,
            'description': 'Pass',
            'invalid_files': []
        }

        list_of_files = os.listdir(data_set_directory)
        count = 0
        for file in list_of_files:
            extension = file.split('.')[-1]
            if extension == '.jpg':
                count += 1

        if count < Config.MINIMUM_NUMBER_OF_IMAGES:
            check_result['check_outcome'] = False
            check_result['description'] = 'Not enough images in dataset'

        return check_result

    def image_size_test(self, data_set_directory):
        check_result = {
            'check_outcome': True,
            'description': 'Pass',
            'invalid_files': []
        }

        list_of_files = os.listdir(data_set_directory)
        for file in list_of_files:
            extension = file.split('.')[-1]
            if extension == 'jpg':
                file_size = (os.path.getsize(data_set_directory + file)) / 1000000
                if file_size >= Config.MAXIMUM_IMAGE_SIZE_IN_MEGABYTES + .02:
                    check_result['check_outcome'] = False
                    check_result['description'] = 'Images too large'
        return check_result

    def downscale_images(self, directory_of_data_set):
        scaler = ScaleImagesAndCorrespondingXML(directory_of_data_set, Config.MAXIMUM_IMAGE_SIZE_IN_MEGABYTES)
        scaler.downscale_images()

    @staticmethod
    def corresponding_xml_file_test(data_set_directory):
        check_result = {
            'check_outcome': True,
            'description': 'Pass',
            'invalid_files': []
        }

        list_of_files = os.listdir(data_set_directory)
        for file in list_of_files:
            extension = file.split('.')[-1]
            if extension == 'jpg':
                if not os.path.isfile(data_set_directory + file.split('.')[0] + '.xml'):
                    check_result['check_outcome'] = False
                    check_result['description'] = 'images present without xml file'
                    check_result['invalid_files'].append(data_set_directory + file)

        return check_result

    def open_label_img_with_invalid_files(self, invalid_files, recheck_signal):
        argv = []
        self.__label_img_instance = MainWindow(
            recheck_signal,
            argv[1] if len(argv) >= 2 else None,
            argv[2] if len(argv) >= 3 else os.path.join(
                os.path.dirname(sys.argv[0]), 'data', 'predefined_classes.txt'),
            argv[3] if len(argv) >= 4 else None)
        self.__label_img_instance.show()
        self.__label_img_instance.loadFile(invalid_files[0])
        self.__label_img_instance.import_array_of_file_paths(invalid_files)

    def validity_xml_file_test(self, data_set_directory):
        check_result = {
            'check_outcome': True,
            'description': 'Pass',
            'invalid_files': []
        }

        list_of_files = os.listdir(data_set_directory)
        for file in list_of_files:
            extension = file.split('.')[-1]
            if extension == 'xml':
                tree = ET.parse(data_set_directory + file)
                root = tree.getroot()
                for member in root.findall('object'):
                    last_member_index = len(member) - 1
                    try:
                        value = (root.find('filename').text,
                                 int(root.find('size')[self.get_index(root.find('size'), 'width')].text),
                                 int(root.find('size')[self.get_index(root.find('size'), 'height')].text),
                                 member[0].text,
                                 int(member[last_member_index][self.get_index(member[last_member_index], 'xmin')].text),
                                 int(member[last_member_index][self.get_index(member[last_member_index], 'ymin')].text),
                                 int(member[last_member_index][self.get_index(member[last_member_index], 'xmax')].text),
                                 int(member[last_member_index][self.get_index(member[last_member_index], 'ymax')].text)
                                 )
                        for i in value:
                            if i == '' or i == None:
                                check_result['check_outcome'] = False
                                check_result['description'] = "Invalid xml files found"
                                check_result['invalid_files'].append(data_set_directory + file.split('.')[0] + '.jpg')
                    except Exception as e:
                        check_result['check_outcome'] = False
                        check_result['description'] = "Invalid xml files found"
                        check_result['invalid_files'].append(data_set_directory + file.split('.')[0] + '.jpg')

        return check_result

    @staticmethod
    def get_index(root, desired_attribute):
        for i, x in enumerate(root):
            if x.tag == desired_attribute:
                return i

    def extract_labels_from_xml_files(self, data_set_directory):
        list_of_files = os.listdir(data_set_directory)
        list_of_objects = []
        for file in list_of_files:
            extension = file.split('.')[-1]
            if extension == 'xml':
                tree = ET.parse(data_set_directory + file)
                root = tree.getroot()
                for member in root.findall('object'):
                    object_name = member.find('name').text
                    if not self.check_for_duplicates(list_of_objects, object_name):
                        list_of_objects.append(object_name)
        return list_of_objects

    @staticmethod
    def check_for_duplicates(current_array, object_to_be_checked):
        for i in current_array:
            if i == object_to_be_checked:
                return True
        return False

    @staticmethod
    def split_data_set(data_set_directory, split_percentage):
        test_set_path = data_set_directory + 'test/'
        train_set_path = data_set_directory + 'train/'
        if os.path.isdir(test_set_path):
            list_of_files = os.listdir(test_set_path)
            for file in list_of_files:
                shutil.move(test_set_path + file, data_set_directory)
            shutil.rmtree(test_set_path)
        if os.path.isdir(train_set_path):
            list_of_files = os.listdir(train_set_path)
            for file in list_of_files:
                shutil.move(train_set_path + file, data_set_directory)
            shutil.rmtree(train_set_path)

        os.mkdir(test_set_path)
        os.mkdir(train_set_path)
        list_of_files = os.listdir(data_set_directory)
        for file in list_of_files:
            extension = file.split('.')[-1]
            if extension == 'jpg':
                filename = data_set_directory + file.split('.')[0]
                if random.randint(0, 100) <= split_percentage:
                    # test
                    shutil.move(filename + '.jpg', test_set_path)
                    shutil.move(filename + '.xml', test_set_path)
                else:
                    # train
                    shutil.move(filename + '.jpg', train_set_path)
                    shutil.move(filename + '.xml', train_set_path)

    @staticmethod
    def check_if_image_data_set_has_been_split(data_set_directory):
        list_of_files = os.listdir(data_set_directory)
        for file in list_of_files:
            if file == 'test' or file == 'train':
                pass
            else:
                return False
        return True

    def generate_tf_records(self, trainer_directory, data_set_directory, list_of_labels):

        data_directory = trainer_directory + '/data'
        if os.path.isdir(data_directory):
            shutil.rmtree(data_directory)
        os.mkdir(data_directory)
        test_set_path = data_set_directory + 'test/'
        train_set_path = data_set_directory + 'train/'

        test_xml = self.xml_to_csv(test_set_path)
        train_xml = self.xml_to_csv(train_set_path)

        test_xml_path = data_directory + '/test' + '_labels.csv'
        train_xml_path = data_directory + '/train' + '_labels.csv'

        test_record_path = data_directory + '/test.record'
        train_record_path = data_directory + '/train.record'

        test_xml.to_csv(data_directory + '/test' + '_labels.csv', index=None)
        train_xml.to_csv(data_directory + '/train' + '_labels.csv', index=None)

        test_record = GenerateTfRecord(test_xml_path, test_record_path, test_set_path, list_of_labels)
        test_record_success = test_record.write_record()
        train_record = GenerateTfRecord(train_xml_path, train_record_path, train_set_path, list_of_labels)
        train_record_success = train_record.write_record()

        return test_record_path, train_record_path, test_record_success, train_record_success

    def xml_to_csv(self, path):
        xml_list = []
        for xml_file in glob.glob(path + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                last_member_index = len(member) - 1
                value = (root.find('filename').text,
                         int(root.find('size')[self.get_index(root.find('size'), 'width')].text),
                         int(root.find('size')[self.get_index(root.find('size'), 'height')].text),
                         member[0].text,
                         int(member[last_member_index][self.get_index(member[last_member_index], 'xmin')].text),
                         int(member[last_member_index][self.get_index(member[last_member_index], 'ymin')].text),
                         int(member[last_member_index][self.get_index(member[last_member_index], 'xmax')].text),
                         int(member[last_member_index][self.get_index(member[last_member_index], 'ymax')].text)
                         )
                xml_list.append(value)
        column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = pd.DataFrame(xml_list, columns=column_name)
        return xml_df

    @staticmethod
    def get_config_path_from_tensorflow(model_directory):
        model_name_width_date = (model_directory.split('/'))[len(model_directory.split('/')) - 1]
        model_name = ''
        for segment in model_name_width_date.split('_'):
            try:
                int(segment)
            except Exception as e:
                model_name = model_name + segment + '_'
        model_name = model_name[:-1]
        list_of_files = os.listdir(Config.TENSOR_FLOW_OBJECT_DETECTION_DIRECTORY + "/samples/configs")
        for file in list_of_files:
            if file == model_name + '.config':
                return Config.TENSOR_FLOW_OBJECT_DETECTION_DIRECTORY + '/samples/configs/' + file
        return ''

    def commit_model_training_directory(
            self,
            model_directory,
            model_config_path,
            trainer_directory,
            list_of_xml_labels,
            test_record_path,
            train_record_path):
        training_directory_path = trainer_directory + '/training'
        if not os.path.isdir(training_directory_path):
            os.mkdir(training_directory_path)

        label_file_path = training_directory_path + '/object_detection.pbtxt'
        if os.path.isfile(label_file_path):
            os.remove(label_file_path)

        file_writer = open(label_file_path, "w+")
        count = 1
        for label in list_of_xml_labels:
            file_writer.write(
                'item {\n'
                '   id: ' + str(count) + '\n'
                                         '   name: \'' + label + '\'' + '\n'
                                                                        '} \n \n'
            )
            count += 1
        file_writer.close()

        parser = open(model_config_path, "r")
        config_file = parser.read()
        config_file = config_file.replace('PATH_TO_BE_CONFIGURED/model.ckpt', model_directory + '/model.ckpt')
        config_file = config_file.replace('PATH_TO_BE_CONFIGURED/mscoco_label_map.pbtxt', label_file_path)
        config_file = config_file.replace('PATH_TO_BE_CONFIGURED/mscoco_train.record-?????-of-00100', train_record_path)
        config_file = config_file.replace('PATH_TO_BE_CONFIGURED/mscoco_val.record-?????-of-00010', test_record_path)

        config_file_directory = training_directory_path + '/pipeline.config'
        if os.path.isfile(config_file_directory):
            os.remove(config_file_directory)

        file_writer = open(config_file_directory, "w+")
        file_writer.write(config_file)
        file_writer.close()
        return training_directory_path

    @staticmethod
    def commence_training(training_directory):
        print(training_directory)
        command = "python3 " + Config.TENSOR_FLOW_OBJECT_DETECTION_DIRECTORY + "legacy/train.py " \
                  "--logtostderr --train_dir=" + training_directory + " --pipeline_config_path=" + training_directory \
                  + "/pipeline.config "
        try:
            os.system("gnome-terminal -e 'bash -c \"" + str(Config.TENSOR_FLOW_PYTHON_PATH) + "\" '")
            os.system("gnome-terminal -e 'bash -c \"" + str(command) + "\" '")
        except Exception as e:
            print(e)

    @staticmethod
    def open_tensor_board(training_directory):
        command = "tensorboard --logdir=" + training_directory + " --host localhost --port 8088"
        os.system("gnome-terminal -e 'bash -c \"" + str(command) + "\"'")
        url = 'http://localhost:8088'

        time.sleep(3)
        webbrowser.open_new(url)

    @staticmethod
    def export_inference_graph(model_directory, file_path_to_checkpoint):
        checkpoint_pre_extension_array = file_path_to_checkpoint.split('.')
        checkpoint_pre_extension = checkpoint_pre_extension_array[0] + '.' + checkpoint_pre_extension_array[1]
        command = "python3 " + Config.TENSOR_FLOW_OBJECT_DETECTION_DIRECTORY \
                  + "/export_inference_graph.py " \
                  "--input_type image_tensor " \
                  "--pipeline_config_path " + model_directory + "/training/pipeline.config " \
                  "--trained_checkpoint_prefix " + checkpoint_pre_extension + " "\
                  "--output_directory " + model_directory + "/graph/"

        print(command)
        try:
            os.system("gnome-terminal -e 'bash -c \"" + str(Config.TENSOR_FLOW_PYTHON_PATH) + "\" '")
            os.system("gnome-terminal -e 'bash -c \"" + str(command) + "\" '")
        except Exception as e:
            print(e)

