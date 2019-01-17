from PIL import Image
import os
path = 'C:\SourceCode\Final-Year-Project\Images\prototype_images\\fingers\\train\\'
for file in os.listdir(path):
     extension = file.split('.')[-1]
     if extension != 'xml':
           fileLoc = path+file
           img = Image.open(fileLoc)
           if img.mode != 'RGB':
                 print(file+', '+img.mode)
