@echo off
rem Changing directory to program files
CD C:/

rem checking if TensorFlow Object Detection API directory is already created
IF NOT EXIST "TensorFlowObjectDetectionAPI" (
    mkdir "TensorFlowObjectDetection API"
)



rem falling into TensorFlow Object Detection API
CD "TensorFlowObjectDetectionAPI"

rem if they already exist then there is no point in cloning again
IF NOT EXIST "cocoapi" (
    git clone https://github.com/cocodataset/cocoapi.git
)

IF NOT EXIST "models" (
    git clone https://github.com/tensorflow/models.git
)

IF NOT EXIST "models/research/pycocotools" (
    ROBOCOPY  "cocoapi/PythonAPI/pycocotools" "models/research/pycocotools" /mir
)

set /p id="Please ensure that protobuf has been added to the environmental path before hitting enter"


CD "models\research"
rem converting the proto files into .py files
protoc.exe --python_out=. "./object_detection/protos/anchor_generator.proto"
protoc.exe --python_out=. "./object_detection/protos/argmax_matcher.proto"
protoc.exe --python_out=. "./object_detection/protos/bipartite_matcher.proto"
protoc.exe --python_out=. "./object_detection/protos/box_coder.proto"
protoc.exe --python_out=. "./object_detection/protos/box_predictor.proto"
protoc.exe --python_out=. "./object_detection/protos/eval.proto"
protoc.exe --python_out=. "./object_detection/protos/faster_rcnn.proto"
protoc.exe --python_out=. "./object_detection/protos/faster_rcnn_box_coder.proto"
protoc.exe --python_out=. "./object_detection/protos/grid_anchor_generator.proto"
protoc.exe --python_out=. "./object_detection/protos/hyperparams.proto"
protoc.exe --python_out=. "./object_detection/protos/image_resizer.proto"
protoc.exe --python_out=. "./object_detection/protos/input_reader.proto"
protoc.exe --python_out=. "./object_detection/protos/losses.proto"
protoc.exe --python_out=. "./object_detection/protos/matcher.proto"
protoc.exe --python_out=. "./object_detection/protos/mean_stddev_box_coder.proto"
protoc.exe --python_out=. "./object_detection/protos/model.proto"
protoc.exe --python_out=. "./object_detection/protos/optimizer.proto"
protoc.exe --python_out=. "./object_detection/protos/pipeline.proto"
protoc.exe --python_out=. "./object_detection/protos/post_processing.proto"
protoc.exe --python_out=. "./object_detection/protos/preprocessor.proto"
protoc.exe --python_out=. "./object_detection/protos/region_similarity_calculator.proto"
protoc.exe --python_out=. "./object_detection/protos/square_box_coder.proto"
protoc.exe --python_out=. "./object_detection/protos/ssd.proto"
protoc.exe --python_out=. "./object_detection/protos/ssd_anchor_generator.proto"
protoc.exe --python_out=. "./object_detection/protos/string_int_label_map.proto"
protoc.exe --python_out=. "./object_detection/protos/train.proto"
protoc.exe --python_out=. "./object_detection/protos/keypoint_box_coder.proto"
protoc.exe --python_out=. "./object_detection/protos/multiscale_anchor_generator.proto"
protoc.exe --python_out=. "./object_detection/protos/graph_rewriter.proto"


rem python dependecies needed
pip install  Cython
pip install  contextlib2
pip install  pillow
pip install  lxml
pip install  jupyter
pip install  matplotlib

pip install tensorflow

set /p id="Nvidia GPU support? (Software detailed here -> https://www.tensorflow.org/install/gpu has been installed) y/n:  "

IF "%id%"=="y" (
  pip install --upgrade tensorflow-gpu
)

python setup.py build
python setup.py install


set PYTHONPATH=%PYTHONPATH%;C:\Program Files\TensorFlow Object Detection API\models\research;C:\Program Files\TensorFlow Object Detection API\models\research\slim
python object_detection/builders/model_builder_test.py

ECHO installation complete, please add the research and research/slim directory to the enviromental variable path before running the API
ECHO set PYTHONPATH=C:\TensorFlowObjectDetectionAPI\models\research;C:\TensorFlowObjectDetectionAPI\models\research\slim