from PIL import Image
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-p",
                    "-path_to_jpg",
                    dest="path_to_jpg",
                    help="File path to the directory containing the jpg files",
                    default=False
                    )

args = parser.parse_args()
if args.path_to_jpg:
    path = args.path_to_jpg
    for file in os.listdir(path):
        extension = file.split('.')[-1]
        if extension == 'jpg':
            fileLoc = path + file
            im = Image.open(fileLoc)
            im.save('path' + file.split('.')[0] + '.png')
else:
    print("Missing required arguments, check --help")
