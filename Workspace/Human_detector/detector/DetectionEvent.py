from Human_detector.detector.config import Config

class DetectionEvent:
    def __init__(self, file_path, timestamp, objects_detected):
        self.__file_path = file_path
        self.__start_timestamp = timestamp
        self.__end_timestamp = timestamp+Config.SECONDS_ADDED_TO_EVENT_TIMESTAMP
        self.__minimum_number_of_object_detections = objects_detected
        self.__maximum_number_of_object_detections = objects_detected

    def set_minimum_number_of_object_detections(self, new_minimum):
        self.__minimum_number_of_object_detections = new_minimum

    def set_maximum_number_of_object_detections(self, new_maximum):
        self.__maximum_number_of_object_detections = new_maximum

    def get_maximum_number_of_object_detections(self):
        return self.__maximum_number_of_object_detections

    def get_file_path(self):
        return self.__file_path

    def get_start_timestamp(self):
        return self.__start_timestamp

    def get_end_timestamp(self):
        return self.__end_timestamp

    def set_end_timestamp(self, new_end_timestamp):
        self.__end_timestamp = new_end_timestamp

    def stringify(self):
        return str(self.__file_path)+","+str(self.__start_timestamp)+","+str(self.__end_timestamp)+","+\
               str(self.__minimum_number_of_object_detections)+","+str(self.__maximum_number_of_object_detections)
