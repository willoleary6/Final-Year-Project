import tensorflow as tf
import numpy as np
from trainer.tasks import load_mnist_data
from trainer.tasks import load_and_inter_leaf_data_set_with_labels


def read_data_sets_into_memory(data_set_file_path):
    train_images_file, train_labels_file, test_images_file, test_labels_file = load_mnist_data(data_set_file_path)
    train_dataset = load_and_inter_leaf_data_set_with_labels(train_images_file, train_labels_file)
    print("complete")