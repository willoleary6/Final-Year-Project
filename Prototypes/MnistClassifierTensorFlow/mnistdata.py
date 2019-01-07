# encoding: UTF-8
# Copyright 2018 Google.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf
import numpy as np
from trainer.tasks import load_mnist_data
from trainer.tasks import load_and_inter_leaf_data_set_with_labels

# This loads entire dataset to an in-memory numpy array.
# This uses tf.data.Dataset to avoid duplicating code.
# Normally, if you already have a tf.data.Dataset, loading
# it to memory is not useful. The goal here is educational:
# teach about neural network basics without having to
# explain tf.data.Dataset now. The concept will be introduced
# later.
# The proper way of using tf.data.Dataset is to call
# features, labels = tf_dataset.make_one_shot_iterator().get_next()
# and then to use "features" and "labels" in your Tensorflow
# model directly. These tensorflow nodes, when executed, will
# automatically trigger the loading of the next batch of data.
# The sample that uses tf.data.Dataset correctly is in mlengine/trainer.


class MnistData(object):
    def __init__(self, data_set, one_hot, reshape):
        self.position = 0
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
        if self.position + batch_size > len(self.images) or self.position + batch_size > len(self.labels):
            self.position = 0
        res = (self.images[self.position:self.position + batch_size], self.labels[self.position:self.position + batch_size])
        self.position += batch_size
        return res


class Mnist(object):
    def __init__(self, training_data_set, testing_data_set, one_hot, reshape):
        self.training_data_set = MnistData(training_data_set, one_hot, reshape)
        self.testing_data_set = MnistData(testing_data_set, one_hot, reshape)


def read_data_sets_into_memory(data_set_file_path, one_hot, reshape):
    training_images_file, training_labels_file, \
        testing_images_file, testing_labels_file = load_mnist_data(data_set_file_path)
    training_data_set = load_and_inter_leaf_data_set_with_labels(training_images_file, training_labels_file)
    training_data_set = training_data_set.shuffle(60000)

    testing_data_set = load_and_inter_leaf_data_set_with_labels(testing_images_file, testing_labels_file)
    mnist = Mnist(training_data_set, testing_data_set, one_hot, reshape)

    return mnist



