# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SourceCode\Final-Year-Project\Workspace\Prototypes\GUIs\UserInterface\View\basicGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QStyle, QLabel, QSizePolicy
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow(object):
    def __init__(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1680, 1050)
        main_window.setMinimumSize(QtCore.QSize(1680, 1050))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("central_widget")

        self.video_player_widget = QVideoWidget(self.centralwidget)
        self.video_player_widget.setGeometry(QtCore.QRect(20, 40, 671, 531))
        self.video_player_widget.setObjectName("video_player_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 580, 671, 111))
        self.verticalLayoutWidget.setObjectName("__base_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("__menu_buttons_layout")
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.skip_to_start_of_video_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_to_start_of_video_button.setObjectName("skip_to_start_of_video_button")

        self.horizontalLayout.addWidget(self.skip_to_start_of_video_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.play_video_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play_video_button.setObjectName("play_video_button")

        self.horizontalLayout.addWidget(self.play_video_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.skip_to_end_of_video_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_to_end_of_video_button.setObjectName("skip_to_end_of_video_button")

        self.horizontalLayout.addWidget(self.skip_to_end_of_video_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(800, 40, 721, 861))
        self.verticalLayoutWidget_2.setObjectName("detection_vertical_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.listView_2 = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_3.addWidget(self.listView_2)
        self.listView_3 = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listView_3.setObjectName("listView_3")
        self.verticalLayout_3.addWidget(self.listView_3)
        self.listView_4 = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listView_4.setObjectName("listView_4")
        self.verticalLayout_3.addWidget(self.listView_4)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.verticalLayoutWidget_2)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_3.addWidget(self.verticalScrollBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.video_player_label = QtWidgets.QLabel(self.centralwidget)
        self.video_player_label.setGeometry(QtCore.QRect(250, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.video_player_label.setFont(font)
        self.video_player_label.setAlignment(QtCore.Qt.AlignCenter)
        self.video_player_label.setObjectName("video_player_label")
        self.detection_label = QtWidgets.QLabel(self.centralwidget)
        self.detection_label.setGeometry(QtCore.QRect(1060, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.detection_label.setFont(font)
        self.detection_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detection_label.setObjectName("detection_label")
        main_window.setCentralWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1680, 18))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.video_player_widget)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                                      QSizePolicy.Maximum)
        self.set_text_and_icons(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def set_text_and_icons(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        icon_object = QtWidgets.QWidget(main_window).style()

        self.skip_to_start_of_video_button.setIcon(icon_object.standardIcon(QStyle.SP_MediaSkipBackward))
        self.play_video_button.setIcon(icon_object.standardIcon(QStyle.SP_MediaPlay))
        self.skip_to_end_of_video_button.setIcon(icon_object.standardIcon(QStyle.SP_MediaSkipForward))

        self.video_player_label.setText(_translate("main_window", "Video Player"))
        self.detection_label.setText(_translate("main_window", "Detections"))

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

    def time_left_counter(self):
        return self.time_left_counter

    def time_into_video_counter(self):
        return self.time_into_video_counter

    def get_menu_bar(self):
        return self.menu_bar



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())