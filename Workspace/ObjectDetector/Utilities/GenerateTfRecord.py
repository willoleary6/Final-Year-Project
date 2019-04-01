from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
# path set in project interpreter settings
from object_detection.utils import dataset_util
from collections import namedtuple


class GenerateTfRecord:
    # converting the csv files to tf records so they can be fed to TensorFlow
    def __init__(self, csv_input, output_path, image_dir, labels):
        self.csv_input = csv_input
        self.output_path = output_path
        self.image_dir = image_dir
        self.labels = labels

    def write_record(self):
        try:
            writer = tf.python_io.TFRecordWriter(self.output_path)
            image_directory_path = os.path.join(self.image_dir)
            examples = pd.read_csv(self.csv_input)
            grouped = self.split(examples, 'filename')
            for group in grouped:
                tf_example = self.create_tf_record(group, image_directory_path)
                writer.write(tf_example.SerializeToString())

            writer.close()
            return True
        except Exception as e:
            return False

    @staticmethod
    def split(df, group):
        data = namedtuple('data', ['filename', 'object'])
        gb = df.groupby(group)
        return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

    def class_text_to_int(self, row_label):
        count = 1
        for i in self.labels:
            if i == row_label:
                return count
            count += 1

    def create_tf_record(self, group, path):
        with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
            encoded_jpg = fid.read()
        encoded_jpg_io = io.BytesIO(encoded_jpg)
        image = Image.open(encoded_jpg_io)
        width, height = image.size

        filename = group.filename.encode('utf8')
        image_format = b'jpg'
        xmins = []
        xmaxs = []
        ymins = []
        ymaxs = []
        classes_text = []
        classes = []

        for index, row in group.object.iterrows():
            xmins.append(row['xmin'] / width)
            xmaxs.append(row['xmax'] / width)
            ymins.append(row['ymin'] / height)
            ymaxs.append(row['ymax'] / height)
            classes_text.append(row['class'].encode('utf8'))
            classes.append(self.class_text_to_int(row['class']))

        tf_example = tf.train.Example(features=tf.train.Features(feature={
            'image/height': dataset_util.int64_feature(height),
            'image/width': dataset_util.int64_feature(width),
            'image/filename': dataset_util.bytes_feature(filename),
            'image/source_id': dataset_util.bytes_feature(filename),
            'image/encoded': dataset_util.bytes_feature(encoded_jpg),
            'image/format': dataset_util.bytes_feature(image_format),
            'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
            'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
            'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
            'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
            'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
            'image/object/class/label': dataset_util.int64_list_feature(classes),
        }))
        return tf_example
