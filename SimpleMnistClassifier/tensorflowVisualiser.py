import tensorflow as tf
import tensorflowvisu_digits
import numpy as np
import matplotlib.pyplot as plt

# input: tensor of shape [100+, 28, 28, 1] containing a batch of images (float32)
# model: tensor of shape [100+, 10] containing recognised digits (one-hot vectors)
# correct_answers: tensor of shape [100+, 10] containing correct digit labels (one-hot vectors)
# return value: tensor of shape [280, 280, 3] containing the 100 first unrecognised images (rgb, uint8)
# followed by other, recognised images. 100 images max arranged as a 10x10 array. Unrecognised images
# are displayed on a red background and labeled with the correct (left) and recognised digit (right.

def tf_format_mnist_images(input, model, correct_answers, n=100, lines=10):
    print("test")
    correct_prediction = tf.equal(tf.argmax(model, 1), tf.argmax(correct_answers, 1))
    # index of correctly recognised digits
    correctly_recognised_indices = tf.squeeze(tf.where(correct_prediction), [1])

    # index of incorrectly recognised digits
    incorrectly_recognised_indices = tf.squeeze(tf.where(tf.logical_not(correct_prediction)), [1])

    # images reordered with indeces of unrecognised images first
    everything_incorrect_first = tf.concat([incorrectly_recognised_indices, correctly_recognised_indices], 0)
    everything_incorrect_first = tf.slice(everything_incorrect_first, [0], [n])

    computed_inputs = tf.gather(input, everything_incorrect_first)
    computed_model = tf.gather(model, everything_incorrect_first)
    computed_correct_answers = tf.gather(correct_answers, everything_incorrect_first)
    correct_prediction_s = tf.gather(correct_prediction, everything_incorrect_first)
    # initialise digits left with sample tensor
    digits_left = tf.image.grayscale_to_rgb(tensorflowvisu_digits.digits_left())
    # correct digits
    correct_tags = tf.gather(digits_left, tf.argmax(computed_correct_answers, 1))

    digits_right = tf.image.grayscale_to_rgb(tensorflowvisu_digits.digits_right())
    computed_tags = tf.gather(digits_right, tf.argmax(computed_model, 1))

    # superimposed_digits = correct_tags+computed_tags
    superimposed_digits = tf.where(correct_prediction_s, tf.zeros_like(correct_tags), correct_tags + computed_tags)

    correct_bkg = tf.reshape(tf.tile([1.3, 1.3, 1.3], [28 * 28]), [1, 28, 28, 3])  # white background
    incorrect_bkg = tf.reshape(tf.tile([1.3, 1.0, 1.0], [28 * 28]), [1, 28, 28, 3])  # red background
    recognised_bkg = tf.gather(tf.concat([incorrect_bkg, correct_bkg], 0), tf.cast(correct_prediction_s,
                                                                                   tf.int32))  # pick either the red
    # or the white background depending on recognised status

    I = tf.image.grayscale_to_rgb(computed_inputs)
    I = ((1 - (
                I + superimposed_digits)) * recognised_bkg) / 1.3  # stencil extra data on top of images and reorder
    # them unrecognised first
    I = tf.image.convert_image_dtype(I, tf.uint8, saturate=True)
    Islices = []  # 100 images => 10x10 image block
    for imslice in range(lines):
        Islices.append(tf.concat(tf.unstack(tf.slice(I, [imslice * n // lines, 0, 0, 0], [n // lines, 28, 28, 3])), 1))
    I = tf.concat(Islices, 0)
    return I