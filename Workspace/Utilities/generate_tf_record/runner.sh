#!/usr/bin/env bash
# run from C:/Program Files/TensorFlow Object Detection API/models
# finger prototype commands
python generate_tfrecord.py --output_path=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/train.record --csv_input=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/train_labels.csv --image_dir=C:/SourceCode/Final-Year-Project/Images/prototype_images/fingers/train
python generate_tfrecord.py --output_path=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/test.record --csv_input=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/test_labels.csv --image_dir=C:/SourceCode/Final-Year-Project/Images/prototype_images/fingers/test

sleep 10