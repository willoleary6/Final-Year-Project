


import mnist_data_set_loader
import NeuralNetwork

# Before we can start training we must first retrieve the data set
# from the data_set_loader we will populate the training data set, validation data set and the test data set
training_data, validation_data, test_data = mnist_data_set_loader.load_data_and_shape()

net = NeuralNetwork.NeuralNet([784, 30, 10])
epochs = 30
mini_batch_size = 10
learning_rate = 1.0
net.stochastic_gradient_decent(training_data, epochs, mini_batch_size, learning_rate, test_data=test_data)
