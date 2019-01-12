import numpy as np
import os
from os import walk
import six.moves.urllib as url_library

import tarfile
import tensorflow as tf

from distutils.version import StrictVersion

from matplotlib import pyplot as plt
from PIL import Image
# Here are the imports from the object detection module.
# in the interest of cleanliness and sanity ive updated the paths
# of the interpreter the IDE uses so we can call the object detection api from outside the
# the models directory, using models.research.object_detection will also not work....
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from object_detection.utils import ops as utils_operations

if StrictVersion(tf.__version__) < StrictVersion('1.9.0'):
    raise ImportError('Please upgrade your TensorFlow installation to v1.9.* or later!')

# Model preparation Variables Any model exported using the export_inference_graph.py tool can be loaded here simply
# by changing PATH_TO_FROZEN_GRAPH_OF_MODEL to point to a new .pb file.

# By default we use an "SSD with Mobilenet" model here. See the detection model zoo for a list of other models that
# can be run out-of-the-box with varying speeds and accuracies.

# change directory to that of the object detection api
os.chdir(os.getcwd() + '\models\\research\object_detection')

# What model to download.
model_name = 'ssd_mobilenet_v1_coco_2017_11_17'
model_file = model_name + '.tar.gz'
download_base = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH_OF_MODEL = model_name + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
path_to_labels = os.getcwd() + '\\data\\mscoco_label_map.pbtxt'
# Download Model

opener = url_library.request.URLopener()
opener.retrieve(
    download_base + model_file,  # url of the file we want to
    model_file  # store model in this variable
)

model_tar_file = tarfile.open(model_file)
for file in model_tar_file.getmembers():
    file_name = os.path.basename(file.name)
    if 'frozen_inference_graph.pb' in file_name:
        model_tar_file.extract(file, os.getcwd())  # extract the desired file to the current directory

# Load a (frozen) Tensorflow model into memory.

detection_graph = tf.Graph()
with detection_graph.as_default():
    object_detection_graph_definition = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH_OF_MODEL, 'rb') as file_id:
        serialized_graph = file_id.read()
        object_detection_graph_definition.ParseFromString(serialized_graph)
        tf.import_graph_def(object_detection_graph_definition, name='')

# Loading label map Label maps map indices to category names, so that when our convolution network predicts 5,
# we know that this corresponds to airplane. Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine

category_index = label_map_util.create_category_index_from_labelmap(path_to_labels, use_display_name=True)


# Helper code

def load_image_into_numpy_array(desired_image):
    (image_width, image_height) = desired_image.size
    return np.array(
        desired_image.getdata()).reshape(
        (image_height, image_width, 3)
    ).astype(np.uint8)


# get all the files in the test_images directory
path_to_images = os.getcwd() + '\\test_images'
files_in_directory = []
for (directory_path, directory_names, file_names) in walk(path_to_images):
    files_in_directory.extend(file_names)
    break

test_image_paths = []
valid_file_extension = ['.jpg', '.png']
# filter out the non image related files and build a list of file paths to each of the images
for i in files_in_directory:
    for j in valid_file_extension:
        if i.endswith(j):
            test_image_paths.append(os.path.join(path_to_images,i))
            break

# Detection

# Size, in inches, of the output images.
image_size = (12, 8)


def run_inference_for_single_image(image, graph):
    with graph.as_default():
        with tf.Session() as sess:
            # Get handles to input and output tensors
            ops = tf.get_default_graph().get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            tensor_dict = {}
            for key in [
                'num_detections', 'detection_boxes', 'detection_scores',
                'detection_classes', 'detection_masks'
            ]:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
                        tensor_name)
            if 'detection_masks' in tensor_dict:
                # The following processing is only for single image
                detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
                detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
                # Reframe is required to translate mask from box coordinates to image coordinates and fit the image
                # size.
                real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
                detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
                detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
                detection_masks_reframed = utils_operations.reframe_box_masks_to_image_masks(
                    detection_masks, detection_boxes, image.shape[0], image.shape[1])
                detection_masks_reframed = tf.cast(
                    tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                # Follow the convention by adding back the batch dimension
                tensor_dict['detection_masks'] = tf.expand_dims(
                    detection_masks_reframed, 0)
            image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

            # Run inference
            output_dict = sess.run(tensor_dict,
                                   feed_dict={image_tensor: np.expand_dims(image, 0)})
            # all outputs are float32 numpy arrays, so convert types as appropriate
            output_dict['num_detections'] = int(output_dict['num_detections'][0])
            output_dict['detection_classes'] = output_dict[
                'detection_classes'][0].astype(np.uint8)
            output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
            output_dict['detection_scores'] = output_dict['detection_scores'][0]
            if 'detection_masks' in output_dict:
                output_dict['detection_masks'] = output_dict['detection_masks'][0]
    return output_dict


plt.switch_backend('TKAgg')
for image_path in test_image_paths:
    image = Image.open(image_path)
    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.
    image_np = load_image_into_numpy_array(image)
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    # Actual detection.
    output_dict = run_inference_for_single_image(image_np, detection_graph)
    # Visualization of the results of a detection.
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        output_dict['detection_boxes'],
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        instance_masks=output_dict.get('detection_masks'),
        use_normalized_coordinates=True,
        line_thickness=8)

    plt.gcf().clear()
    plt.imshow(image_np)
    #plt.show()
