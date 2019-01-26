#!/usr/bin/env bash
# run from C:/Program Files/TensorFlow Object Detection API/models
set PYTHONPATH=C:\TensorFlowObjectDetectionAPI\models\research;C:\TensorFlowObjectDetectionAPI\models\research\slim
python generate_tfrecord.py --output_path=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/train.record --csv_input=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionFingerPrototype/data/train_labels.csv --image_dir=C:/SourceCode/Final-Year-Project/Images/prototype_images/fingers/train
sleep 10