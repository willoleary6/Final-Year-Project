import os
import subprocess
import cv2


class ReaderWindowModel:

    @staticmethod
    def open_file_in_explorer(file_path):
        subprocess.check_call(['nautilus', '--', file_path])

    @staticmethod
    def check_connection_with_live_stream(signal, address_of_stream):
        # rtsp://willoleary6:password1@192.168.1.210:554/videoMain
        successful_test = False
        cap = cv2.VideoCapture(address_of_stream)
        for i in range(5):
            # Read frame from camera
            ret, image_np = cap.read()
            if image_np is not None:
                successful_test = True

        if successful_test:
            signal.emit(
                (
                    "Connection Established",
                    "background-color: green; color: white"
                )
            )
        else:
            signal.emit(
                (
                    "Connection Failed",
                    "background-color: red; color: white"
                )
            )

    @staticmethod
    def check_if_file_path_is_valid(field, is_directory, desired_extension='/'):
        if is_directory and field.text().endswith(desired_extension):
            return os.path.isdir(field.text())
        elif not is_directory and field.text().endswith(desired_extension):
            return os.path.isfile(field.text())

