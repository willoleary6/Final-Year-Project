from Human_detector.config import Config
from Human_detector.detector.DetectionEvent import DetectionEvent
import Human_detector.DatabaseHandler.detectionDatabaseHandler as databaseHandler


class Detector:
    def __init__(self):
        self.__detections = []
        self.__objects_detected = []

    def new_detection(self, objects_detected, filename, timestamp, number_of_objects):
        self.__objects_detected = objects_detected
        self.remove_duplicate_objects()
        # first detection always gets added
        if len(self.__detections) == 0:
            self.generate_new_event(objects_detected, filename, timestamp, number_of_objects)
        # checking if new detection can be added to the last one
        elif self.__detections[(len(self.__detections) - 1)].get_file_path() == filename and \
                (timestamp - self.__detections[(len(self.__detections) - 1)].get_end_timestamp()) \
                < +Config.SECONDS_ADDED_TO_EVENT_TIMESTAMP:
            last_detection_event = self.__detections[(len(self.__detections) - 1)]
            last_detection_event.set_end_timestamp(timestamp + Config.SECONDS_ADDED_TO_EVENT_TIMESTAMP)
            # if there is more objects on screen than in the detection object, update
            if last_detection_event.get_maximum_number_of_object_detections() < number_of_objects:
                last_detection_event.set_maximum_number_of_object_detections(number_of_objects)
            # if new objects have appeared on screen
            if last_detection_event.get_objects_detected() != objects_detected:
                for x in objects_detected:
                    if x not in last_detection_event.get_objects_detected():
                        last_detection_event.append_detected_objects(x)
            self.__detections[(len(self.__detections) - 1)] = last_detection_event
        else:
            # commit last detection to csv
            self.insert_into_database()
            self.generate_new_event(objects_detected, filename, timestamp, number_of_objects)

    def generate_new_event(self, objects_detected, filename, timestamp, number_of_objects):
        new_detection = DetectionEvent(objects_detected, filename, timestamp,
                                       timestamp + Config.SECONDS_ADDED_TO_EVENT_TIMESTAMP,
                                       number_of_objects, number_of_objects)
        self.__detections.append(new_detection)

    def insert_into_database(self):
        latest_detection = self.__detections[(len(self.__detections) - 1)]
        databaseHandler.insert_new_detection(latest_detection.get_objects_detected(), latest_detection.get_file_path(),
                                             latest_detection.get_start_timestamp(),
                                             latest_detection.get_end_timestamp(),
                                             latest_detection.get_minimum_number_of_object_detections(),
                                             latest_detection.get_maximum_number_of_object_detections())

    def flush_remaining_detections(self):
        if len(self.__detections) > 0:
            self.insert_into_database()

    def remove_duplicate_objects(self):
        array_of_non_duplicate_objects = []
        for x in self.__objects_detected:
            if x not in array_of_non_duplicate_objects:
                array_of_non_duplicate_objects.append(x)

        self.__objects_detected = array_of_non_duplicate_objects
