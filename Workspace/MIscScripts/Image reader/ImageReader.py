import numpy as np
import hyperspy.api as hs
import matplotlib.pyplot as plt
import cv
import os
from os import walk


class ImageReader:

    def __init__(self, source_directory, destination_directory, file_type):
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.file_type = file_type

    @staticmethod
    def read_em_files(filename):

        img = hs.load(filename)  # Hyperspy function to load dm3 files

        img.plot()
        '''
        The pixel intensity values are stored in the .data extension - as a numpy array. The DM3 data comes in as 
        data type float32, in order to display it in python, or save as a tiff, I round and convert 
        the values to integers. The range of the micro-graphs I was dealing with was from 0-65535 - 2^16 
        (so I converted to uint16). Sometimes the range in intensity can be larger. 
        It is simple to work in images which have gray-scale values from 0-255, but the extra resolution in the 
        intensity dimension could be valuable to you.
        '''
        img.data = np.around(
            img.data)  # Round to integer - straight conversion to uint16 floors the value - would rather round

        img.data = img.data.astype('uint16')  # Change to data type int
        return img.data

    def convert_dm4_files(self):
        files_to_convert = self.get_file_names_from_directory(self.source_directory)
        for i in files_to_convert:
            os.chdir(self.source_directory)
            numpy_data_from_file = self.read_em_files(i)
            new_file_name = self.change_file_name_extension(i)

            os.chdir(self.destination_directory)
            cv2.imwrite(new_file_name, numpy_data_from_file)

    # change file name extension to new extension
    def change_file_name_extension(self, file_name):
        sep = '.'
        # split string into characters before and after '.'
        file_name_without_extension = file_name.split(sep, 1)[0]
        return file_name_without_extension + self.file_type

    # retrieve list of file names from desired directory
    def get_file_names_from_directory(self):
        files_to_convert = []
        for (dir_path, dir_names, file_names) in walk(self.source_directory):
            files_to_convert.extend(file_names)
            break
        return files_to_convert;

    # method to display a desired image
    def show_em_file_contents(self, filename):
        os.chdir(self.source_directory)
        numpy_data_from_file = self.read_em_files(filename)
        plt.gcf().clear()
        plt.imshow(numpy_data_from_file)
        plt.show()
