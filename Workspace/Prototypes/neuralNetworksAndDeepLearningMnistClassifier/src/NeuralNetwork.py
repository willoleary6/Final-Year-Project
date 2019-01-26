import numpy
import random


def sigmoid(sum_of_weights_and_biases):
    # calculating σ
    return 1.0 / (1.0 + numpy.exp(-sum_of_weights_and_biases))


def sigmoid_derivative(sum_of_weights_and_biases):
    # calculating dσ(x)/d(x)= σ(x)*(1−σ(x))
    return sigmoid(sum_of_weights_and_biases) * (1 - sigmoid(sum_of_weights_and_biases))


class NeuralNet(object):
    # initialising class
    def __init__(self, net_sizes):  # the list sizes contains the number of neurons in the respective layers.
        self.net_sizes = net_sizes
        # number of layers in neuralNet
        self.number_of_layers = len(net_sizes)
        # selecting a random set of biases
        self.biases = [numpy.random.randn(i, 1) for i in self.net_sizes[1:]]
        # selecting random weights
        self.weights = [numpy.random.randn(j, i) for i, j in zip(self.net_sizes[:-1], self.net_sizes[1:])]

    def stochastic_gradient_decent(self, training_data, epochs, mini_batch_size, learning_rate, test_data=None):
        # our method of training neural net
        """
        training-data: This is the data we will use to train the neuralNet to recognise the digits.

        epochs: The number of times we will feed the data set through the neural net in the training process.

        mini_batch_size: The number of randomly selected tuples of weights and biases used to help calculate
        the current gradient.

        learning_rate: Also represented as η, this parameter will be used to adjust the rate at which we will change the
        weights and biases.

        test_data: If populated this parameter will be used to evaluate the neural net after each iteration.
        """
        # if test_data is None don't evaluate
        if test_data:
            new_test = len(test_data)
        training_data_length = len(training_data)
        for i in range(epochs):
            random.shuffle(training_data)
            # populating mini_batches with shuffled training data
            mini_batches = [training_data[j:j + mini_batch_size]
                            for j in range(0, training_data_length, mini_batch_size)]

            # applying gradient decent
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, learning_rate)

            if test_data:
                print("Epoch {0}: {1} / {2}".format(i, self.evaluate_neural_net_performance(test_data), new_test))
            else:
                print("Epoch {0} complete".format(i))

    def update_mini_batch(self, mini_batch, learning_rate):
        """
            updating the networks weights and biases by applying gradient descent using the back-propagation to
            each of the mini-batches.

            mini-batch: This is a list of randomly selected tuples of training images.

            learning_rate: Also represented as η, this parameter will be used to adjust the rate at which we will change the
            weights and biases.

        """
        # inverting delta of biases
        # nabla = ∇
        nabla_biases = [numpy.zeros(bias.shape) for bias in self.biases]
        nabla_weights = [numpy.zeros(weight.shape) for weight in self.weights]

        for digit, result in mini_batch:
            delta_nabla_biases, delta_nabla_weights = self.back_propagation(digit, result)
            # updating the biases and weights
            nabla_biases = [nabla_bias + delta_nabla_bias
                            for nabla_bias, delta_nabla_bias in zip(nabla_biases, delta_nabla_biases)]
            nabla_weights = [nabla_weight + delta_nabla_weight
                             for nabla_weight, delta_nabla_weight in zip(nabla_weights, delta_nabla_weights)]

        # applying gradient descent update rule
        self.biases = [bias - (learning_rate / len(mini_batch)) * nabla_bias
                       for bias, nabla_bias in zip(self.biases, nabla_biases)]
        self.weights = [weight - (learning_rate / len(mini_batch)) * nabla_weight
                        for weight, nabla_weight in zip(self.weights, nabla_weights)]

    def back_propagation(self, digit, result):
        # nabla = ∇
        nabla_biases = [numpy.zeros(bias.shape) for bias in self.biases]
        nabla_weights = [numpy.zeros(weight.shape) for weight in self.weights]

        # feeding digit forward
        activation = digit
        # storing activations in this list
        activations = [digit]
        # storing all our x vectors here
        z_vectors = []

        for bias, weight in zip(self.biases, self.weights):
            z_vector = numpy.dot(weight, activation) + bias
            z_vectors.append(z_vector)
            activation = sigmoid(z_vector)
            activations.append(activation)

        # backward pass
        # delta = Δ
        cost_derivative = self.calculate_cost_derivative(activations[-1], result)

        delta = cost_derivative * sigmoid_derivative(activations[-1])
        nabla_biases[-1] = delta
        nabla_weights[-1] = numpy.dot(delta, activations[-2].transpose())

        for i in range(2, self.number_of_layers):
            z_vector = z_vectors[-i]
            sig_deriv = sigmoid_derivative(z_vector)
            delta = numpy.dot(self.weights[-i + 1].transpose(), delta) * sig_deriv
            nabla_biases[-i] = delta
            nabla_weights[-i] = numpy.dot(delta, activations[-i - 1].transpose())

        return nabla_biases, nabla_weights

    @staticmethod
    def calculate_cost_derivative(output_activation, result):
        # calculating the partial derivatives for output activations
        cost_derivative = output_activation - result
        return cost_derivative

    def evaluate_neural_net_performance(self, test_data):
        # returns the number of inputs the neural net correctly classifies
        evaluation_results = [(numpy.argmax(self.feed_forward(digit)), result)
                              for digit, result in test_data]
        return sum(int(result == expected_result)
                   for result, expected_result in evaluation_results)

    def feed_forward(self, digit):
        # checking to see what the neural net will output if we pass a digit through as input
        for bias, weight in zip(self.biases, self.weights):
            digit = sigmoid(numpy.dot(weight, digit) + bias)
        return digit
