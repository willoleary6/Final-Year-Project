cd C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionAPI_Prototype/models/research
set PYTHONPATH=C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionAPI_Prototype/models/research;C:/SourceCode/Final-Year-Project/Prototypes/TensorFlowObjectDetectionAPI_Prototype/models/research/slim
python setup.py build
python setup.py install
python object_detection/builders/model_builder_test.py