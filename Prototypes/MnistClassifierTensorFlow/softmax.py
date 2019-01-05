# encoding: UTF-8
# Copyright 2016 Google.com
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
import visualisation
import mnistdata

#print("Tensorflow version " + tf.__version__)
tf.set_random_seed(0)

# neural network with 1 layer of 10 softmax neurons
#
# · · · · · · · · · ·       (input data, flattened pixels)       images_matrix [batch, 784]   # 784 = 28 * 28
# \x/x\x/x\x/x\x/x\x/    -- fully connected layer (softmax)      weights_matrix [784, 10]     bias_vector[10]
#   · · · · · · · ·                                              model [batch, 10]

# The model is:
#
# model = softmax( flattened_image_matrix * weights_matrix + bias_vector)
#              flattened_image_matrix: matrix for 100 grayscale images of 28x28 pixels,
#              flattened (there are 100 images in a mini-batch)
#
#              weights_matrix: weight matrix with 784 lines and 10 columns
#              bias_vector: bias vector with 10 dimensions
#              +: add with broadcasting: adds the vector to each line of the matrix (numpy)
#              softmax(matrix) applies softmax on each line
#              softmax(line) applies an exp to each value then divides by the norm of the resulting line
#              model: output matrix with 100 lines and 10 columns

# Download images and labels into mnist.test (10K images+labels) and mnist.train (60K images+labels)
mnist = mnistdata.read_data_sets_into_memory("data", one_hot=True, reshape=False)

# input images_matrix: 28x28 grayscale images, the first dimension (None) will index the images in the mini-batch
images_matrix = tf.placeholder(tf.float32, [None, 28, 28, 1])
# correct answers will go here
labels_matrix = tf.placeholder(tf.float32, [None, 10])
# weights weights_matrix[784, 10]   784=28*28
weights_matrix = tf.Variable(tf.zeros([784, 10]))
# biases bias_vector[10]
bias_vector = tf.Variable(tf.zeros([10]))

# flatten the images into a single line of pixels
# -1 in the shape definition means "the only possible dimension that will preserve the number of elements"
flattened_image_matrix = tf.reshape(images_matrix, [-1, 784])

# The model
model = tf.nn.softmax(tf.matmul(flattened_image_matrix, weights_matrix) + bias_vector)

# loss function: cross-entropy = - sum( Y_i * log(Yi) )
#                           model: the computed output vector
#                           labels_matrix: the desired output vector

# cross-entropy
# log takes the log of each element, * multiplies the tensors element by element
# reduce_mean will add all the components in the tensor

# so here we end up with the total cross-entropy for all images in the batch
# normalized for batches of 100 images,
# *10 because  "mean" included an unwanted division by 10
cross_entropy = -tf.reduce_mean(labels_matrix * tf.log(model)) * 1000.0


# accuracy of the trained model, between 0 (worst) and 1 (best)
correct_prediction = tf.equal(tf.argmax(model, 1), tf.argmax(labels_matrix, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# training, learning rate = 0.005
train_step = tf.train.GradientDescentOptimizer(0.005).minimize(cross_entropy)

# matplotlib visualisation
all_weights = tf.reshape(weights_matrix, [-1])
all_biases = tf.reshape(bias_vector, [-1])

data_visualisation = visualisation.DataVisualisation('softmax')

# init
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


# You can call this function in a loop to train the model, 100 images at a time
def training_step(i, update_test_data, update_train_data):

    # training on batches of 100 images with 100 labels
    mini_batch_of_images, mini_batch_of_labels = mnist.train.next_batch(100)

    # compute training values for visualisation
    if update_train_data:
        a, c, w, b = sess.run([accuracy, cross_entropy, all_weights, all_biases], feed_dict={images_matrix: mini_batch_of_images, labels_matrix: mini_batch_of_labels})
        data_visualisation.append_training_curves_data(i, a, c)
        data_visualisation.append_data_histograms(i, w, b)
        print(str(i) + ": accuracy:" + str(a) + " loss: " + str(c))

    # compute test values for visualisation
    if update_test_data:
        a, c = sess.run([accuracy, cross_entropy], feed_dict={images_matrix: mnist.test.images, labels_matrix: mnist.test.labels})
        data_visualisation.append_test_curves_data(i, a, c)
        print(str(i) + ": ********* epoch " + str(i*100//mnist.train.images.shape[0]+1) + " ********* test accuracy:" + str(a) + " test loss: " + str(c))

    # the backpropagation training step
    sess.run(train_step, feed_dict={images_matrix: mini_batch_of_images, labels_matrix: mini_batch_of_labels})


data_visualisation.animate(training_step, iterations=2000 + 1, train_data_update_frequency=10, test_data_update_freq=50, more_tests_at_start=True)

# to save the matplotlib_animation as a movie, add save_movie=True as an argument to data_visualisation.animate
# to disable the visualisation use the following line instead of the data_visualisation.animate line
# for i in range(2000+1): training_step(i, i % 50 == 0, i % 10 == 0)

print("max test accuracy: " + str(data_visualisation.get_max_test_accuracy()))

# final max test accuracy = 0.9268 (10K training_iteration). Accuracy should peak above 0.92 in the first 2000 training_iteration.
