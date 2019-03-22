import os

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
        return length*width

    @staticmethod
    def get_mega_bytes_per_pixel(pixels_in_image, image_size):
        return float(image_size/pixels_in_image)

    def downscale_images(self):
        for file_name in self.__list_of_files_names:
            file_location = self.__directory_of_images_path + file_name
            image = Image.open(file_location)
            file_size = os.path.getsize(file_location)
            file_size_in_megabytes = float(file_size/1000000)

            if file_size_in_megabytes > self.__max_image_file_size_in_mega_bytes:

                image_length, image_width = image.size
                length_width_ratio = image_width / image_length

                product_of_image_dimensions = self.get_product_of_image_dimensions(image_length, image_width)
                mega_bytes_per_pixel = self.get_mega_bytes_per_pixel(product_of_image_dimensions,
                                                                     file_size_in_megabytes)

                mega_bytes_over_limit = file_size_in_megabytes - self.__max_image_file_size_in_mega_bytes

                number_of_pixels_in_reduced_image = (mega_bytes_over_limit / file_size_in_megabytes) * self.__max_image_file_size_in_mega_bytes

                print(str(product_of_image_dimensions))
                print(number_of_pixels_in_reduced_image)
                '''
                print(number_of_pexels_to_reduce_by)
                print(str(product_of_image_dimensions) + ' : ' + str(file_size_in_megabytes) + ' : ' + str(length_width_ratio)+" : "+str(mega_bytes_over_limit))
                # reduce proportionally the number of pixels to a file size below the limit

                # ration is .625   (.625 * 1438977) * mega_bytes_per_pixel
                print((.625 * 1438977) * product_of_image_dimensions)
                '''