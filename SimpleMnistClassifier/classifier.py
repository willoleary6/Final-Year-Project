import os
import tensorflow as tf

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from mnist_data import read_data_sets_into_memory

print("Version "+tf.__version__)
tf.set_random_seed(0)

mnist = read_data_sets_into_memory("data")