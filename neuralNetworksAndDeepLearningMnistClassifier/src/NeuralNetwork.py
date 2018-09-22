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
        # number of layers in neuralNet
        self.number_of_layers = len(net_sizes)
        self.net_sizes = net_sizes
        # selecting a random set of biases
        self.biases = [numpy.random.randn(i, 1) for i in net_sizes[1:]]
        # selecting random weights
        self.weights = [numpy.random.randn(i, j) for i, j in zip(net_sizes[:-1], net_sizes[:-1])]
