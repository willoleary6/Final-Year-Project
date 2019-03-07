from Human_detector.detector.CsvWriter import CsvWriter
from Human_detector.detector.config import Config
from Human_detector.detector.DetectionEvent import DetectionEvent


class Detector:
    def __init__(self):
        self.__detections = []

    def new_detection(self, filename, timestamp, number_of_objects):
        if len(self.__detections) == 0:
            self.generate_new_event(filename, timestamp, number_of_objects)
        elif self.__detections[(len(self.__detections) - 1)].get_file_path() == filename and \
                (timestamp - self.__detections[(len(self.__detections) - 1)].get_end_timestamp()) \
                < +Config.SECONDS_ADDED_TO_EVENT_TIMESTAMP:
            last_detection_event = self.__detections[(len(self.__detections) - 1)]
            last_detection_event.set_end_timestamp(timestamp + Config.SECONDS_ADDED_TO_EVENT_TIMESTAMP)
            if last_detection_event.get_maximum_number_of_object_detections() < number_of_objects:
                last_detection_event.set_maximum_number_of_object_detections(number_of_objects)
            self.__detections[(len(self.__detections) - 1)] = last_detection_event
        else:
            # commit last detection to csv
            self.write_to_csv()
            self.generate_new_event(filename, timestamp, number_of_objects)

    def generate_new_event(self, filename, timestamp, number_of_objects):
        new_detection = DetectionEvent(filename, timestamp, number_of_objects)
        self.__detections.append(new_detection)

    def write_to_csv(self):
        test = CsvWriter(
            Config.DETECTION_CSV_FILE_PATH,
            self.__detections[(len(self.__detections) - 1)].get_csv_column_names())
        test.write_to_csv(self.__detections[(len(self.__detections) - 1)].stringify())

    def flush_remaining_detections(self):
        if len(self.__detections) > 0:
            self.write_to_csv()

    def stringify_detection_events(self):
        for x in self.__detections:
            print(x.stringify())
