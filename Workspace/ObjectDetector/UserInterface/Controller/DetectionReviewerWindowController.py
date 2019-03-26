import _thread
import math
import time
from functools import partial
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QStyle, QWidget, QVBoxLayout
from PyQt5 import QtCore, QtWidgets
from Workspace.ObjectDetector.UserInterface.Model.DetectionReviewerWindowModel import DetectionReviewerWindowModel
from Workspace.ObjectDetector.UserInterface.View.DetectionReviewerWindowView import DetectionReviewerWindowView
from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from Workspace.ObjectDetector.config import Config


def check_for_database_changes(signal, window_controller, model):
    while True:
        try:
            time.sleep(Config.THREAD_LOOP_DELAY)
            database_detections = model.get_detections_from_database()
            current_detections = window_controller.get_array_of_detection_events()
            if len(database_detections) != len(current_detections):
                signal.emit(database_detections)
        except Exception as e:
            print(e)


class DetectionReviewerWindowController(QMainWindow, ViewController):
    signal = QtCore.pyqtSignal(object)

    def __init__(self, coordinator, parent=None):
        super(DetectionReviewerWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        # Window objects
        self.__detection_reviewer_window_view = DetectionReviewerWindowView()
        self.__detection_reviewer_window_model = DetectionReviewerWindowModel()
        self.__detection_reviewer_window_position_slider = self.__detection_reviewer_window_view.get_position_slider()
        self.__detection_reviewer_window_menu_bar = self.__detection_reviewer_window_view.get_menu_bar()
        self.__detection_reviewer_window_video_widget = self.__detection_reviewer_window_view.get_video_widget()
        self.__detection_reviewer_window_play_button = self.__detection_reviewer_window_view.get_play_button()
        self.__detection_reviewer_window_media_player = self.__detection_reviewer_window_view.get_media_player()
        self.__detection_reviewer_window_media_player.setVideoOutput(self.__detection_reviewer_window_video_widget)
        self.__detection_reviewer_window_skip_backwards = self.__detection_reviewer_window_view.get_skip_backward_button()
        self.__detection_reviewer_window_skip_forwards = self.__detection_reviewer_window_view.get_skip_forward_button()
        self.__detection_reviewer_window_time_into_video_counter = self.__detection_reviewer_window_view.get_time_into_video_counter()
        self.__detection_reviewer_window_time_left_counter = self.__detection_reviewer_window_view.get_time_left_counter()
        self.__detection_reviewer_window_detection_list_scroll_area = self.__detection_reviewer_window_view.get_detection_event_scroll_area()
        self.__detection_reviewer_window_detections_vertical_layout = self.__detection_reviewer_window_view.get_detection_vertical_layout()

        self.initialise_menu_bar_actions()
        self.connect_ui_elements_to_methods()
        # misc
        self.__video_duration = 0
        self.__current_selected_detection = None
        self.__array_of_detection_events = self.__detection_reviewer_window_model.get_detections_from_database()
        self.initialise_detections()

        try:
            _thread.start_new_thread(check_for_database_changes, (self.signal,
                                                                  self,
                                                                  self.__detection_reviewer_window_model))
        except Exception as e:
            print("Error: unable to start thread")
            print(e)

        self.signal.connect(self.update_detections)



    def get_array_of_detection_events(self):
        return self.__array_of_detection_events

    @staticmethod
    def format_event_text(detection_event):
        formatted_text = 'Objects Detected: '
        # getting names of objects
        for i, name in enumerate(detection_event.get_objects_detected()):
            formatted_text += name
            if i < len(detection_event.get_objects_detected()) - 1:
                formatted_text += ","
        formatted_text += "\n"
        # time frame
        formatted_text += "Time Frame: " + str(detection_event.get_start_timestamp()) + "s - " + str(
            detection_event.get_end_timestamp()) + "s"
        formatted_text += "\n"
        # number of detections
        formatted_text += "Detections: " + str(detection_event.get_minimum_number_of_object_detections()) \
                          + " - " + str(detection_event.get_maximum_number_of_object_detections())
        formatted_text += "\n"
        # video file
        file_path_array = detection_event.get_file_path().split("/")
        formatted_text += "File name: " + file_path_array[len(file_path_array) - 1]
        return formatted_text

    def update_detections(self, new_detections):
        self.__array_of_detection_events = new_detections
        self.initialise_detections(False)

    def initialise_detections(self, initialise=True):
        items = []
        
        for detection_event in self.__array_of_detection_events[::-1]:
            list_widget = QtWidgets.QListWidget(self.__detection_reviewer_window_detections_vertical_layout)
            list_widget_item = QtWidgets.QListWidgetItem(list_widget)
            size = QtCore.QSize(10, 100)
            list_widget_item.setSizeHint(size)
            list_widget_item.setText(self.format_event_text(detection_event))
            list_widget.itemSelectionChanged.connect(
                partial(self.detection_selected, detection_event, list_widget_item))
            items.append(list_widget)
        scroll_content = QWidget(self.__detection_reviewer_window_detection_list_scroll_area)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)
        for item in items:
            scroll_layout.addWidget(item)
        self.__detection_reviewer_window_detection_list_scroll_area.setWidgetResizable(True)
        self.__detection_reviewer_window_detection_list_scroll_area.setWidget(scroll_content)
        if initialise:
            if len(self.__array_of_detection_events) > 0:
                first_detection = self.__array_of_detection_events[0]
                self.change_video_playing(first_detection)
                self.__detection_reviewer_window_play_button.setEnabled(True)
            else:
                self.__detection_reviewer_window_play_button.setEnabled(False)

    def initialise_view(self):
        self.__detection_reviewer_window_view.show()

    def connect_ui_elements_to_methods(self):
        self.__detection_reviewer_window_position_slider.sliderMoved.connect(self.set_position_slider)
        self.__detection_reviewer_window_play_button.clicked.connect(self.play)
        self.__detection_reviewer_window_skip_backwards.clicked.connect(self.skip_to_start)
        self.__detection_reviewer_window_skip_forwards.clicked.connect(self.skip_to_end)

        self.__detection_reviewer_window_media_player.stateChanged.connect(self.video_player_state_changed)
        self.__detection_reviewer_window_media_player.positionChanged.connect(self.position_changed)
        self.__detection_reviewer_window_media_player.durationChanged.connect(self.duration_changed)
        self.__detection_reviewer_window_media_player.error.connect(self.handle_error)

    def change_video_playing(self, detection_event):
        self.__current_selected_detection = detection_event
        self.__detection_reviewer_window_media_player.setMedia(
            QMediaContent(QUrl.fromLocalFile(self.__current_selected_detection.get_file_path())))
        self.__detection_reviewer_window_play_button.setEnabled(True)
        self.set_position_slider(self.__current_selected_detection.get_start_timestamp() * 1000)

    def initialise_menu_bar_actions(self):
        self.__detection_reviewer_window_menu_bar = QtWidgets.QMenuBar(self.__detection_reviewer_window_view)
        self.__detection_reviewer_window_menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.__detection_reviewer_window_menu_bar.setObjectName("menubar")
        menu_file = QtWidgets.QMenu(self.__detection_reviewer_window_menu_bar)
        menu_file.setObjectName("menu_file")
        self.__detection_reviewer_window_view.setMenuBar(self.__detection_reviewer_window_menu_bar)
        status_bar = QtWidgets.QStatusBar(self.__detection_reviewer_window_view)
        status_bar.setObjectName("status_bar")
        self.__detection_reviewer_window_view.setStatusBar(status_bar)
        open_action = QtWidgets.QAction(self.__detection_reviewer_window_view)
        open_action.setObjectName("open_action")
        delete_selected_detection_action = QtWidgets.QAction(self.__detection_reviewer_window_view)
        delete_selected_detection_action.setObjectName("delete_selected_detection_action")
        menu_file.addAction(open_action)
        menu_file.addAction(delete_selected_detection_action)
        self.__detection_reviewer_window_menu_bar.addAction(menu_file.menuAction())
        self.__detection_reviewer_window_menu_bar.show()
        file_menu = self.__detection_reviewer_window_menu_bar.addMenu('&Tools')
        file_menu.addAction(open_action)
        file_menu.addAction(delete_selected_detection_action)
        _translate = QtCore.QCoreApplication.translate
        open_action.setText(_translate("MainWindow", "Open Current Video in Explorer"))
        open_action.triggered.connect(self.open_current_video_in_file_explorer)

        delete_selected_detection_action.setText(_translate("MainWindow", "Delete Current detection"))
        delete_selected_detection_action.triggered.connect(self.delete_currently_selected_detection)

    def open_current_video_in_file_explorer(self):
        if self.__current_selected_detection is not None:
            DetectionReviewerWindowModel.open_file_in_explorer(self.__current_selected_detection.get_file_path())

    def delete_currently_selected_detection(self):
        if self.__current_selected_detection is not None:
            self.__detection_reviewer_window_media_player.pause()
            self.__detection_reviewer_window_model.delete_detection(self.__current_selected_detection.get_id())

    def open_file(self):
        file_path = self.__current_selected_detection.get_file_path()
        if file_path is not None:
            self.__detection_reviewer_window_media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.__detection_reviewer_window_play_button.setEnabled(True)

    def play(self):
        if self.__detection_reviewer_window_media_player.state() == QMediaPlayer.PlayingState:
            self.__detection_reviewer_window_media_player.pause()
        else:
            self.__detection_reviewer_window_media_player.play()

    def skip_to_start(self):
        self.set_position_slider(0)
        self.__detection_reviewer_window_media_player.play()

    def skip_to_end(self):
        self.set_position_slider(self.__video_duration)
        self.__detection_reviewer_window_media_player.play()

    def update_time_left_counter(self, timestamp):
        timestamp = self.__video_duration - timestamp
        timestamp_in_seconds = timestamp / 1000
        minutes = math.floor(timestamp_in_seconds / 60)
        seconds = round(timestamp_in_seconds % 60)
        string_minutes = str(minutes)
        if minutes < 10:
            string_minutes = '0' + string_minutes
        string_seconds = str(seconds)
        if seconds < 10:
            string_seconds = '0' + string_seconds

        self.__detection_reviewer_window_time_left_counter.display(string_minutes + ':' + string_seconds)

    def update_time_into_video_counter(self, timestamp):
        timestamp_in_seconds = timestamp / 1000
        minutes = math.floor(timestamp_in_seconds / 60)
        seconds = round(timestamp_in_seconds % 60)
        string_minutes = str(minutes)
        if minutes < 10:
            string_minutes = '0' + string_minutes
        string_seconds = str(seconds)
        if seconds < 10:
            string_seconds = '0' + string_seconds

        self.__detection_reviewer_window_time_into_video_counter.display(string_minutes + ':' + string_seconds)

    def video_player_state_changed(self):
        if self.__detection_reviewer_window_media_player.state() == QMediaPlayer.PlayingState:
            self.__detection_reviewer_window_play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.__detection_reviewer_window_play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.update_time_into_video_counter(position)
        self.update_time_left_counter(position)
        self.__detection_reviewer_window_position_slider.setValue(position)

    def duration_changed(self, duration):
        self.__video_duration = duration
        self.__detection_reviewer_window_position_slider.setRange(0, self.__video_duration)

    def set_position_slider(self, position):
        self.__detection_reviewer_window_media_player.setPosition(position)

    def handle_error(self):
        self.__detection_reviewer_window_play_button.setEnabled(False)
        print("Error: " + self.__detection_reviewer_window_media_player.errorString())

    def detection_selected(self, detection_event, list_widget_item):
        if list_widget_item.isSelected():
            list_widget_item.setSelected(False)
            self.change_video_playing(detection_event)
            self.play()

    def show(self):
        self.__detection_reviewer_window_view.show()

    def hide(self):
        self.__detection_reviewer_window_view.hide()
