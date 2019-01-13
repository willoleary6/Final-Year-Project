#!/usr/bin/env bash

#initialise training (legacy script)
python models/research/object_detection/legacy/train.py --logtostderr --train_dir=C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\hurley_test\training --pipeline_conf
ig_path=C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\hurley_test\\training\ssd_mobilenet_v1_pets.config

# export trained graph to a model
python export_inference_graph.py --input_type image_tensor --pipeline_config_path C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\hurley_test\\training\ssd_mobilenet_
v1_pets.config --trained_checkpoint_prefix C:\SourceCode\Final-Year-Project\Prototypes\TensorFlowObjectDetectionAPI_Prototype\hurley_test\\training\model.ckpt-3972 --output_direct
ory hurley_graph
