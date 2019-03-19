import ast
import subprocess



from Workspace.Human_detector.detector.DetectionEvent import DetectionEvent
import Workspace.Human_detector.DatabaseHandler.detectionDatabaseHandler as databaseHandler

class DetectionReviewerWindowModel:
    def __int__(self):
        self.test = None
        
    @staticmethod
    def open_file_in_explorer(file_path):
        subprocess.check_call(['nautilus', '--', file_path])

    @staticmethod
    def get_detections_from_database():
        keys, detections = databaseHandler.select_all_detections()
        array_of_detection_events = []
        for x in detections:
            array_of_detection_events.append(
                DetectionEvent(ast.literal_eval(x[keys[1]]), x[keys[2]], x[keys[3]],
                               x[keys[4]], x[keys[5]],
                               x[keys[6]], x[keys[0]]))
        return array_of_detection_events
