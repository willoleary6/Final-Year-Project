import os
import xml.etree.ElementTree as ET
import math
import re

from PIL import Image


class ScaleImagesAndCorrespondingXML:
    def __init__(self, directory_of_images_path, max_image_file_size_in_mega_bytes):
        self.__directory_of_images_path = directory_of_images_path
        self.__max_image_file_size_in_mega_bytes = max_image_file_size_in_mega_bytes
        self.__list_of_files_names = []

        for file_name in os.listdir(self.__directory_of_images_path):
            extension = file_name.split('.')[-1]
            # only image files
            if extension != 'xml':
                self.__list_of_files_names.append(file_name)

    @staticmethod
    def get_product_of_image_dimensions(length, width):
        return length * width

    @staticmethod
    def get_mega_bytes_per_pixel(pixels_in_image, image_size):
        return float(image_size / pixels_in_image)

    def downscale_images(self):
        for file_name in self.__list_of_files_names:
            file_location = self.__directory_of_images_path + file_name
            image = Image.open(file_location)
            file_size = os.path.getsize(file_location)
            # convert bytes to megabytes
            file_size_in_megabytes = float(file_size / 1000000)
            if file_size_in_megabytes > self.__max_image_file_size_in_mega_bytes:
                image_length, image_width = image.size
                length_width_ratio = image_width / image_length

                product_of_image_dimensions = self.get_product_of_image_dimensions(image_length, image_width)
                bytes_per_pixel = self.get_mega_bytes_per_pixel(product_of_image_dimensions,
                                                                file_size)
                bytes_limit = self.__max_image_file_size_in_mega_bytes * 1000000

                bytes_to_reduce_by = file_size - bytes_limit
                # determine how much should the length be reduced by
                length_to_reduce_by = (((bytes_to_reduce_by / bytes_per_pixel) / length_width_ratio) / image_length)
                # get percentage of rump length and use that to scale width down to same proportion
                percentage_of_length_remaining = length_to_reduce_by / image_length
                new_length = math.ceil(image_length - length_to_reduce_by)
                new_width = math.ceil(image_width * (1 - percentage_of_length_remaining))
                # resizing
                image = image.resize((new_length, new_width))
                image.save(file_location)
                filename_without_extension = file_name.split('.')[0]
                path_to_potential_xml_files = self.__directory_of_images_path + filename_without_extension + '.xml'
                # check if file has corresponding xml file
                exists = os.path.isfile(path_to_potential_xml_files)
                if exists:
                    self.adjust_xml_file_values(image_length, image_width, new_length, new_width,
                                                path_to_potential_xml_files)

    def adjust_xml_file_values(self, old_length, old_width, new_length, new_width, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        # what we need to multiply all the lengths and weights by to bring the xml values in line with the
        # rescaled image.
        height_multiplicity = new_length / old_length
        width_multiplicity = new_width / old_width
        root.find('size')[self.get_index(root.find('size'), 'width')].text = str(new_length)
        root.find('size')[self.get_index(root.find('size'), 'height')].text = str(new_width)
        # running through each labeled object
        for member in root.findall('object'):
            last_member_index = len(member) - 1
            # get current values
            x_min_value = int(member[last_member_index][self.get_index(member[last_member_index], 'xmin')].text)
            y_min_value = int(member[last_member_index][self.get_index(member[last_member_index], 'ymin')].text)
            x_max_value = int(member[last_member_index][self.get_index(member[last_member_index], 'xmax')].text)
            y_max_value = int(member[last_member_index][self.get_index(member[last_member_index], 'ymax')].text)

            member[last_member_index][
                self.get_index(member[last_member_index], 'xmin')].text = str(round(x_min_value * width_multiplicity))
            member[last_member_index][
                self.get_index(member[last_member_index], 'ymin')].text = str(round(y_min_value * height_multiplicity))
            member[last_member_index][
                self.get_index(member[last_member_index], 'xmax')].text = str(round(x_max_value * width_multiplicity))
            member[last_member_index][
                self.get_index(member[last_member_index], 'ymax')].text = str(round(y_max_value * height_multiplicity))

        str_data = re.findall('\'([^\']*)\'', str(ET.tostring(root)))
        my_file = open(file_path, "w")
        my_file.write(str_data[0])

    @staticmethod
    def get_title_from_element(element):
        element_string = str(element)
        title = re.findall('\'([^\']*)\'', element_string)
        return title[0]

    @staticmethod
    def get_index(root, desired_attribute):
        for i, x in enumerate(root):
            if x.tag == desired_attribute:
                return i
