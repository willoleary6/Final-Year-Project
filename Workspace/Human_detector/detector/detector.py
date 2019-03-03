class detector:
    def __init__(self):
        self.__detections = []

    def new_detection(self, filename, timestamp, number_of_objects):
        print(filename)
        print(timestamp)
        print(number_of_objects)
