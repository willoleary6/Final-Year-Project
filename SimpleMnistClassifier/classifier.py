import os
import tensorflow as tf
import tensorflowVisualiser

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from mnist_data import read_data_sets_into_memory

print("Version " + tf.__version__)
tf.set_random_seed(0)

mnist = read_data_sets_into_memory("data", one_hot=True, reshape=False)

input = tf.placeholder(tf.float32, [None, 28, 28, 1])

correct_answers = tf.placeholder(tf.float32, [None, 10])

weights = tf.Variable(tf.zeros([784, 10]))
biases = tf.Variable(tf.zeros([10]))
flattened_input = tf.reshape(input, [-1, 784])

model = tf.nn.softmax(tf.matmul(flattened_input, weights) + biases)

cross_entropy = -tf.reduce_mean(correct_answers * tf.log(model)) * 1000.0

correct_prediction = tf.equal(tf.argmax(model, 1), tf.argmax(correct_answers, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

train_step = tf.train.GradientDescentOptimizer(0.005).minimize(cross_entropy)

all_weights = tf.reshape(weights, [-1])
all_biases = tf.reshape(biases, [-1])

I = tensorflowVisualiser.tf_format_mnist_images(input, model, correct_answers)


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
