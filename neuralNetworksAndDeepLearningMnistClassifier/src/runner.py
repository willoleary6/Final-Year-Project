


import mnist_data_set_loader
import NeuralNetwork

# Before we can start training we must first retrieve the data set
# from the data_set_loader we will populate the training data set, validation data set and the test data set
training_data, validation_data, test_data = mnist_data_set_loader.load_data_and_shape()

net = NeuralNetwork.NeuralNet([784, 30, 10])
# net.SGD(training_data, 30, 10, 1.0, test_data=test_data)
