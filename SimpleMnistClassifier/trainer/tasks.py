import tensorflow as tf
from tensorflow.python.platform import tf_logging as logging

from trainer.download_gzip_file_and_unzip import download_gzip_file_and_unzip

logging.set_verbosity(logging.INFO)
logging.log(logging.INFO, "Tensorflow version " + tf.__version__)


def load_mnist_data(data_destination_directory):
    # url we are using to pull MNIST data set
    data_set_url = 'https://storage.googleapis.com/cvdf-datasets/mnist/'
    # Download and unzip the training images
    training_images_filename = 'train-images-idx3-ubyte.gz'
    training_images = download_gzip_file_and_unzip(training_images_filename, data_destination_directory,
                                                   data_set_url + training_images_filename)
    # Also need their labels....
    training_labels_filename = 'train-labels-idx1-ubyte.gz'
    training_labels = download_gzip_file_and_unzip(training_labels_filename, data_destination_directory,
                                                   data_set_url + training_labels_filename)
    # Same process with test data set
    test_images_filename = 't10k-images-idx3-ubyte.gz'
    test_images = download_gzip_file_and_unzip(training_labels_filename, data_destination_directory,
                                               data_set_url + test_images_filename)

    test_labels_filename = 't10k-labels-idx1-ubyte.gz'
    test_labels = download_gzip_file_and_unzip(training_labels_filename, data_destination_directory,
                                               data_set_url + test_labels_filename)

    return training_images, training_labels, test_images, test_labels


def decode_raw_image(tf_byte_string):
    # converting the raw data
    image = tf.decode_raw(tf_byte_string, tf.uint8)
    # casting the decoded image into 32bit characters and returning
    return tf.cast(image, tf.float32) / 256.0


def decode_raw_label(tf_byte_string):
    # converting the raw labels data into unsigned 8 bit integers
    label = tf.decode_raw(tf_byte_string, tf.uint8)
    return tf.reshape(label, [])


def load_and_inter_leaf_data_set_with_labels(images_filename, labels_filename):
    # combining our images and our labels for training
    # first we have to decode the data
    images_data_set = tf.data.FixedLengthRecordDataset(images_filename, 28 * 28,
                                                       header_bytes=15, buffer_size=1024 * 16).map(decode_raw_image)
    labels_data_set = tf.data.FixedLengthRecordDataset(labels_filename, 1,
                                                       header_bytes=8, buffer_size=1024 * 16).map(decode_raw_label)
    # zip the data sets up and return them
    data_set = tf.data.Dataset.zip((images_data_set, labels_data_set))
    return data_set



