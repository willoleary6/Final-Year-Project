# encoding: UTF-8
# Copyright 2016 Google.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
Mostly reworked this file to work better and more readable
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as matplotlib_animation
from matplotlib import rcParams
import math


# number of percentile slices for histogram visualisations
HISTOGRAM_BUCKETS = 7


# n = HISTOGRAM_BUCKETS (global)
# Buckets the data into n buckets so that there are an equal number of data points in
# each bucket. Returns n+1 bucket boundaries. Spreads the remainder data.size % n more
# or less evenly among the central buckets.
# data: 1-D ndarray containing float data, MUST BE SORTED in ascending order
#    n: integer, the number of desired output buckets
# return value: ndarray, 1-D vector of size n+1 containing the bucket boundaries
#               the first value is the min of the data, the last value is the max
def probability_distribution(data):
    n = HISTOGRAM_BUCKETS
    data.sort()
    bucket_size = data.size // n
    bucket_remainder = data.size % n
    buckets = np.zeros([n + 1])
    buckets[0] = data[0]  # min
    buckets[-1] = data[-1]  # max
    bucket_n = 0
    remainder = 0
    remainder_n = 0
    k = 0
    count = 0  # only for assert
    last_value = data[0]
    for i in range(data.size):
        value = data[i]
        bucket_n += 1
        count += 1
        # crossing bucket boundary
        if bucket_n > bucket_size + remainder:
            count -= 1
            k += 1
            buckets[k] = (value + last_value) / 2
            if k < n + 1:
                count += 1
            # value goes into the new bucket
            bucket_n = 1
            if k >= (n - bucket_remainder) // 2 and remainder_n < bucket_remainder:
                remainder = 1
                remainder_n += 1
            else:
                remainder = 0
        last_value = value
    assert i + 1 == count
    return buckets


def display_time_histogram(diagram, x_axis_data, y_axis_data, color):
    diagram.collections.clear()
    histogram_length = HISTOGRAM_BUCKETS // 2
    histogram_width = HISTOGRAM_BUCKETS // 2
    for i in range(int(math.ceil(HISTOGRAM_BUCKETS / 2.0))):
        diagram.fill_between(x_axis_data, y_axis_data[:, histogram_length - i], y_axis_data[:, histogram_width + 1 + i],
                             facecolor=color, alpha=1.6 / HISTOGRAM_BUCKETS)
        if HISTOGRAM_BUCKETS % 2 == 0 and i == 0:
            diagram.fill_between(x_axis_data, y_axis_data[:, histogram_length - 1], y_axis_data[:, histogram_width],
                                 facecolor=color, alpha=1.6 / HISTOGRAM_BUCKETS)
            histogram_length = histogram_length - 1


#  retrieve the color from the color cycle, default is 1
def get_histogram_cycle_color(color_number):
    color_list = rcParams['axes.prop_cycle']
    color_count = 1 if (color_number is None) else color_number
    colors = color_list.by_key()['color']
    for i, c in enumerate(colors):
        if i == color_count % 3:
            return c


def set_title(diagram, title, default=""):
    if title is not None and title != "":
        diagram.set_title(title, y=1.02)  # adjustment for plot title bottom margin
    else:
        diagram.set_title(default, y=1.02)  # adjustment for plot title bottom margin


class DataVisualisation:
    max_iteration = 0
    max_test_accuracy = 0
    training_iteration = []
    training_accuracy = []
    training_loss = []
    test_iteration = []
    test_accuracy = []
    test_loss = []
    list_of_iterations = []
    list_of_distribution_of_weights = np.zeros([0, HISTOGRAM_BUCKETS + 1])
    list_of_distribution_of_biases = np.zeros([0, HISTOGRAM_BUCKETS + 1])
    animation_pause = False
    animation = None
    data_visualisation_window = None
    data_visualisation_initialisation_function = None
    data_visualisation_update_function = None
    color_3 = None
    color_4 = None
    data_visualisation_window = None

    def diagram_initialisation(self, slot, x_label, y_label, title, default_title):
        diagram = self.data_visualisation_window.add_subplot(slot)
        diagram.set_xlabel(x_label)
        diagram.set_ylabel(y_label)
        set_title(diagram, title, default=default_title)
        return diagram

    def __init__(self, window_title, title_1=None, title_2=None, title_3=None, title_4=None,
                 histogram_3_color=None, histogram_4_color=None, dpi=70):
        self.color_3 = get_histogram_cycle_color(histogram_3_color)
        self.color_4 = get_histogram_cycle_color(histogram_4_color)
        # establishing the data_visualisation_window with dimensions and color
        self.data_visualisation_window = plt.figure(figsize=(25, 15), dpi=dpi)
        # base color
        self.data_visualisation_window.set_facecolor('#FFFFFF')
        # setting data_visualisation_window title
        plt.gcf().canvas.set_window_title(window_title)
        # setting the slots for each of the diagrams
        top_left_slot = 221
        top_right_slot = 222
        bottom_left_slot = 223
        bottom_center_slot = 224

        # Initialise the 4 diagrams
        diagram_1 = self.diagram_initialisation(top_left_slot, 'Iterations', 'Accuracy', title_1, "Accuracy")
        diagram_2 = self.diagram_initialisation(top_right_slot, 'Iterations', 'Loss', title_2, "Cross entropy loss")
        diagram_3 = self.diagram_initialisation(bottom_left_slot, 'Iterations', 'Distribution', title_3, "Weights")
        diagram_4 = self.diagram_initialisation(bottom_center_slot, 'Iterations', 'Distribution', title_4, "Biases")

        training_accuracy_line, = diagram_1.plot(self.training_iteration, self.training_accuracy,
                                                 label="training accuracy")
        test_accuracy_line, = diagram_1.plot(self.test_iteration, self.test_accuracy, label="test accuracy")
        legend = diagram_1.legend(loc='lower right')  # fancybox : slightly rounded corners
        legend.draggable(True)

        training_loss_line, = diagram_2.plot(self.training_iteration, self.training_loss, label="training loss")
        test_loss_line, = diagram_2.plot(self.test_iteration, self.test_loss, label="test loss")
        legend = diagram_2.legend(loc='upper right')  # fancybox : slightly rounded corners
        legend.draggable(True)

        def initialise():
            diagram_1.set_xlim(0, 10)  # initial value only, auto scaled after that
            diagram_2.set_xlim(0, 10)  # initial value only, auto scaled after that
            diagram_3.set_xlim(0, 10)  # initial value only, auto scaled after that
            diagram_4.set_xlim(0, 10)  # initial value only, auto scaled after that
            # Setting y axis limit for accuracy and loss charts
            diagram_1.set_ylim(0, 1)  # important: not auto scaled
            diagram_2.set_ylim(0, 100)  # important: not auto scaled
            return training_accuracy_line, test_accuracy_line, training_loss_line, test_loss_line

        def update():
            # x scale: training_iteration
            diagram_1.set_xlim(0, self.max_iteration + 1)
            diagram_2.set_xlim(0, self.max_iteration + 1)
            diagram_3.set_xlim(0, self.max_iteration + 1)
            diagram_4.set_xlim(0, self.max_iteration + 1)

            # four curves: train and test accuracy, train and test loss
            training_accuracy_line.set_data(self.training_iteration, self.training_accuracy)
            test_accuracy_line.set_data(self.test_iteration, self.test_accuracy)

            training_loss_line.set_data(self.training_iteration, self.training_loss)
            test_loss_line.set_data(self.test_iteration, self.test_loss)

            # histograms
            display_time_histogram(diagram_3, self.list_of_iterations, self.list_of_distribution_of_weights,
                                   self.color_3)
            display_time_histogram(diagram_4, self.list_of_iterations, self.list_of_distribution_of_biases,
                                   self.color_4)

            # return changed artists
            return training_accuracy_line, test_accuracy_line, training_loss_line, test_loss_line

        self.data_visualisation_initialisation_function = initialise
        self.data_visualisation_update_function = update

    def set_max_iteration(self, iteration):
        if iteration > self.max_iteration:
            self.max_iteration = iteration

    def get_max_test_accuracy(self):
        return self.max_test_accuracy

    def set_max_test_accuracy(self, test_accuracy):
        if test_accuracy > self.max_test_accuracy:
            self.max_test_accuracy = test_accuracy

    def append_training_curves_data(self, iteration, accuracy, loss):
        self.training_iteration.append(iteration)
        self.training_accuracy.append(accuracy)
        self.training_loss.append(loss)
        self.set_max_iteration(iteration)

    def append_test_curves_data(self, iteration, accuracy, loss):
        self.test_iteration.append(iteration)
        self.test_accuracy.append(accuracy)
        self.test_loss.append(loss)
        self.set_max_iteration(iteration)
        self.set_max_test_accuracy(accuracy)

    def append_data_histograms(self, iteration, data_vector_1, data_vector_2):
        self.list_of_iterations.append(iteration)
        data_vector_1.sort()
        self.list_of_distribution_of_weights = np.concatenate((self.list_of_distribution_of_weights,
                                                               np.expand_dims(probability_distribution(data_vector_1),
                                                                              0)))
        data_vector_2.sort()
        self.list_of_distribution_of_biases = np.concatenate((self.list_of_distribution_of_biases,
                                                              np.expand_dims(probability_distribution(data_vector_2),
                                                                             0)))
        self.set_max_iteration(iteration)

    def is_paused(self):
        return self.animation_pause

    def animate(self, compute_step, iterations, train_data_update_frequency=20, test_data_update_freq=100,
                one_test_at_start=True, more_tests_at_start=False):

        def animate_step(i):
            if i == iterations // train_data_update_frequency:  # last iteration
                compute_step(iterations, True, True)
            else:
                for k in range(train_data_update_frequency):
                    n = i * train_data_update_frequency + k
                    request_data_update = (n % train_data_update_frequency == 0)
                    request_test_data_update = (n % test_data_update_freq == 0) and (n > 0 or one_test_at_start)
                    if more_tests_at_start and n < test_data_update_freq:
                        request_test_data_update = request_data_update

                    compute_step(n, request_test_data_update, request_data_update)
                    # makes the UI a little more responsive
                    plt.pause(0.001)
            if not self.is_paused():
                return self.data_visualisation_update_function()

        self.animation = matplotlib_animation.FuncAnimation(self.data_visualisation_window, animate_step,
                                                            int(iterations // train_data_update_frequency + 1),
                                                            init_func=self.data_visualisation_initialisation_function,
                                                            interval=16,
                                                            repeat=False,
                                                            blit=False
                                                            )
        plt.show(block=True)
