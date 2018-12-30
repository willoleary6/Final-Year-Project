import tensorflow as tf
import numpy as np
from trainer.tasks import load_mnist_data
from trainer.tasks import load_and_inter_leaf_data_set_with_labels


class MnistData(object):
    def __init__(self, data_set, one_hot, reshape):
        self.pos = 0
        self.images = None
        self.labels = None
        data_set = data_set.batch(10000)
        data_set = data_set.repeat(1)
        features, labels = data_set.make_one_shot_iterator().get_next()

        if not reshape:
            features = tf.reshape(features, [-1, 28, 28, 1])
        if one_hot:
            labels = tf.one_hot(labels, 10)
        with tf.Session() as sess:

            while True:
                try:
                    feats, labs = sess.run([features, labels])
                    self.images = feats if self.images is None else np.concatenate([self.images, feats])
                    self.labels = labs if self.labels is None else np.concatenate([self.labels, labs])
                except tf.errors.OutOfRangeError:
                    break

    def next_batch(self, batch_size):
        if self.pos + batch_size > len(self.images) or self.pos + batch_size > len(self.labels):
            self.pos = 0
        res = (self.images[self.pos:self.pos + batch_size], self.labels[self.pos:self.pos + batch_size])
        self.pos += batch_size
        return res


class Mnist(object):
    def __init__(self, training_data_set, testing_data_set, one_hot, reshape):
        self.train = MnistData(training_data_set, one_hot, reshape)
        self.test = MnistData(testing_data_set, one_hot, reshape)


def read_data_sets_into_memory(data_set_file_path, one_hot, reshape):
    training_images_file, training_labels_file, \
        testing_images_file, testing_labels_file = load_mnist_data(data_set_file_path)
    training_data_set = load_and_inter_leaf_data_set_with_labels(training_images_file, training_labels_file)
    training_data_set = training_data_set.shuffle(60000)

    testing_data_set = load_and_inter_leaf_data_set_with_labels(testing_images_file, testing_labels_file)
    mnist = Mnist(training_data_set, testing_data_set, one_hot, reshape)

    return mnist
