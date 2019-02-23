#!/usr/bin/env bash
cd /home/$USER/shell-test
#checking if tensorflow folder already exists
if [ ! -d "TensorFlowObjectDetectionAPI" ]; then
  mkdir TensorFlowObjectDetectionAPI
fi

cd TensorFlowObjectDetectionAPI

if [ ! -d "cocoapi" ]; then
    git clone https://github.com/cocodataset/cocoapi.git
fi

if [ ! -d "models" ]; then
   git clone https://github.com/tensorflow/models.git
fi


if [ ! -d "models/research/pycocotools" ]; then
   cp -i -r cocoapi/PythonAPI/pycocotools models/research/pycocotools

fi
cd models/research/
wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
unzip protobuf.zip

./bin/protoc object_detection/protos/*.proto --python_out=.


export PYTHONPATH=$PYTHONPATH:/home/will/Tensorflow_Object_Detection_API/models/research:/home/will/Tensorflow_Object_Detection_API/models/research/slim

pip install --user Cython
pip install --user contextlib2
pip install --user pillow
pip install --user lxml
pip install --user jupyter
pip install --user matplotlib

pip install tensorflow

echo "Nvidia GPU support? (Software detailed here -> https://www.tensorflow.org/install/gpu has been installed) y/n:"

read varname


if [[ $varname = "y" ]]; then
  pip install --upgrade tensorflow-gpu
fi

if [[ $varname = "Y" ]]; then
  pip install --upgrade tensorflow-gpu
fi
python object_detection/builders/model_builder_test.py