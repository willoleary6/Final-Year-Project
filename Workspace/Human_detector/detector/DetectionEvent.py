import time

from Human_detector.config import Config


class DetectionEvent:
    def __init__(self, file_path, start_timestamp, end_timestamp,
                 minimum_number_of_object_detections, maximum_number_of_object_detections, detection_id=time.time()):
        self.__id = detection_id
        self.__file_path = file_path
        self.__start_timestamp = start_timestamp
        self.__end_timestamp = end_timestamp
        self.__minimum_number_of_object_detections = minimum_number_of_object_detections
        self.__maximum_number_of_object_detections = maximum_number_of_object_detections
        self.__csv_column_names = Config.DETECTION_CSV_COLUMNS

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

    def get_id(self):
        return self.__id

    def get_csv_column_names(self):
        return self.__csv_column_names

    def stringify(self):
        return str(self.__id) + "," + str(self.__file_path) + "," + str(self.__start_timestamp) + "," + \
               str(self.__end_timestamp) + "," + str(self.__minimum_number_of_object_detections) + \
               "," + str(self.__maximum_number_of_object_detections)
