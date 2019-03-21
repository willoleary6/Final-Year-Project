import math
from functools import partial

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QStyle, QAction, QWidget, QVBoxLayout
from PyQt5 import QtCore, QtWidgets
from Prototypes.GUIs.PyQT.Model.MainWindowModel import MainWindowModel
from Prototypes.GUIs.PyQT.View.MainWindowView import MainWindowView


class MainWindowController(QMainWindow):
    def __init__(self, coordinator, main_window, parent=None):
        super(MainWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        # Window objects
        self.__main_window = main_window
        self.__main_window_view = MainWindowView(self.__main_window)
        self.__main_window_model = MainWindowModel()

        # set each of the ui elemements
        self.__main_window_error_label = self.__main_window_view.get_error_label()
        self.__main_window_position_slider = self.__main_window_view.get_position_slider()
        self.__main_window_menu_bar = self.__main_window_view.get_menu_bar()
        self.__video_widget = self.__main_window_view.get_video_widget()
        self.__main_window_play_button = self.__main_window_view.get_play_button()
        self.__main_window_media_player = self.__main_window_view.get_frame_display()
        self.__main_window_media_player.setVideoOutput(self.__video_widget)
        self.__main_window_skip_backwards = self.__main_window_view.get_skip_backward_button()
        self.__main_window_skip_forwards = self.__main_window_view.get_skip_forward_button()
        self.__main_window_time_into_video_counter = self.__main_window_view.get_time_into_video_counter()
        self.__main_window_time_left_counter = self.__main_window_view.get_time_left_counter()
        self.__main_window_detection_list_scroll_area = self.__main_window_view.get_detection_event_scroll_area()
        self.__main_window_detections_vertical_layout = self.__main_window_view.get_detection_vertical_layout()

        self.initialise_menu_bar_actions()
        self.connect_ui_elements_to_methods()
        self.initialise_detections()
        # misc
        self.__video_duration = 0

    def initialise_detections(self):
        items = []
        for x in range(50):
            list_widget = QtWidgets.QListWidget(self.__main_window_detections_vertical_layout)
            # self.list_widget.mousePressEvent = self.detection_selected
            message = "test " + str(x)
            list_widget_item = QtWidgets.QListWidgetItem(list_widget)
            size = QtCore.QSize(10, 100)
            list_widget_item.setSizeHint(size)

            T = x * 15
            list_widget_item.setText(str(T))
            list_widget_item.setData(1, T)

            list_widget.itemSelectionChanged.connect(partial(self.clicked_event, message, list_widget_item))
            items.append(list_widget)
        scroll_content = QWidget(self.__main_window_detection_list_scroll_area)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)
        for item in items:
            scroll_layout.addWidget(item)
        self.__main_window_detection_list_scroll_area.setWidget(scroll_content)

    def connect_ui_elements_to_methods(self):
        self.__main_window_position_slider.sliderMoved.connect(self.setPosition)
        self.__main_window_play_button.clicked.connect(self.play)
        self.__main_window_skip_backwards.clicked.connect(self.skip_to_start)
        self.__main_window_skip_forwards.clicked.connect(self.skip_to_end)

        self.__main_window_media_player.stateChanged.connect(self.mediaStateChanged)
        self.__main_window_media_player.position_changed.connect(self.positionChanged)
        self.__main_window_media_player.duration_changed.connect(self.durationChanged)
        self.__main_window_media_player.error.connect(self.handleError)

    def initialise_view(self):
        self.__main_window.show()
        self.__main_window_media_player.setMedia(
            QMediaContent(QUrl.fromLocalFile('D:/Crystalline growth/video files/FFA3.mp4')))
        self.__main_window_play_button.setEnabled(True)
        self.play()

    def initialise_menu_bar_actions(self):
        # Create new action
        open_action = QAction(QIcon('open.png'), '&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open movie')
        open_action.triggered.connect(self.open_file)

        # Create menu bar and add action
        print(self.__main_window_menu_bar.children())
        file_menu = self.__main_window_menu_bar.addMenu('&File')
        file_menu.addAction(open_action)
        print(self.__main_window_menu_bar.children())

    def file_menu_clicked(self):
        print('test')

    def open_file(self):
        file_path = self.__main_window_model.openFile()
        if file_path is not None:
            self.__main_window_media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.__main_window_play_button.setEnabled(True)

    def play(self):
        if self.__main_window_media_player.state() == QMediaPlayer.PlayingState:
            self.__main_window_media_player.pause()
        else:
            self.__main_window_media_player.play()

    def skip_to_start(self):
        # self.positionChanged(0)
        self.setPosition(0)
        self.__main_window_media_player.play()

    def skip_to_end(self):
        # self.positionChanged(self.__video_duration)
        self.setPosition(self.__video_duration)
        self.__main_window_media_player.play()

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

        self.__main_window_time_left_counter.display(string_minutes + ':' + string_seconds)

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

        self.__main_window_time_into_video_counter.display(string_minutes + ':' + string_seconds)

    def mediaStateChanged(self):
        if self.__main_window_media_player.state() == QMediaPlayer.PlayingState:
            self.__main_window_play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.__main_window_play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.update_time_into_video_counter(position)
        self.update_time_left_counter(position)
        self.__main_window_position_slider.setValue(position)

    def durationChanged(self, duration):
        self.__video_duration = duration
        self.__main_window_position_slider.setRange(0, self.__video_duration)

    def setPosition(self, position):
        self.__main_window_media_player.set_position_slider(position)

    def handleError(self):
        self.__main_window_play_button.setEnabled(False)
        self.__main_window_error_label.setText("Error: " + self.__main_window_media_player.errorString())

    def clicked_event(self, value, list_widget_item):

        if list_widget_item.isSelected():
            list_widget_item.setSelected(False)
            print(value)
