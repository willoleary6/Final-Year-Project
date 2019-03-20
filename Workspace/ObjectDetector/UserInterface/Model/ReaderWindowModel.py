import subprocess
import cv2

class ReaderWindowModel:

    @staticmethod
    def open_file_in_explorer(file_path):
        subprocess.check_call(['nautilus', '--', file_path])

    @staticmethod
    def check_connection_with_live_stream(address_of_stream):
        # rtsp://willoleary6:password1@192.168.1.210:554/videoMain
        cap = cv2.VideoCapture(address_of_stream)
        for i in range(5):
            # Read frame from camera
            ret, image_np = cap.read()
            if image_np is not None:
                return True
        return False
