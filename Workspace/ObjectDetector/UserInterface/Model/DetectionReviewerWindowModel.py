import ast
import subprocess

from Workspace.ObjectDetector.detector.DetectionEvent import DetectionEvent
from Workspace.ObjectDetector.Utilities.DatabaseHandler import DetectionDatabaseHandler


class DetectionReviewerWindowModel:

    @staticmethod
    def open_file_in_explorer(file_path):
        subprocess.check_call(['nautilus', '--', file_path])

    @staticmethod
    def get_detections_from_database():
        handler = DetectionDatabaseHandler()

        keys, detections = handler.select_all_detections()
        array_of_detection_events = []
        for x in detections:
            array_of_detection_events.append(
                DetectionEvent(ast.literal_eval(x[keys[1]]), x[keys[2]], x[keys[3]],
                               x[keys[4]], x[keys[5]],
                               x[keys[6]], x[keys[0]]))
        handler.close_connection()
        return array_of_detection_events

    @staticmethod
    def delete_detection(id):
        handler = DetectionDatabaseHandler()
        handler.delete_detection(id)
