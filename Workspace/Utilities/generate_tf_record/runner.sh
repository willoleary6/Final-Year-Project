#!/usr/bin/env bash
# run from C:/Program Files/TensorFlow Object Detection API/models
# finger prototype commands
python generate_tfrecord.py --output_path=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/train.record --csv_input=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/train_labels.csv --image_dir=C:/SourceCode/Final-Year-Project/Images/prototype_images/fingers/train
python generate_tfrecord.py --output_path=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/test.record --csv_input=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/test_labels.csv --image_dir=C:/SourceCode/Final-Year-Project/Images/prototype_images/fingers/test


python generate_tfrecord.py --output_path=/home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/data/test.record --csv_input=/home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/data/test_labels.csv --image_dir=/home/will/SourceCode/Final-Year-Project/Images/prototype_images/coins/test
python generate_tfrecord.py --output_path=/home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/data/train.record --csv_input=/home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/data/train_labels.csv --image_dir=/home/will/SourceCode/Final-Year-Project/Images/prototype_images/coins/train
sleep 10