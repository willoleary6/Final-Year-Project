class Config:
    SECONDS_ADDED_TO_EVENT_TIMESTAMP = .5
    DETECTION_CSV_FILE_PATH = 'C:\\SourceCode\\Final-Year-Project\\Workspace\\Workspace.ObjectDetector\\CsvFiles\\detections.csv'
    FRAME_DELIMITER_FOR_TENSORFLOW = 5
    CAMERA_IP_ADDRESS = '192.168.1.210'
    CAMERA_PORT = '554'
    CAMERA_USERNAME = 'willoleary6'
    CAMERA_PASSWORD = 'password1'
    DETECTION_CSV_COLUMNS = ['detection_id', 'video_file_path', 'start_timestamp', 'end_timestamp',
                             'minimum_detections', 'maximum_detections']
    WINDOW_TITLE_FONT_SIZE = 16
    READER_REVIEWER_WINDOW_WIDTH = 2000
    READER_REVIEWER_WINDOW_HEIGHT = 1080
    DETECTION_REVIEWER_WINDOW_WIDTH = 1080
    DETECTION_REVIEWER_WINDOW_HEIGHT = 1920
    MAIN_MENU_WINDOW_WIDTH = 720
    MAIN_MENU_WINDOW_HEIGHT = 720
    DATABASE_USERNAME = 'root'
    DATABASE_PASSWORD = ''
    DATABASE_NAME = 'object_detector'
    DATABASE_HOST = 'localhost'
    THREAD_LOOP_DELAY = .1
    VALID_VIDEO_FORMATS = ['.mp4']
    #file extensions
    INFERENCE_GRAPH_FILE_EXTENSION = '.pb'
    OBJECT_LABELS_FILE_EXTENSION = '.pbtxt'
