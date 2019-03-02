import math
import os
import random


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f",
                    "-filePath",
                    dest="filePath",
                    help="File path to the directory used to store the csv files",
                    default=False
                    )

args = parser.parse_args()

if args.filePath:
    file_names = []
    list_of_all_files = os.listdir(args.filePath)
    for file_name in list_of_all_files:
        extension = file_name.split('.')[-1]
        file_name = file_name.split('.')[0]
        if extension != 'xml':
            file_names.append(file_name)
    #   shuffling array
    random.shuffle(file_names)
    test_percentage = 10
    number_of_images_going_to_test = math.ceil(len(file_names) * (test_percentage / 100))
    args.filePath = args.filePath.replace('\\', '/')
    os.mkdir(args.filePath+'/test')
    os.mkdir(args.filePath+'/train')
    for x, file in enumerate(file_names):
        if x <= number_of_images_going_to_test:
            destination_directory = args.filePath+'/test/'+file
        else:
            destination_directory = args.filePath+'/train/'+file

        os.rename(args.filePath+'/'+file+'.jpg', destination_directory+'.jpg')
        os.rename(args.filePath+'/'+file+'.xml', destination_directory+'.xml')

else:
    print("Missing required arguments, check --help")
