import copy
import shutil
import subprocess
import sys
import time

import gi
import cv2
import numpy as np
import os
from os import walk
import re
import tensorflow as tf
from PIL import Image

from Workspace.ObjectDetector.detector.Detector import Detector
from Workspace.ObjectDetector.config import Config
from Workspace.labelImg.labelImg import MainWindow
from Workspace.ObjectDetector.Utilities.ScaleImagesAndCorrespondingXML import ScaleImagesAndCorrespondingXML
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
            if extension == 'png':
                self.convert_png_to_jpg(file, file_name)
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
            tree = ET.parse(file_path.split('.')[0] + '.xml')
            root = tree.getroot()
            root.find('filename').text = str(file_name.split('.')[0] + '.jpg')
            root.find('path').text = str(file_path.split('.')[0] + '.jpg')
            str_data = re.findall('\'([^\']*)\'', str(ET.tostring(root)))
            my_file = open(file_path.split('.')[0] + '.xml', "w")
            my_file.write(str_data[0])

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
            if extension == '.jpg' or extension == '.jpeg':
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
            if extension == 'jpg' or extension == 'jpeg':
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
            if extension == 'jpg' or extension == 'jpeg':
                if not os.path.isfile(data_set_directory+file.split('.')[0]+'.xml'):
                    check_result['check_outcome'] = False
                    check_result['description'] = 'images present without xml file'
                    check_result['invalid_files'].append(data_set_directory+file)

        return check_result
    def open_label_img_with_invalid_files(self, invalid_files, recheck_signal):
        argv = []
        self.__label_img_instance = MainWindow(
            recheck_signal,
            argv[1] if len(argv) >= 2 else None,
            argv[2] if len(argv) >= 3 else os.path.join(
                os.path.dirname(sys.argv[0]),'data', 'predefined_classes.txt'),
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
                tree = ET.parse(data_set_directory+file)
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
                                check_result['invalid_files'].append(data_set_directory + file.split('.')[0]+'.jpg')
                    except Exception as e:
                        check_result['check_outcome'] = False
                        check_result['description'] = "Invalid xml files found"
                        check_result['invalid_files'].append(data_set_directory + file.split('.')[0]+'.jpg')


        return check_result

    @staticmethod
    def get_index(root, desired_attribute):
        for i, x in enumerate(root):
            if x.tag == desired_attribute:
                return i