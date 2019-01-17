from PIL import Image
from scipy.misc import imread, imsave, imresize
import os
path = 'C:\SourceCode\Final-Year-Project\Images\prototype_images\\fingers\\test\\'
for file in os.listdir(path):
     extension = file.split('.')[-1]
     if extension == 'jpg':
        fileLoc = path + file
        im = Image.open(fileLoc)
        im.save('C:\SourceCode\Final-Year-Project\Images\prototype_images\\fingers\\test\\'+file.split('.')[0]+'.png')

