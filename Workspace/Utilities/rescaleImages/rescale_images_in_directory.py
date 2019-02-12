from PIL import Image
from argparse import ArgumentParser
import os
import math

parser = ArgumentParser()
parser.add_argument("-p",
                    "-path_to_videos",
                    dest="path_to_videos",
                    help="File path to the directory containing the images",
                    default=False
                    )

parser.add_argument("-m",
                    "-max_dimension",
                    dest="max_dimension",
                    help="The largest dimension the image can have",
                    default=False
                    )

args = parser.parse_args()
if args.path_to_images and args.max_dimension:
    path = args.path_to_images
    # path = "C:\SourceCode\Final-Year-Project\Images\prototype_images\coins\\"
    max_dimension = int(args.max_dimension)
    # max_dimension = 600
    # every file_name in the directory
    for file_name in os.listdir(path):
        extension = file_name.split('.')[-1]
        # only image files
        if extension != 'xml':
            # the location we want to retrieve and save the image too
            file_Location = path + file_name
            image = Image.open(file_Location)
            file_size = os.path.getsize(file_Location)
            # print the image name, its size of bytes and the dimensions of the image
            print(file_name + " : " + str(file_size) + " : " + str(image.size))
            image = Image.open(file_Location)
            # retrieve the image dimensions
            image_length, image_width = image.size
            length_width_ratio = image_width / image_length
            # check if the image already falls into our max size
            if image_length > max_dimension or image_width > max_dimension:
                # which ever dimension in the largest will be reduced to the max dimension and the smaller dimension
                # will be proportionally decreased to preserve the aspect ratio
                if image_length > image_width:
                    reduction_amount = image_length - max_dimension
                    # updating value of dimension
                    image_length = image_length - reduction_amount

                    # updating the width proportional to the new length
                    image_width = math.floor(image_width - (reduction_amount * length_width_ratio))
                else:
                    reduction_amount = image_width - max_dimension
                    image_width = image_width - reduction_amount

                    image_length = math.floor(image_length - (reduction_amount / length_width_ratio))
                # resize the image with the new dimensions
                image = image.resize((image_length, image_width))
                # save the rescaled image
                image.save(file_Location)

            file_size = os.path.getsize(file_Location)
            print(file_name + " : " + str(file_size) + " : " + str(image.size))
            print("-----------------------")
else:
    print("Missing required arguments, check --help")
