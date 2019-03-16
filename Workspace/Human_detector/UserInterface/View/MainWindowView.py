from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QStyle, QLabel, QSizePolicy, QScrollArea, QWidget, QMainWindow
from PyQt5.QtMultimediaWidgets import QVideoWidget
from Human_detector.config import Config


class MainWindowView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__(parent=None)
        self.setupUi()

    def setupUi(self, window_height=Config.WINDOW_HEIGHT, window_width=Config.WINDOW_WIDTH):
        self.setObjectName("main_window")

        self.resize(window_height, window_width)
        self.setMinimumSize(QtCore.QSize(Config.WINDOW_HEIGHT, Config.WINDOW_WIDTH))
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.video_player_widget = QVideoWidget(self.central_widget)

        self.video_player_widget.setObjectName("video_player_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.central_widget)

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.time_into_video_counter = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.time_into_video_counter.setObjectName("time_into_video_counter")

        self.horizontalLayout_2.addWidget(self.time_into_video_counter)

        self.video_position_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.video_position_slider.setOrientation(QtCore.Qt.Horizontal)
        self.video_position_slider.setObjectName("video_position_slider")

        self.horizontalLayout_2.addWidget(self.video_position_slider)

        self.time_left_counter = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.time_left_counter.setObjectName("time_left_counter")

        self.horizontalLayout_2.addWidget(self.time_left_counter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spacer_item = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(self.spacer_item)

        self.skip_to_start_of_video_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_to_start_of_video_button.setObjectName("skip_to_start_of_video_button")

        self.horizontalLayout.addWidget(self.skip_to_start_of_video_button)
        self.spacer_item_1 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.spacer_item_1)

        self.play_video_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play_video_button.setObjectName("play_video_button")

        self.horizontalLayout.addWidget(self.play_video_button)
        self.spacer_item_2 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.spacer_item_2)

        self.skip_to_end_of_video_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_to_end_of_video_button.setObjectName("skip_to_end_of_video_button")

        self.horizontalLayout.addWidget(self.skip_to_end_of_video_button)
        self.spacer_item_3 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(self.spacer_item_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.detection_vertical_layout = QtWidgets.QWidget(self.central_widget)

        self.detection_vertical_layout.setObjectName("detection_vertical_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.detection_vertical_layout)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.detection_list_scrollable_area = QScrollArea()
        self.horizontalLayout_3.addWidget(self.detection_list_scrollable_area)
        self.detection_list_scrollable_area.setWidgetResizable(True)

        scroll_content = QWidget(self.detection_list_scrollable_area)
        self.detection_list_scrollable_area.setWidget(scroll_content)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar()

        self.menu_bar.setObjectName("menu_bar")
        self.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.setObjectName("status_bar")
        self.setStatusBar(self.status_bar)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                                      QSizePolicy.Maximum)
        self.set_text_and_icons(self)
        self.update_geometry()

    def update_geometry(self):
        self.video_player_widget.setGeometry(
            QtCore.QRect(
                self.__percentage_of_width(1.5),  # margin - left
                self.__percentage_of_height(5),  # margin - top
                self.__percentage_of_width(50),  # width
                self.__percentage_of_height(50)  # height
            )
        )
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(
                self.__percentage_of_width(1.5),  # margin - left
                self.__percentage_of_height(52),  # margin - top
                self.__percentage_of_width(50),  # width
                self.__percentage_of_height(10)  # height
            )
        )

        self.spacer_item = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.spacer_item_1 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.spacer_item_2 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.spacer_item_3 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(1.5),  # margin - left
            self.__percentage_of_height(5),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.detection_vertical_layout.setGeometry(
            QtCore.QRect(
                self.__percentage_of_width(55),  # margin - left
                self.__percentage_of_height(5),  # margin - top
                self.__percentage_of_width(40),  # width
                self.__percentage_of_height(80)  # height
            )
        )

    def __percentage_of_height(self, percentage):
        return (percentage / 100) * self.geometry().height()

    def resizeEvent(self, event):
        self.update_geometry()  # call your update method
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def __percentage_of_width(self, percentage):
        return (percentage / 100) * self.geometry().width()

    def set_text_and_icons(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        icon_object = QtWidgets.QWidget(main_window).style()

        self.skip_to_start_of_video_button.setIcon(icon_object.standardIcon(QStyle.SP_MediaSkipBackward))
        self.play_video_button.setIcon(icon_object.standardIcon(QStyle.SP_MediaPlay))
        self.skip_to_end_of_video_button.setIcon(icon_object.standardIcon(QStyle.SP_MediaSkipForward))

    def get_video_widget(self):
        return self.video_player_widget

    def get_media_player(self):
        return self.mediaPlayer

    def get_play_button(self):
        return self.play_video_button

    def get_skip_backward_button(self):
        return self.skip_to_start_of_video_button

    def get_skip_forward_button(self):
        return self.skip_to_end_of_video_button

    def get_position_slider(self):
        return self.video_position_slider

    def get_error_label(self):
        return self.errorLabel

    def get_time_left_counter(self):
        return self.time_left_counter

    def get_time_into_video_counter(self):
        return self.time_into_video_counter

    def get_menu_bar(self):
        return self.menu_bar

    def get_detection_event_scroll_area(self):
        return self.detection_list_scrollable_area

    def get_detection_vertical_layout(self):
        return self.detection_vertical_layout



