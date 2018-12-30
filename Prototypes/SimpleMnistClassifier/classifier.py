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
# 1000 images on 25 lines
It = tensorflowVisualiser.tf_format_mnist_images(input, model, correct_answers, 1000, lines=25)
data_visualisation = tensorflowVisualiser.VisualiseMnistDataSet()

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


# You can call this function in a loop to train the model, 100 images at a time
def training_step(i, update_test_data, update_train_data):
    # training on batches of 100 images with 100 labels
    batch_X, batch_Y = mnist.train.next_batch(100)

    # compute training values for visualisation
    if update_train_data:
        a, c, im, w, b = sess.run([accuracy, cross_entropy, I, all_weights, all_biases],
                                  feed_dict={input: batch_X, correct_answers: batch_Y})
        data_visualisation.append_training_curves_data(i, a, c)
        data_visualisation.append_data_histograms(i, w, b)
        data_visualisation.update_image1(im)
        print(str(i) + ": accuracy:" + str(a) + " loss: " + str(c))

    # compute test values for visualisation
    if update_test_data:
        a, c, im = sess.run([accuracy, cross_entropy, It],
                            feed_dict={input: mnist.test.images, correct_answers: mnist.test.labels})
        data_visualisation.append_test_curves_data(i, a, c)
        data_visualisation.update_image2(im)
        print(str(i) + ": ********* epoch " + str(
            i * 100 // mnist.train.images.shape[0] + 1) + " ********* test accuracy:" + str(a) + " test loss: " + str(
            c))

    # the backpropagation training step
    sess.run(train_step, feed_dict={input: batch_X, correct_answers: batch_Y})


data_visualisation.animate(training_step, iterations=2000 + 1, train_data_update_freq=10, test_data_update_freq=50,
                           more_tests_at_start=True)
