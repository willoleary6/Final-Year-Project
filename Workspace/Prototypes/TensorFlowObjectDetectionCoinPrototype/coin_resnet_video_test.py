import cv2
import numpy as np
import os
from os import walk
import re
import tensorflow as tf


from distutils.version import StrictVersion

# Here are the imports from the object detection module.
# in the interest of cleanliness and sanity ive updated the paths
# of the interpreter the IDE uses so we can call the object detection api from outside the
# the models directory, using models.research.object_detection will also not work....
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# get all the files in the test_images directory
path_to_images = 'test_videos'
files_in_directory = []
for (directory_path, directory_names, file_names) in walk(path_to_images):
    files_in_directory.extend(file_names)
    break

test_video_paths = []
valid_file_extension = ['.mp4']
# filter out the non image related files and build a list of file paths to each of the images
for i in files_in_directory:
    for j in valid_file_extension:
        if i.endswith(j):
            test_video_paths.append(os.path.join(path_to_images, i))
            break

cap = cv2.VideoCapture(test_video_paths[0])

if StrictVersion(tf.__version__) < StrictVersion('1.9.0'):
    raise ImportError('Please upgrade your TensorFlow installation to v1.9.* or later!')

# Model preparation Variables Any model exported using the export_inference_graph.py tool can be loaded here simply
# by changing PATH_TO_FROZEN_GRAPH_OF_MODEL to point to a new .pb file.

# By default we use an "SSD with Mobilenet" model here. See the detection model zoo for a list of other models that
# can be run out-of-the-box with varying speeds and accuracies.

# change directory to that of the object detection api
# os.chdir(os.getcwd() + '\models\\research\object_detection')

# What model to download.
model_name = 'coin_resnet_graph'
# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH_OF_MODEL = model_name + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.

path_to_labels = 'training_resnet/object_detection.pbtxt'
#path_to_labels = 'training_resnet/object_detection.pbtxt'



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


def value_on_screen(objects):
    values = []
    for object in objects:
        values.append((re.findall('\'([^\']*)\'', str(object)))[0])
    numeric_value = 0.00
    for single_value in values:
        if single_value == 'Five Cent':
            numeric_value = numeric_value + 0.05
        elif single_value == 'Ten Cent':
            numeric_value = numeric_value + 0.10
        elif single_value == 'Twenty Cent':
            numeric_value = numeric_value + 0.20
        elif single_value == 'Fifty Cent':
            numeric_value = numeric_value + 0.50
        elif single_value == 'One Euro':
            numeric_value = numeric_value + 1.00
        elif single_value == 'Two Euro':
            numeric_value = numeric_value + 2.00
    return round(numeric_value, 2)


# Size, in inches, of the output images.
image_size = (24, 16)
frame_number = 0
# Detection
with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        while True:
            frame_number = frame_number + 1
            # Read frame from camera
            ret, image_np = cap.read()
            if frame_number % 5 == 0:

                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Extract image tensor
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                # Extract detection boxes
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                # Extract detection scores
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                # Extract detection classes
                classes = detection_graph.get_tensor_by_name('detection_classes:0')

                # Extract number of detectionsd
                num_detections = detection_graph.get_tensor_by_name(
                    'num_detections:0')
                # Actual detection.
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.

                vis_util.visualize_boxes_and_labels_on_image_array(
                    image_np,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=8)

                objects = []
                threshold = 0.5  # in order to get higher percentages you need to lower this number; usually at 0.01 you get 100% predicted objects
                for index, value in enumerate(classes[0]):
                    object_dict = {}
                    if scores[0, index] > threshold:
                        object_dict[(category_index.get(value)).get('name').encode('utf8')] = \
                            scores[0, index]
                        objects.append(object_dict)
                value = value_on_screen(objects)
                # Display output
                message = 'Euros on screen: ' + str(value)
                cv2.putText(image_np, message, (1100, 1000), cv2.FONT_ITALIC, 1.5, (255, 255, 255), 3, cv2.LINE_AA)
                cv2.imshow('object detection', cv2.resize(image_np, (1920, 1080)))

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
