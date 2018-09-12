import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def display_image(i):
    img = test_data[i]
    plt.title('Mnist %d. Value: %d' % (i, test_labels[i]))
    # Several processes going on here. when we receive the image it is stored in a single array
    # we must reformat it to a 2D in order for us to display it properly.
    two_d_img = img.reshape((28, 28))
    # convert to grey scale
    plt.imshow(two_d_img, cmap=plt.cm.gray_r)
    # display to user
    plt.show()


learner = tf.contrib.learn
tf.logging.set_verbosity(tf.logging.ERROR)

# download data set from mnist
mnist_data_set = learner.datasets.load_dataset('mnist')

# training data
data = mnist_data_set.train.images
labels = np.asarray(mnist_data_set.train.labels, dtype=np.int32)

# test data
test_data = mnist_data_set.test.images
test_labels = np.asarray(mnist_data_set.test.labels, dtype=np.int32)

display_image(0)
# So far able to load sample data onto learner and we can display that too

