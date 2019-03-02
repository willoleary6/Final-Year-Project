# taken from https://github.com/datitran/raccoon_dataset
#modified to work with command line arguements
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from argparse import ArgumentParser


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            last_member_index = len(member) - 1
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[last_member_index][0].text),
                     int(member[last_member_index][1].text),
                     int(member[last_member_index][2].text),
                     int(member[last_member_index][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


parser = ArgumentParser()
parser.add_argument("-x",
                    "-xmlDir",
                    dest="xmlDirectory",
                    help="File path to the directory containing both the test and train directory of xml files",
                    default=False
                    )
parser.add_argument("-d",
                    "-destinationDir",
                    dest="destinationDirectory",
                    help="File path to the directory used to store the csv files",
                    default=False
                    )

args = parser.parse_args()

if args.xmlDirectory and args.destinationDirectory:
    for directory in ['train', 'test']:
        xml_path = args.xmlDirectory + directory
        xml_df = xml_to_csv(xml_path)
        xml_df.to_csv(args.destinationDirectory + directory + '_labels.csv', index=None)
        #xml_df.to_csv('data/' + directory + '_labels.csv', index=None)
        print('Successfully converted xml to csv. Stored in '+args.destinationDirectory + directory + '_labels.csv')
else:
    print("Missing required arguments, check --help")
