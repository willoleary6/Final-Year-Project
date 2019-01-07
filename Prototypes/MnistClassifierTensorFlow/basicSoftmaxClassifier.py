# Solution built from Google's "TensorFlow without a PHD" repository
# https://github.com/GoogleCloudPlatform/tensorflow-without-a-phd/tree/master/tensorflow-mnist-tutorial
# This solution uses the softmax function which grants reasonable accuracy_of_predictions
# but will be iteratively introducing new techniques to improve said accuracy_of_predictions.

import tensorflow as tf
import visualisation
import mnistdata

# setting the graph-level random seed.
tf.set_random_seed(0)
# this network is not deep and only a single layer exists between the input and out put
# input layer is of 784 (number of pixels in flattened mnist image)
# 10 neurons in center and output layer

# 784        10            10
#  O    ->
#  O    ->
#  O    ->
#  O    ->
#  O    ->
#  O    ->    O     ->    O   =  0
#  O    ->    O     ->    O   =  1
#  O    ->    O     ->    O   =  2
#  .    ->    O     ->    O   =  3
#  .    ->    O     ->    O   =  4
#  .    ->    O     ->    O   =  5
#  .    ->    O     ->    O   =  6
#  O    ->    O     ->    O   =  7
#  O    ->    O     ->    O   =  8
#  O    ->    O     ->    O   =  9
#  O    ->
#  O    ->
#  O    ->
#  O    ->
#  O    ->


# using softmax is defined as the following
# i = flattened matrix of images
# w = matrix of weights
# b = vector of biases

# model = softmax((i * w) + b)

# first we must procure dataset
# encoding dataset in one hot so it can be fed later
data_set = mnistdata.read_data_sets_into_memory("data", one_hot=True, reshape=False)

# matrix of tensor containing the image
image_matrix = tf.placeholder(
    tf.float32,
    [
        None,  # index of image in mini-batch
        28,  # dimensions of image
        28,
        1
    ])
# matrix of labels
label_matrix = tf.placeholder(
    tf.float32,
    [
        None,  # index of labels in mini_batch
        10  # 10 possible unique labels
    ]
)
# declaring the weights matrix, setting everything to start zero
# each neuron in the input layer will feed into the 10 neurons in the middle layer
weights_matrix = tf.Variable(
    tf.zeros(
        [
            784,  # number of weights coming out of the input layer
            10  # number of neurons that the 784 weights will all be applied too
        ]
    )
)
# since we only have one layer for computation we don't need a matrix, a simple vector will suffice
bias_vector = tf.Variable(
    tf.zeros(
        [
            10  # only one middle layer so we just need a column of size 10 for each neurons bias
        ]
    ))
# flattening the image matrix from 28*28 to 784*1
flattened_image_matrix =  tf.layers.flatten(image_matrix)

# defining the softmax activation
softmax_model = tf.nn.softmax(
    tf.matmul(flattened_image_matrix, weights_matrix)  # multiplying the weights by the flattened image matrix
    + bias_vector  # adding the bias to apply the bias to each of the 10 neurons in the middle layer
)

# now we must define the cost function or cross-entropy
# this formula returns the negative sum of
# multiplying the label matrix (the desired output) by the log of
# each element in the softmax_model

# this function will calculate the total cost for all images
# in the batch through using the softmax_model
cross_entropy = -tf.reduce_mean(
    label_matrix * tf.log(softmax_model)
) * 1000  # we must multiply by 1000 as reduce_mean divides by 1000 that is not wanted

# defining how to calculate the number of correct predictions
correct_predictions = tf.equal(  # building a tensor of all the correct predictions vs incorrect predictions
    tf.argmax(softmax_model, 1),  # comparing the answer the softmax model generates against what the correct answer is
    tf.argmax(label_matrix, 1)
)
accuracy_of_predictions = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

# defining how the network will training_data_set
learning_rate = 0.005  # defining by how much the TensorFlow should adjust the weights and biases
# Employing gradient decent as our training optimiser
# basing the the optimiser on the cost (cross entropy) value
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

# reshaping the weights and biases for the visualisation
all_weights = tf.reshape(weights_matrix, [-1])
all_biases = tf.reshape(bias_vector, [-1])

# this object will generate a visualisation of how the TensorFlow is learning
visualisation_of_training = visualisation.DataVisualisation('Softmax')

# initialising the TensorFlow session
initialisation = tf.global_variables_initializer()
# defining the session
session = tf.Session()
# running the session to complete initialisation
session.run(initialisation)


# now to define how the session will compute each mini-batch through iterations
def training_step(iteration, compute_next_batch_of_test_data, compute_next_batch_of_training_data):
    # feeding in the next mini-batch of images
    mini_batch_of_images, mini_batch_of_labels = data_set.training_data_set.next_batch(100)

    if compute_next_batch_of_training_data:
        # running training for this iteration
        accuracy_from_session, cross_entropy_from_session, weights_from_session, biases_from_session = session.run(
            [
                accuracy_of_predictions,
                cross_entropy,
                all_weights,
                all_biases
            ],
            feed_dict={
                image_matrix: mini_batch_of_images,
                label_matrix: mini_batch_of_labels
            }
        )
        # update the training graphs
        visualisation_of_training.append_training_curves_data(
            iteration, accuracy_from_session, cross_entropy_from_session
        )

        visualisation_of_training.append_data_histograms(
            iteration, weights_from_session, biases_from_session
        )
        # printing to command line
        print(
            str(iteration) + ": accuracy:" +
            str(accuracy_from_session) +
            " loss: " + str(cross_entropy_from_session)
        )
    if compute_next_batch_of_test_data:
        # testing the TensorFlow against the test data set
        accuracy_from_session, cross_entropy_from_session = session.run(
            [
                accuracy_of_predictions,
                cross_entropy
            ],
            feed_dict={
                image_matrix: data_set.testing_data_set.images,
                label_matrix: data_set.testing_data_set.labels
            }
        )
        # update the test graphs
        visualisation_of_training.append_test_curves_data(
            iteration,
            accuracy_from_session,
            cross_entropy_from_session
        )
        # printing to command line
        print(
            str(iteration) + ": ********* epoch " +
            str(iteration * 100 // data_set.training_data_set.images.shape[0] + 1) +
            " ********* test accuracy:" + str(accuracy_from_session) +
            " test loss: " + str(cross_entropy_from_session)
        )
    # now to run backpropagation
    session.run(
        train_step,  # gradient descent
        feed_dict={
            image_matrix: mini_batch_of_images,
            label_matrix: mini_batch_of_labels
        }
    )


# using the visualiser as a driver for running the sessions
visualisation_of_training.animate(
    training_step,  # computation for each session
    iterations=2000 + 1,  # how many times we will run the sessions
    train_data_update_frequency=10,  # how often we will run a new training mini batch
    test_data_update_freq=50,  # how often we will test TensorFlow against the test dataset
    more_tests_at_start=True  # if we want to test the first "test_data_update_freq" number of iterations
)

print("max test accuracy: " + str(visualisation_of_training.get_max_test_accuracy()))
