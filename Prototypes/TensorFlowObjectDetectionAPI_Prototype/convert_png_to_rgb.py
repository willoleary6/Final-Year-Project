from PIL import Image
import numpy as np
import os
path = 'C:\SourceCode\Final-Year-Project\Images\prototype_images\\fingers\\test\\'
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
        img.save(path+file.split('.')[0]+'.jpg')

