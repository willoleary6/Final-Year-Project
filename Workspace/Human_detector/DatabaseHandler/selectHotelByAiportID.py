import Workspace.Human_detector.DatabaseHandler.detectionDatabaseHandler as databaseHandler

#print(databaseHandler.select_all_detections())
objects_detected = ['Ten Cent', 'Five Cent']
file_path = "test"
start_timestamp = 0.0
end_timestamp = 0.0
minimum_number_of_detections = 1
maximum_number_of_detections = 4
print(databaseHandler.insert_new_detection(objects_detected, file_path, start_timestamp, end_timestamp, minimum_number_of_detections,
                         maximum_number_of_detections))
