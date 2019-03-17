import ast
import subprocess

from PyQt5.QtWidgets import QFileDialog

from Human_detector.detector.DetectionEvent import DetectionEvent
import Human_detector.DatabaseHandler.detectionDatabaseHandler as databaseHandler

class DetectionReviewerWindowModel:

    def open_file_in_explorer(self, file_path):
        self
        subprocess.Popen(r'explorer /select,"' + file_path + '"')

    def get_detections_from_database(self):
        keys, detections = databaseHandler.select_all_detections()
        array_of_detection_events = []
        for x in detections:
            array_of_detection_events.append(
                DetectionEvent(ast.literal_eval(x[keys[1]]), x[keys[2]], x[keys[3]],
                               x[keys[4]], x[keys[5]],
                               x[keys[6]], x[keys[0]]))
        return array_of_detection_events
