# Solution built from Google's "TensorFlow without a PHD" repository
# https://github.com/GoogleCloudPlatform/tensorflow-without-a-phd/tree/master/tensorflow-mnist-tutorial
# This solution uses the softmax function which grants reasonable accuracy_of_predictions
# but will be iteratively introducing new techniques to improve said accuracy_of_predictions.

import tensorflow as tf
import visualisation
import mnistdata
import math

tf.set_random_seed(0)

# 28*28     6*6*1       5*5*6       4*4*12      200          10          10
# Input     conv        conv        conv        ReLU     Softmax     Output
# O ->
# O ->      @ ->
# O ->      @ ->        @ ->
# O ->      @ ->        @ ->        @ ->
# O ->      @ ->        @ ->        @ ->        O ->
# . ->      @ ->        @ ->        @ ->        O ->        O ->        O   = 0
# . ->      . ->        . ->        @ ->        O ->        O ->        O   = 1
# . ->      . ->        . ->        . ->        . ->        . ->        .
# . ->      . ->        . ->        . ->        . ->        . ->        .
# . ->      . ->        . ->        . ->        . ->        . ->        .
# . ->      . ->        @ ->        @ ->        O ->        O ->        O   = 8
# . ->      @ ->        @ ->        @ ->        O ->        O ->        O   = 9
# O ->      @ ->        @ ->        @ ->        O ->
# O ->      @ ->        @ ->
# O ->      @ ->
# O ->
# O ->

NUMBER_OF_ITERATIONS = 2000
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

# introducing variable learning rate
# allows for finer adjustments in gradient decent so we don't over shoot local minimum
variable_learning_rate = tf.placeholder(tf.float32)
#  rate at which learning rate will be adjusted
iterations_so_far = tf.placeholder(tf.int32)

probability_of_saving_node_from_dropout = tf.placeholder(tf.float32)
# three convolutional layers with their channel counts, and a
# fully connected layer (the last layer has 10 softmax neurons)
input_layer_output_depth = 1
first_layer_output_depth = 6
second_layer_output_depth = 12
third_layer_output_depth = 24
fourth_layer_output_depth = 200
fifth_layer_output_depth = 10
# defining the dimensions and depths of each of the layers
first_conv_layer_dimensions_and_depth = [
    6,  # dimensions of convolution
    6,  # dimensions of convolution
    input_layer_output_depth,  # depth of previous layer output
    first_layer_output_depth  # output depth
]

second_conv_layer_dimensions_and_depth = [
    5,  # dimensions of convolution
    5,  # dimensions of convolution
    first_layer_output_depth,  # depth of previous layer output
    second_layer_output_depth  # output depth
]

third_conv_layer_dimensions_and_depth = [
    4,  # dimensions of convolution
    4,  # dimensions of convolution
    second_layer_output_depth,  # depth of previous layer output
    third_layer_output_depth  # output depth
]

fully_connected_relu_layer_dimensions = [
    7 * 7 * third_layer_output_depth,  # connections into feeding into layer
    fourth_layer_output_depth  # neurons in layer
]

output_layer = [
    fourth_layer_output_depth,
    fifth_layer_output_depth
]

array_of_weights_matrices = [
    # populating each layer of weights, initialised with small values to avoid exploding/vanishing gradients
    tf.Variable(tf.truncated_normal(first_conv_layer_dimensions_and_depth, stddev=0.1)),
    tf.Variable(tf.truncated_normal(second_conv_layer_dimensions_and_depth, stddev=0.1)),
    tf.Variable(tf.truncated_normal(third_conv_layer_dimensions_and_depth, stddev=0.1)),
    tf.Variable(tf.truncated_normal(fully_connected_relu_layer_dimensions, stddev=0.1)),
    tf.Variable(tf.truncated_normal(output_layer, stddev=0.1)),
]

array_of_bias_vectors = [
    tf.Variable(tf.constant(0.1, tf.float32, [first_layer_output_depth])),
    tf.Variable(tf.constant(0.1, tf.float32, [second_layer_output_depth])),
    tf.Variable(tf.constant(0.1, tf.float32, [third_layer_output_depth])),
    tf.Variable(tf.constant(0.1, tf.float32, [fourth_layer_output_depth])),
    tf.Variable(tf.constant(0.1, tf.float32, [fifth_layer_output_depth])),
]

division_of_output_dimensions = 1  # keep image in original size for first convolution
first_layer = tf.nn.relu(
    tf.nn.conv2d(
        image_matrix,  # feeding in the input layer
        array_of_weights_matrices[0],  # weights applied to the first layer
        strides=[  # sub sampling input
            1,
            division_of_output_dimensions,
            division_of_output_dimensions,
            1
        ],
        padding='SAME'
    ) + array_of_bias_vectors[0]
)

division_of_output_dimensions = 2  # sub sampling image to half its size
second_layer = tf.nn.relu(
    tf.nn.conv2d(
        first_layer,  # feeding in the first layer
        array_of_weights_matrices[1],  # weights applied to the second layer
        strides=[
            1,
            division_of_output_dimensions,
            division_of_output_dimensions,
            1
        ],
        padding='SAME'
    ) + array_of_bias_vectors[1]
)

division_of_output_dimensions = 2  # sub sampling image to half its size
third_layer = tf.nn.relu(
    tf.nn.conv2d(
        second_layer,  # feeding in the first layer
        array_of_weights_matrices[2],  # weights applied to the third layer
        strides=[
            1,
            division_of_output_dimensions,
            division_of_output_dimensions,
            1
        ],
        padding='SAME'
    ) + array_of_bias_vectors[2]
)

# reshape the output from the third convolution for the fully connected layer
reshaped_output_from_third_layer  = tf.reshape(third_layer, shape=[-1, 7 * 7 * third_layer_output_depth])

fully_connected_relu_layer = tf.nn.relu(
   tf.matmul(
       reshaped_output_from_third_layer, # reshaped output from third convolutional layer fed in
       array_of_weights_matrices[3] # multiply matrices by the weights matrices for each of these neurons in layer
   )
)

fully_connected_relu_layer_dropout = tf.nn.dropout(
    fully_connected_relu_layer,
    probability_of_saving_node_from_dropout
)

# logits for final layer mapping probability
final_layer_logits = tf.matmul(
    fully_connected_relu_layer_dropout,
    array_of_weights_matrices[4]
    ) + array_of_bias_vectors[4]

final_layer = tf.nn.softmax(final_layer_logits)

# cross-entropy loss function (= -sum(Y_i * log(Yi)) ), normalised for batches of 100  images
# TensorFlow provides the softmax_cross_entropy_with_logits function to avoid numerical stability
# problems with log(0) which is NaN
cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(logits=final_layer_logits, labels=label_matrix)
cross_entropy = tf.reduce_mean(cross_entropy) * 100

correct_predictions = tf.equal(  # building a tensor of all the correct predictions vs incorrect predictions
    tf.argmax(final_layer, 1),  # comparing the answer the final_layer generates against what the correct answer is
    tf.argmax(label_matrix, 1)
)
accuracy_of_predictions = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
reshaped_weights_matrices = []
# flattening the weights matrices and bias vectors for distribution graph
for i in array_of_weights_matrices:
    reshaped_weights_matrices.append(tf.reshape(i, [-1]))

all_weights = tf.concat(reshaped_weights_matrices, 0)

reshaped_bias_vectors = []
for j in array_of_bias_vectors:
    reshaped_bias_vectors.append(tf.reshape(j, [-1]))

all_biases = tf.concat(reshaped_bias_vectors, 0)

# this object will generate a visualisation of how the TensorFlow is learning
visualisation_of_training = visualisation.DataVisualisation('ReLU - incorporating dropout')

# the learning rate is: # 0.0001 + 0.003 * (1/e)^(iterations_so_far/NUMBER_OF_ITERATIONS)), i.e. exponential decay
# from 0.003->0.0001
lr = 0.0001 + tf.train.exponential_decay(
    0.003,
    iterations_so_far,
    NUMBER_OF_ITERATIONS,
    1 / math.e)

train_step = tf.train.AdamOptimizer(lr).minimize(cross_entropy)

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
                label_matrix: mini_batch_of_labels,
                probability_of_saving_node_from_dropout: 1.0,  # no culling
                iterations_so_far: iteration
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
            # no need for drop out here as we simply want to test TensorFlow
            feed_dict={
                image_matrix: data_set.testing_data_set.images,
                label_matrix: data_set.testing_data_set.labels,
                probability_of_saving_node_from_dropout: 1.0  # no culling
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
            label_matrix: mini_batch_of_labels,
            probability_of_saving_node_from_dropout: .75,  # cull 25% of neurons
            iterations_so_far: iteration
        }
    )


# using the visualiser as a driver for running the sessions
visualisation_of_training.animate(
    training_step,  # computation for each session
    iterations=NUMBER_OF_ITERATIONS + 1,  # how many times we will run the sessions
    train_data_update_frequency=10,  # how often we will run a new training mini batch
    test_data_update_freq=50,  # how often we will test TensorFlow against the test dataset
    more_tests_at_start=True  # if we want to test the first "test_data_update_freq" number of iterations
)

print("max test accuracy: " + str(visualisation_of_training.get_max_test_accuracy()))

