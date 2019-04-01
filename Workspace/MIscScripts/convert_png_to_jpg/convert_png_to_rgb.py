from PIL import Image
import numpy as np
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-p",
                    "-path_to_png",
                    dest="path_to_png",
                    help="File path to the directory containing the png files",
                    default=False
                    )

args = parser.parse_args()
if args.path_to_png:
    path = args.path_to_png
    for file in os.listdir(path):
        extension = file.split('.')[-1]
        if extension != 'xml':
            fileLoc = path + file
            img = Image.open(fileLoc).convert('RGBA')
            x = np.array(img)
            r, g, b, a = np.rollaxis(x, axis=-1)
            r[a == 0] = 255
            g[a == 0] = 255
            b[a == 0] = 255
            x = np.dstack([r, g, b, a])
            img = Image.fromarray(x, 'RGBA')
            img.save(path + file.split('.')[0] + '.jpg')
else:
    print("Missing required arguments, check --help")
