from PIL import Image
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-p",
                    "-path_to_directory",
                    dest="path_to_directory",
                    help="File path to the directory ",
                    default=False
                    )

args = parser.parse_args()
if args.path_to_directory:
    path = args.path_to_directory
    for file in os.listdir(path):
        extension = file.split('.')[-1]
        if extension != 'xml':
            fileLoc = path + file
            img = Image.open(fileLoc)
            if img.mode != 'RGB':
                print(file + ', ' + img.mode)

else:
    print("Missing required arguments, check --help")
