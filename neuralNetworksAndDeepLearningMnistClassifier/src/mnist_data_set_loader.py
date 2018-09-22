import pickle
import gzip
import numpy


def load_data_and_shape():
    # read data from file
    raw_training_data, raw_validation_data, raw_test_data = retrieve_data_from_file()

    # beginning reshape process
    # training data
    training_inputs = [numpy.reshape(x, (784, 1)) for x in raw_training_data[0]]
    training_results = [vectorized_result(j) for j in raw_training_data[1]]
    # formatting training data so that list contains but the inputs and expected result
    training_data = list(zip(training_inputs, training_results))

    # validation data
    validation_inputs = [numpy.reshape(x, (784, 1)) for x in raw_validation_data[0]]
    validation_data = list(zip(validation_inputs, raw_validation_data[1]))

    # test data
    test_inputs = [numpy.reshape(x, (784, 1)) for x in raw_test_data[0]]
    test_data = list(zip(test_inputs, raw_test_data[1]))

    return training_data, validation_data, test_data


def retrieve_data_from_file():
    # importing  data from file, using gzip to unpack file
    data_file = gzip.open('../data/mnist.pkl.gz', mode='rb')

    # using pickle to encode data set with latin alphabet
    # https://en.wikipedia.org/wiki/ISO/IEC_8859-1
    training_data, validation_data, test_data = pickle.load(data_file, encoding='iso-8859-1')

    # closing data set file
    data_file.close()

    # return data retrieved
    return training_data, validation_data, test_data


def vectorized_result(j):
    # creating an array of 10 length so the neural net can pick an answer
    result_vector = numpy.zeros((10, 1))
    # setting j to 1.0 for training neural net
    result_vector[j] = 1.0
    return result_vector
