import tensorflow as tf
from tensorflow.python.platform import tf_logging as logging

from trainer.download_gzip_file_and_unzip import download_gzip_file_and_unzip

logging.set_verbosity(logging.INFO)
logging.log(logging.INFO, "Tensorflow version " + tf.__version__)


def load_mnist_data(data_destination_directory):
    data_set_url = 'https://storage.googleapis.com/cvdf-datasets/mnist/'
    # download each of the files we need and unzip it
    training_images_zipped_file = 'train-images-idx3-ubyte.gz'
    local_training_images_file = download_gzip_file_and_unzip(training_images_zipped_file, data_destination_directory,
                                                              data_set_url + training_images_zipped_file)
    training_labels_file = 'train-labels-idx1-ubyte.gz'
    local_training_labels_file = download_gzip_file_and_unzip(training_labels_file, data_destination_directory,
                                                              data_set_url + training_labels_file)

    testing_images_file = 't10k-images-idx3-ubyte.gz'
    local_testing_images_file = download_gzip_file_and_unzip(testing_images_file, data_destination_directory,
                                                              data_set_url + testing_images_file)
    testing_labels_file = 't10k-labels-idx1-ubyte.gz'
    local_testing_labels_file = download_gzip_file_and_unzip(testing_labels_file, data_destination_directory,
                                                             data_set_url + testing_labels_file)
    return local_training_images_file, local_training_labels_file, local_testing_images_file, local_testing_labels_file


def decode_raw_image(tf_byte_string):
    # converting the raw data
    image = tf.decode_raw(tf_byte_string, tf.uint8)
    # casting the decoded image into 32bit characters and returning
    return tf.cast(image, tf.float32) / 256.0


def decode_raw_label(tf_byte_string):
    label = tf.decode_raw(tf_byte_string, tf.uint8)
    return tf.reshape(label, [])


def load_and_inter_leaf_data_set_with_labels(images_filename, labels_filename):
    # combining our images and our labels for training
    # first we have to decode the data
    images_data_set = tf.data.FixedLengthRecordDataset(images_filename, 28 * 28,
                                                       header_bytes=16, buffer_size=1024 * 16).map(decode_raw_image)
    labels_data_set = tf.data.FixedLengthRecordDataset(labels_filename, 1,
                                                       header_bytes=8, buffer_size=1024 * 16).map(decode_raw_label)
    # zip the data sets up and return them
    data_set = tf.data.Dataset.zip((images_data_set, labels_data_set))
    return data_set



