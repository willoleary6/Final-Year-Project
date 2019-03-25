import os
import xml.etree.ElementTree as ET
import math
import re

from PIL import Image

path = '/home/will/Documents/Stanford40_JPEGImages'

list_of_files = os.listdir(path)
for file in list_of_files:
    extension = file.split('.')[-1]
    if extension == 'xml':
        tree = ET.parse(path + '/' + file)
        root = tree.getroot()
        file_name = root.find('filename').text
        file_name_split = file_name.split('_')
        object_name = ''
        for i,x in enumerate(file_name_split):
            if i < len(file_name_split)-1:
                object_name += x + '_'
        object_name = object_name[:-1]
        for member in root.findall('object'):
            member.find('name').text = object_name

        str_data = re.findall('\'([^\']*)\'', str(ET.tostring(root)))
        my_file = open(path + '/' + file, "w")
        my_file.write(str_data[0])

