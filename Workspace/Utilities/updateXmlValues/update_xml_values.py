from PIL import Image
from argparse import ArgumentParser
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
import math
import re

# parser = ArgumentParser()
# parser.add_argument("-p",
#                    "-path_to_videos",
#                    dest="path_to_videos",
#                    help="File path to the directory containing the images",
#                    default=False
#                    )
#
# parser.add_argument("-m",
#                    "-multiply_values",
#                    dest="multiply_values",
#                    help="The largest dimension the image can have",
#                    default=False
#                    )

# args = parser.parse_args()
# if args.path_to_videos and args.max_dimension:

def adjust_size(size, multiplicity):
    for dimension in ['height', 'width']:
        size[0].getElementsByTagName(dimension)[0].childNodes[0].data = \
            int(size[0].getElementsByTagName(dimension)[0].childNodes[0].data) * int(multiplicity)

    return size


def get_title_from_element(element):
    element_string = str(element)
    title = re.findall('\'([^\']*)\'', element_string)
    return title[0]


# path = args.path_to_videos
path = "C:\SourceCode\Final-Year-Project\Images\prototype_images\coins\\"

# max_dimension = 600
# every file_name in the directory
multiplying_by = 2
for file_name in os.listdir(path):
    extension = file_name.split('.')[-1]
    # only image files
    if extension == 'xml':
        # the location we want to retrieve and save the image too
        file_Location = path + file_name
        tree = ET.parse(file_Location)
        root = tree.getroot()
        data = ET.Element('data')
        for i in root:
            title = get_title_from_element(i)
            if title == 'size':
                i[0].text = str(int(i[0].text) * multiplying_by)
                i[1].text = str(int(i[1].text) * multiplying_by)

            elif title == 'object':
                bndbox = i[4]
                for j in bndbox:
                    j.text = str(int(j.text) * multiplying_by)

        str_data = re.findall('\'([^\']*)\'', str(ET.tostring(root)))
        data = (ET.tostring(root))
        myfile = open(file_Location, "w")
        myfile.write(str_data[0])

    # else:
#   print("Missing required arguments, check --help")
