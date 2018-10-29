import tensorflow as tf
import tensorflowvisu_digits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.animation as animation
import math

# number of percentile slices for histogram visualisations
HISTOGRAM_BUCKETS = 7


# input: tensor of shape [100+, 28, 28, 1] containing a batch of images (float32)
# model: tensor of shape [100+, 10] containing recognised digits (one-hot vectors)
# correct_answers: tensor of shape [100+, 10] containing correct digit labels (one-hot vectors)
# return value: tensor of shape [280, 280, 3] containing the 100 first unrecognised images (rgb, uint8)
# followed by other, recognised images. 100 images max arranged as a 10x10 array. Unrecognised images
# are displayed on a red background and labeled with the correct (left) and recognised digit (right.

def tf_format_mnist_images(input, model, correct_answers, n=100, lines=10):
    correct_prediction = tf.equal(tf.argmax(model, 1), tf.argmax(correct_answers, 1))
    # index of correctly recognised digits
    correctly_recognised_indices = tf.squeeze(tf.where(correct_prediction), [1])

    # index of incorrectly recognised digits
    incorrectly_recognised_indices = tf.squeeze(tf.where(tf.logical_not(correct_prediction)), [1])

    # images reordered with indices of unrecognised images first
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
                                                                                   tf.int32))
    # pick either the red or the white background depending on recognised status

    I = tf.image.grayscale_to_rgb(computed_inputs)
    # stencil extra data on top of images and reorder
    I = ((1 - (I + superimposed_digits)) * recognised_bkg) / 1.3
    # them unrecognised first
    I = tf.image.convert_image_dtype(I, tf.uint8, saturate=True)
    Islices = []  # 100 images => 10x10 image block
    for imslice in range(lines):
        Islices.append(tf.concat(tf.unstack(tf.slice(I, [imslice * n // lines, 0, 0, 0], [n // lines, 28, 28, 3])), 1))
    I = tf.concat(Islices, 0)
    return I


class VisualiseMnistDataSet:
    x_maximum = 0
    y_maximum = 0
    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    x3 = []
    w3 = np.zeros([0, HISTOGRAM_BUCKETS + 1])
    b3 = np.zeros([0, HISTOGRAM_BUCKETS + 1])
    im1 = np.full((28 * 10, 28 * 10, 3), 255, dtype='uint8')
    im2 = np.full((28 * 10, 28 * 10, 3), 255, dtype='uint8')
    _animpause = False
    _animation = None
    _mpl_figure = None
    _mlp_init_func = None
    _mpl_update_func = None
    _color4 = None
    _color5 = None

    def __init__(self, axis_title_1 = None, axis_title_2=None, axis_title_3=None,
                axis_title_4=None, axis_title_5=None, axis_title_6=None, histogram_1_color_num=None,
                histogram_2_color_num=None, dpi=70):
        self._color4 = self.__get_histogram_cycle_color(histogram_1_color_num)
        self._color5 = self.__get_histogram_cycle_color(histogram_2_color_num)
        fig = plt.figure(figsize=(19.20, 10.80), dpi=dpi)
        plt.gcf().canvas.set_window_title("MNIST")

        ax1 = fig.add_subplot(231)
        ax2 = fig.add_subplot(232)
        ax3 = fig.add_subplot(233)
        ax4 = fig.add_subplot(234)
        ax5 = fig.add_subplot(235)
        ax6 = fig.add_subplot(236)
        
        # fig, ax = plt.subplots() # if you need only 1 graph

        self.__set_title(ax1, axis_title_1, default="Accuracy")
        self.__set_title(ax2, axis_title_2, default="Cross entropy loss")
        self.__set_title(ax3, axis_title_3, default="Training digits")
        self.__set_title(ax4, axis_title_4, default="Weights")
        self.__set_title(ax5, axis_title_5, default="Biases")
        self.__set_title(ax6, axis_title_6, default="Test digits")

        line1, = ax1.plot(self.x1, self.y1, label="training accuracy")
        line2, = ax1.plot(self.x2, self.y2, label="test accuracy")
        # fancybox : slightly rounded corners
        legend = ax1.legend(loc='lower right')
        legend.draggable(True)

        line3, = ax2.plot(self.x1, self.z1, label="training loss")
        line4, = ax2.plot(self.x2, self.z2, label="test loss")
        # fancybox : slightly rounded corners
        legend = ax2.legend(loc='upper right')
        legend.draggable(True)

        ax3.grid(False)  # toggle grid off
        ax3.set_axis_off()
        imax1 = ax3.imshow(self.im1, animated=True, cmap='binary', vmin=0.0, vmax=1.0, interpolation='nearest',
                           aspect=1.0)

        ax6.grid(False)  # toggle grid off
        ax6.axes.get_xaxis().set_visible(False)
        imax2 = ax6.imshow(self.im2, animated=True, cmap='binary', vmin=0.0, vmax=1.0, interpolation='nearest',
                           aspect=1.0)
        ax6.locator_params(axis='y', nbins=7)

        # hack...
        ax6.set_yticks([0, 280 - 4 * 56, 280 - 3 * 56, 280 - 2 * 56, 280 - 56, 280])
        ax6.set_yticklabels(["100%", "98%", "96%", "94%", "92%", "90%"])

        def _key_event_handler(event):
            if len(event.key) == 0:
                return
            else:
                keycode = event.key

            # pause/resume with space bar
            if keycode == ' ':
                self._animpause = not self._animpause
                if not self._animpause:
                    _update()
                return

            # [p, m, n] p is the #of the subplot, [n,m] is the subplot layout
            toggles = {'1': [1, 1, 1],  # one plot
                       '2': [2, 1, 1],  # one plot
                       '3': [3, 1, 1],  # one plot
                       '4': [4, 1, 1],  # one plot
                       '5': [5, 1, 1],  # one plot
                       '6': [6, 1, 1],  # one plot
                       '7': [12, 1, 2],  # two plots
                       '8': [45, 1, 2],  # two plots
                       '9': [36, 1, 2],  # two plots
                       'escape': [123456, 2, 3],  # six plots
                       '0': [123456, 2, 3]}  # six plots

            # other matplotlib keyboard shortcuts:
            # 'o' box zoom
            # 'p' mouse pan and zoom
            # 'h' or 'home' reset
            # 's' save
            # 'g' toggle grid (when mouse is over a plot)
            # 'k' toggle log/lin x axis
            # 'l' toggle log/lin y axis

            if not (keycode in toggles):
                return

            for i in range(6):
                fig.axes[i].set_visible(False)

            fignum = toggles[keycode][0]
            if fignum <= 6:
                fig.axes[fignum - 1].set_visible(True)
                fig.axes[fignum - 1].change_geometry(toggles[keycode][1], toggles[keycode][2], 1)
                ax6.set_aspect(25.0 / 40)  # special case for test digits
            elif fignum < 100:
                fig.axes[fignum // 10 - 1].set_visible(True)
                fig.axes[fignum // 10 - 1].change_geometry(toggles[keycode][1], toggles[keycode][2], 1)
                fig.axes[fignum % 10 - 1].set_visible(True)
                fig.axes[fignum % 10 - 1].change_geometry(toggles[keycode][1], toggles[keycode][2], 2)
                ax6.set_aspect(1.0)  # special case for test digits
            elif fignum == 123456:
                for i in range(6):
                    fig.axes[i].set_visible(True)
                    fig.axes[i].change_geometry(toggles[keycode][1], toggles[keycode][2], i + 1)
                ax6.set_aspect(1.0)  # special case for test digits

            plt.draw()

        def _update():
            # x scale: iterations
            ax1.set_xlim(0, self.x_maximum + 1)
            ax2.set_xlim(0, self.x_maximum + 1)
            ax4.set_xlim(0, self.x_maximum + 1)
            ax5.set_xlim(0, self.x_maximum + 1)

            # four curves: train and test accuracy, train and test loss
            line1.set_data(self.x1, self.y1)
            line2.set_data(self.x2, self.y2)
            line3.set_data(self.x1, self.z1)
            line4.set_data(self.x2, self.z2)

            # images
            imax1.set_data(self.im1)
            imax2.set_data(self.im2)

            # histograms
            _display_time_histogram(ax4, self.x3, self.w3, self._color4)
            _display_time_histogram(ax5, self.x3, self.b3, self._color5)

            # return changed artists
            return imax1, imax2, line1, line2, line3, line4

        def _init():
            ax1.set_xlim(0, 10)  # initial value only, autoscaled after that
            ax2.set_xlim(0, 10)  # initial value only, autoscaled after that
            ax4.set_xlim(0, 10)  # initial value only, autoscaled after that
            ax5.set_xlim(0, 10)  # initial value only, autoscaled after that
            ax1.set_ylim(0, 1)  # important: not autoscaled
            # ax1.autoscale(axis='y')
            ax2.set_ylim(0, 100)  # important: not autoscaled
            return imax1, imax2, line1, line2, line3, line4

        fig.canvas.mpl_connect('key_press_event', _key_event_handler)

        self._mpl_figure = fig
        self._mlp_init_func = _init
        self._mpl_update_func = _update

    #  retrieve the color from the color cycle, default is 1
    def __get_histogram_cycle_color(self, color_num):
        color_list = rcParams['axes.prop_cycle']
        color_count = 1 if (color_num is None) else color_num
        colors = color_list.by_key()['color']
        for i, current_color in enumerate(colors):
            if (i == color_count % 3):
                return current_color

    def __set_title(self, ax, title, default=""):
        if title is not None and title != "":
            # adjustment for plot title bottom margin
            ax.set_title(title, y=1.02)
        else:
            # adjustment for plot title bottom margin
            ax.set_title(default, y=1.02)

    def append_training_curves_data(self, x, accuracy, loss):
        self.x1.append(x)
        self.y1.append(accuracy)
        self.z1.append(loss)
        self._update_x_maximum(x)

    def append_data_histograms(self, x, datavect1, datavect2, title1=None, title2=None):
        self.x3.append(x)
        datavect1.sort()
        self.w3 = np.concatenate((self.w3, np.expand_dims(probability_distribution(datavect1), 0)))
        datavect2.sort()
        self.b3 = np.concatenate((self.b3, np.expand_dims(probability_distribution(datavect2), 0)))
        self._update_x_maximum(x)

    def update_image1(self, im):
        self.im1 = im

    def update_image2(self, im):
        self.im2 = im

    def _update_y_maximum(self, y):
        if (y > self.y_maximum):
            self.y_maximum = y

    def _update_x_maximum(self, x):
        if (x > self.x_maximum):
            self.x_maximum = x

    def append_test_curves_data(self, x, accuracy, loss):
        self.x2.append(x)
        self.y2.append(accuracy)
        self.z2.append(loss)
        self._update_x_maximum(x)
        self._update_y_maximum(accuracy)

    def is_paused(self):
        return self._animpause

    def animate(self, compute_step, iterations, train_data_update_freq=20, test_data_update_freq=100,
                one_test_at_start=True, more_tests_at_start=False, save_movie=False):

        def animate_step(i):
            if (i == iterations // train_data_update_freq):  # last iteration
                compute_step(iterations, True, True)
            else:
                for k in range(train_data_update_freq):
                    n = i * train_data_update_freq + k
                    request_data_update = (n % train_data_update_freq == 0)
                    request_test_data_update = (n % test_data_update_freq == 0) and (n > 0 or one_test_at_start)
                    if more_tests_at_start and n < test_data_update_freq: request_test_data_update = request_data_update
                    compute_step(n, request_test_data_update, request_data_update)
                    # makes the UI a little more responsive
                    plt.pause(0.001)
            if not self.is_paused():
                return self._mpl_update_func()

        self._animation = animation.FuncAnimation(self._mpl_figure, animate_step,
                                                  int(iterations // train_data_update_freq + 1),
                                                  init_func=self._mlp_init_func, interval=16, repeat=False, blit=False)

        if save_movie:
            mywriter = animation.FFMpegWriter(fps=24, codec='libx264',
                                              extra_args=['-pix_fmt', 'yuv420p', '-profile:v', 'high', '-tune',
                                                          'animation', '-crf', '18'])
            self._animation.save("./tensorflowvisu_video.mp4", writer=mywriter)
        else:
            plt.show(block=True)

def _empty_collection(collection):
    tempcoll = []
    for a in (collection):
        tempcoll.append(a)
    for a in (tempcoll):
        collection.remove(a)

def _display_time_histogram(ax, xdata, ydata, color):
    _empty_collection(ax.collections)
    midl = HISTOGRAM_BUCKETS//2
    midh = HISTOGRAM_BUCKETS//2
    for i in range(int(math.ceil(HISTOGRAM_BUCKETS/2.0))):
        ax.fill_between(xdata, ydata[:,midl-i], ydata[:,midh+1+i], facecolor=color, alpha=1.6/HISTOGRAM_BUCKETS)
        if HISTOGRAM_BUCKETS % 2 == 0 and i == 0:
            ax.fill_between(xdata, ydata[:,midl-1], ydata[:,midh], facecolor=color, alpha=1.6/HISTOGRAM_BUCKETS)
            midl = midl-1

def probability_distribution(data):
    n = HISTOGRAM_BUCKETS
    data.sort()
    bucketsize = data.size // n
    bucketrem  = data.size % n
    buckets = np.zeros([n+1])
    buckets[0] = data[0]  # min
    buckets[-1] = data[-1]  # max
    buckn = 0
    rem = 0
    remn = 0
    k = 0
    cnt = 0 # only for assert
    lastval = data[0]
    for i in range(data.size):
        val = data[i]
        buckn += 1
        cnt += 1
        if buckn > bucketsize+rem : ## crossing bucket boundary
            cnt -= 1
            k += 1
            buckets[k] = (val + lastval) / 2
            if (k<n+1):
                cnt += 1
            buckn = 1 # val goes into the new bucket
            if k >= (n - bucketrem) // 2 and remn < bucketrem:
                rem = 1
                remn += 1
            else:
                rem = 0
        lastval = val
    assert i+1 == cnt
    return buckets