from Human_detector.config import Config


class DetectionEvent:
    def __init__(self, objects_detected, file_path, start_timestamp,
                 end_timestamp, minimum_number_of_detections, maximum_number_of_detections, auto_id=None):
        self.__id = auto_id
        self.__objects_detected = objects_detected
        self.__file_path = file_path
        self.__start_timestamp = start_timestamp
        self.__end_timestamp = end_timestamp
        self.__minimum_number_of_object_detections = minimum_number_of_detections
        self.__maximum_number_of_object_detections = maximum_number_of_detections

    def set_minimum_number_of_object_detections(self, new_minimum):
        self.__minimum_number_of_object_detections = new_minimum

    def set_maximum_number_of_object_detections(self, new_maximum):
        self.__maximum_number_of_object_detections = new_maximum

    def get_maximum_number_of_object_detections(self):
        return self.__maximum_number_of_object_detections

    def get_minimum_number_of_object_detections(self):
        return self.__minimum_number_of_object_detections

    def get_file_path(self):
        return self.__file_path

    def get_start_timestamp(self):
        return self.__start_timestamp

    def get_objects_detected(self):
        return self.__objects_detected

    def append_detected_objects(self, new_object_detections):
        return self.__objects_detected.append(new_object_detections)

    def get_end_timestamp(self):
        return self.__end_timestamp

    def set_end_timestamp(self, new_end_timestamp):
        self.__end_timestamp = new_end_timestamp

    def get_id(self):
        return self.__id
