#!/usr/bin/env bash
# windows
set PYTHONPATH=C:/TensorFlowObjectDetectionAPI/models/research;C:/TensorFlowObjectDetectionAPI/models/research/slim

#Ubuntu
export PYTHONPATH=$PYTHONPATH:/home/will/Tensorflow_Object_Detection_API/models/research:/home/will/Tensorflow_Object_Detection_API/models/research/slim
#initialise training (legacy script)

#windows
python C:/TensorFlowObjectDetectionAPI/models/research/object_detection/legacy/train.py --logtostderr --train_dir=training --pipeline_config_path=training\ssd_mobilenet_v2_quantized_300x300_coco.config

#Ubuntu
python /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/legacy/train.py --logtostderr --train_dir=training --pipeline_config_path=training/ssd_mobilenet_v2_quantized_300x300_coco.config
#resnet
python /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/legacy/train.py --logtostderr --train_dir=training_resnet --pipeline_config_path=training_resnet/faster_rcnn_inception_resnet_v2_atrous_coco.config

python /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/legacy/train.py --logtostderr --train_dir=training --pipeline_config_path=training/ssd_mobilenet_v2_coco.config

python models/research/object_detection/legacy/train.py --logtostderr --train_dir=C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\finger_test\training --pipeline_config_path=C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\finger_test\\training\ssd_mobilenet_v2_quantized_300x300_coco.config



# export trained graph to a model
python export_inference_graph.py --input_type image_tensor --pipeline_config_path C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\hurley_test\\training\ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\hurley_test\\training\model.ckpt-3972 --output_directory hurley_graph
python export_inference_graph.py --input_type image_tensor --pipeline_config_path C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\finger_test\\training\ssd_mobilenet_v2_quantized_300x300_coco.config --trained_checkpoint_prefix C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\finger_test\\training\model.ckpt-10004 --output_directory finger_graph

#Ubuntu

python /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path /home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/training/ssd_mobilenet_v2_coco.config --trained_checkpoint_prefix /home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/training/model.ckpt-29664 --output_directory coin_graph
#resnet
python /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path /home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/training_resnet/faster_rcnn_inception_resnet_v2_atrous_coco.config --trained_checkpoint_prefix /home/will/SourceCode/Final-Year-Project/Workspace/Prototypes/TensorFlowObjectDetectionCoinPrototype/training_resnet/model.ckpt-15434--output_directory coin_resnet_graph


python3 /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path /home/will/Documents/training_test/training/pipleline.config --trained_checkpoint_prefix home/will/Documents/faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28/model.ckpt --output_directory /home/will/Documents/training_test/test_graph


python3 /home/will/Tensorflow_Object_Detection_API/models/research/object_detection/legacy/train.py --logtostderr --train_dir=/home/will/Documents/training_test/training/ --pipeline_config_path=/home/will/Documents/training_test/training/pipeline.config