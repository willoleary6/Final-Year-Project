# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/will/SourceCode/Final-Year-Project/Workspace/ObjectDetector/UserInterface/misc/Reader.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2937, 1725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 2921, 1638))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.readers_horizontal_layout = QtWidgets.QHBoxLayout()
        self.readers_horizontal_layout.setObjectName("readers_horizontal_layout")
        self.saved_file_reader_vertical_layout = QtWidgets.QVBoxLayout()
        self.saved_file_reader_vertical_layout.setObjectName("saved_file_reader_vertical_layout")
        self.file_reader_title_horizontal_layout = QtWidgets.QHBoxLayout()
        self.file_reader_title_horizontal_layout.setObjectName("file_reader_title_horizontal_layout")
        self.file_reader_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_title.setAlignment(QtCore.Qt.AlignCenter)
        self.file_reader_title.setObjectName("file_reader_title")
        self.file_reader_title_horizontal_layout.addWidget(self.file_reader_title)
        self.saved_file_reader_vertical_layout.addLayout(self.file_reader_title_horizontal_layout)
        self.file_reader_status_horizontal_layout = QtWidgets.QHBoxLayout()
        self.file_reader_status_horizontal_layout.setObjectName("file_reader_status_horizontal_layout")
        self.file_reader_status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_reader_status_label.setObjectName("file_reader_status_label")
        self.file_reader_status_horizontal_layout.addWidget(self.file_reader_status_label)
        self.saved_file_reader_vertical_layout.addLayout(self.file_reader_status_horizontal_layout)
        self.file_reader_file_path_field_horizontal_layout = QtWidgets.QHBoxLayout()
        self.file_reader_file_path_field_horizontal_layout.setObjectName("file_reader_file_path_field_horizontal_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_file_path_field_horizontal_layout.addItem(spacerItem)
        self.file_reader_file_path_field_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_file_path_field_title.setMinimumSize(QtCore.QSize(150, 0))
        self.file_reader_file_path_field_title.setObjectName("file_reader_file_path_field_title")
        self.file_reader_file_path_field_horizontal_layout.addWidget(self.file_reader_file_path_field_title)
        self.file_reader_file_path_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_reader_file_path_field.setMinimumSize(QtCore.QSize(400, 0))
        self.file_reader_file_path_field.setObjectName("file_reader_file_path_field")
        self.file_reader_file_path_field_horizontal_layout.addWidget(self.file_reader_file_path_field)
        self.file_reader_file_path_open_nautilus_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_reader_file_path_open_nautilus_button.setMinimumSize(QtCore.QSize(125, 0))
        self.file_reader_file_path_open_nautilus_button.setObjectName("file_reader_file_path_open_nautilus_button")
        self.file_reader_file_path_field_horizontal_layout.addWidget(self.file_reader_file_path_open_nautilus_button)
        self.file_reader_file_path_field_status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_file_path_field_status_label.setMinimumSize(QtCore.QSize(150, 0))
        self.file_reader_file_path_field_status_label.setObjectName("file_reader_file_path_field_status_label")
        self.file_reader_file_path_field_horizontal_layout.addWidget(self.file_reader_file_path_field_status_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_file_path_field_horizontal_layout.addItem(spacerItem1)
        self.saved_file_reader_vertical_layout.addLayout(self.file_reader_file_path_field_horizontal_layout)
        self.file_reader_inference_path_horizontal_layout = QtWidgets.QHBoxLayout()
        self.file_reader_inference_path_horizontal_layout.setObjectName("file_reader_inference_path_horizontal_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_inference_path_horizontal_layout.addItem(spacerItem2)
        self.file_reader_inference_path_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_inference_path_title.setMinimumSize(QtCore.QSize(150, 0))
        self.file_reader_inference_path_title.setObjectName("file_reader_inference_path_title")
        self.file_reader_inference_path_horizontal_layout.addWidget(self.file_reader_inference_path_title)
        self.file_reader_inference_path_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_reader_inference_path_field.setMinimumSize(QtCore.QSize(400, 0))
        self.file_reader_inference_path_field.setObjectName("file_reader_inference_path_field")
        self.file_reader_inference_path_horizontal_layout.addWidget(self.file_reader_inference_path_field)
        self.file_reader_inference_path_open_nautlus_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_reader_inference_path_open_nautlus_button.setMinimumSize(QtCore.QSize(125, 0))
        self.file_reader_inference_path_open_nautlus_button.setObjectName("file_reader_inference_path_open_nautlus_button")
        self.file_reader_inference_path_horizontal_layout.addWidget(self.file_reader_inference_path_open_nautlus_button)
        self.file_reader_inference_path_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_inference_path_status.setMinimumSize(QtCore.QSize(150, 0))
        self.file_reader_inference_path_status.setObjectName("file_reader_inference_path_status")
        self.file_reader_inference_path_horizontal_layout.addWidget(self.file_reader_inference_path_status)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_inference_path_horizontal_layout.addItem(spacerItem3)
        self.saved_file_reader_vertical_layout.addLayout(self.file_reader_inference_path_horizontal_layout)
        self.file_reader_labels_path = QtWidgets.QHBoxLayout()
        self.file_reader_labels_path.setObjectName("file_reader_labels_path")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_labels_path.addItem(spacerItem4)
        self.file_reader_labels_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_labels_title.setMinimumSize(QtCore.QSize(150, 0))
        self.file_reader_labels_title.setObjectName("file_reader_labels_title")
        self.file_reader_labels_path.addWidget(self.file_reader_labels_title)
        self.file_reader_labels_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_reader_labels_field.setMinimumSize(QtCore.QSize(400, 0))
        self.file_reader_labels_field.setObjectName("file_reader_labels_field")
        self.file_reader_labels_path.addWidget(self.file_reader_labels_field)
        self.file_reader_labels_open_nautilus_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_reader_labels_open_nautilus_button.setMinimumSize(QtCore.QSize(125, 0))
        self.file_reader_labels_open_nautilus_button.setObjectName("file_reader_labels_open_nautilus_button")
        self.file_reader_labels_path.addWidget(self.file_reader_labels_open_nautilus_button)
        self.file_reader_labels_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_reader_labels_status.setMinimumSize(QtCore.QSize(150, 0))
        self.file_reader_labels_status.setObjectName("file_reader_labels_status")
        self.file_reader_labels_path.addWidget(self.file_reader_labels_status)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_labels_path.addItem(spacerItem5)
        self.saved_file_reader_vertical_layout.addLayout(self.file_reader_labels_path)
        self.file_reader_start_stop_buttons_horizontal_layout = QtWidgets.QHBoxLayout()
        self.file_reader_start_stop_buttons_horizontal_layout.setObjectName("file_reader_start_stop_buttons_horizontal_layout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_start_stop_buttons_horizontal_layout.addItem(spacerItem6)
        self.file_reader_start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_reader_start_button.setMinimumSize(QtCore.QSize(125, 0))
        self.file_reader_start_button.setObjectName("file_reader_start_button")
        self.file_reader_start_stop_buttons_horizontal_layout.addWidget(self.file_reader_start_button)
        self.file_reader_stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_reader_stop_button.setMinimumSize(QtCore.QSize(125, 0))
        self.file_reader_stop_button.setObjectName("file_reader_stop_button")
        self.file_reader_start_stop_buttons_horizontal_layout.addWidget(self.file_reader_stop_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_reader_start_stop_buttons_horizontal_layout.addItem(spacerItem7)
        self.saved_file_reader_vertical_layout.addLayout(self.file_reader_start_stop_buttons_horizontal_layout)
        self.readers_horizontal_layout.addLayout(self.saved_file_reader_vertical_layout)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.readers_horizontal_layout.addWidget(self.widget)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.readers_horizontal_layout.addWidget(self.line)
        self.live_stream_reader_vertical_layout = QtWidgets.QVBoxLayout()
        self.live_stream_reader_vertical_layout.setObjectName("live_stream_reader_vertical_layout")
        self.live_stream_reader_title_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_title_horizontal_layout.setObjectName("live_stream_reader_title_horizontal_layout")
        self.live_stream_reader_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.live_stream_reader_title_label.setObjectName("live_stream_reader_title_label")
        self.live_stream_reader_title_horizontal_layout.addWidget(self.live_stream_reader_title_label)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_title_horizontal_layout)
        self.live_stream_reader_status_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_status_horizontal_layout.setObjectName("live_stream_reader_status_horizontal_layout")
        self.live_stream_reader_status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.live_stream_reader_status_label.setObjectName("live_stream_reader_status_label")
        self.live_stream_reader_status_horizontal_layout.addWidget(self.live_stream_reader_status_label)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_status_horizontal_layout)
        self.live_stream_reader_ip_field_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_ip_field_horizontal_layout.setObjectName("live_stream_reader_ip_field_horizontal_layout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_ip_field_horizontal_layout.addItem(spacerItem8)
        self.live_stream_reader_ip_field_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_ip_field_title.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_ip_field_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.live_stream_reader_ip_field_title.setObjectName("live_stream_reader_ip_field_title")
        self.live_stream_reader_ip_field_horizontal_layout.addWidget(self.live_stream_reader_ip_field_title)
        self.live_stream_reader_ip_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.live_stream_reader_ip_field.setMinimumSize(QtCore.QSize(400, 0))
        self.live_stream_reader_ip_field.setAlignment(QtCore.Qt.AlignCenter)
        self.live_stream_reader_ip_field.setObjectName("live_stream_reader_ip_field")
        self.live_stream_reader_ip_field_horizontal_layout.addWidget(self.live_stream_reader_ip_field)
        self.live_stream_reader_ip_field_check_connection = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.live_stream_reader_ip_field_check_connection.setMinimumSize(QtCore.QSize(125, 0))
        self.live_stream_reader_ip_field_check_connection.setObjectName("live_stream_reader_ip_field_check_connection")
        self.live_stream_reader_ip_field_horizontal_layout.addWidget(self.live_stream_reader_ip_field_check_connection)
        self.live_stream_reader_ip_field_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_ip_field_status.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_ip_field_status.setObjectName("live_stream_reader_ip_field_status")
        self.live_stream_reader_ip_field_horizontal_layout.addWidget(self.live_stream_reader_ip_field_status)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_ip_field_horizontal_layout.addItem(spacerItem9)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_ip_field_horizontal_layout)
        self.live_stream_reader_recordings_file_path_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_recordings_file_path_horizontal_layout.setObjectName("live_stream_reader_recordings_file_path_horizontal_layout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_recordings_file_path_horizontal_layout.addItem(spacerItem10)
        self.live_stream_reader_recordings_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_recordings_title.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_recordings_title.setObjectName("live_stream_reader_recordings_title")
        self.live_stream_reader_recordings_file_path_horizontal_layout.addWidget(self.live_stream_reader_recordings_title)
        self.live_stream_reader_recordings_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.live_stream_reader_recordings_field.setMinimumSize(QtCore.QSize(400, 0))
        self.live_stream_reader_recordings_field.setObjectName("live_stream_reader_recordings_field")
        self.live_stream_reader_recordings_file_path_horizontal_layout.addWidget(self.live_stream_reader_recordings_field)
        self.live_stream_reader_recordings_open_nautilus_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.live_stream_reader_recordings_open_nautilus_button.setMinimumSize(QtCore.QSize(125, 0))
        self.live_stream_reader_recordings_open_nautilus_button.setObjectName("live_stream_reader_recordings_open_nautilus_button")
        self.live_stream_reader_recordings_file_path_horizontal_layout.addWidget(self.live_stream_reader_recordings_open_nautilus_button)
        self.live_stream_reader_recordings_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_recordings_status.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_recordings_status.setObjectName("live_stream_reader_recordings_status")
        self.live_stream_reader_recordings_file_path_horizontal_layout.addWidget(self.live_stream_reader_recordings_status)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_recordings_file_path_horizontal_layout.addItem(spacerItem11)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_recordings_file_path_horizontal_layout)
        self.live_stream_reader_inference_graph_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_inference_graph_horizontal_layout.setObjectName("live_stream_reader_inference_graph_horizontal_layout")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_inference_graph_horizontal_layout.addItem(spacerItem12)
        self.live_stream_reader_inference_graph_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_inference_graph_title.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_inference_graph_title.setObjectName("live_stream_reader_inference_graph_title")
        self.live_stream_reader_inference_graph_horizontal_layout.addWidget(self.live_stream_reader_inference_graph_title)
        self.live_stream_reader_inference_graph_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.live_stream_reader_inference_graph_field.setMinimumSize(QtCore.QSize(400, 0))
        self.live_stream_reader_inference_graph_field.setObjectName("live_stream_reader_inference_graph_field")
        self.live_stream_reader_inference_graph_horizontal_layout.addWidget(self.live_stream_reader_inference_graph_field)
        self.live_stream_reader_inference_graph_open_nautilus_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.live_stream_reader_inference_graph_open_nautilus_button.setMinimumSize(QtCore.QSize(125, 0))
        self.live_stream_reader_inference_graph_open_nautilus_button.setObjectName("live_stream_reader_inference_graph_open_nautilus_button")
        self.live_stream_reader_inference_graph_horizontal_layout.addWidget(self.live_stream_reader_inference_graph_open_nautilus_button)
        self.live_stream_reader_inference_graph_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_inference_graph_status.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_inference_graph_status.setObjectName("live_stream_reader_inference_graph_status")
        self.live_stream_reader_inference_graph_horizontal_layout.addWidget(self.live_stream_reader_inference_graph_status)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_inference_graph_horizontal_layout.addItem(spacerItem13)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_inference_graph_horizontal_layout)
        self.live_stream_reader_labels_path_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_labels_path_horizontal_layout.setObjectName("live_stream_reader_labels_path_horizontal_layout")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_labels_path_horizontal_layout.addItem(spacerItem14)
        self.live_stream_reader_label_path_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_label_path_title.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_label_path_title.setObjectName("live_stream_reader_label_path_title")
        self.live_stream_reader_labels_path_horizontal_layout.addWidget(self.live_stream_reader_label_path_title)
        self.live_stream_reader_label_path_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.live_stream_reader_label_path_field.setMinimumSize(QtCore.QSize(400, 0))
        self.live_stream_reader_label_path_field.setObjectName("live_stream_reader_label_path_field")
        self.live_stream_reader_labels_path_horizontal_layout.addWidget(self.live_stream_reader_label_path_field)
        self.live_stream_reader_label_path_open_nautilus_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.live_stream_reader_label_path_open_nautilus_button.setMinimumSize(QtCore.QSize(125, 0))
        self.live_stream_reader_label_path_open_nautilus_button.setObjectName("live_stream_reader_label_path_open_nautilus_button")
        self.live_stream_reader_labels_path_horizontal_layout.addWidget(self.live_stream_reader_label_path_open_nautilus_button)
        self.live_stream_reader_label_path_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.live_stream_reader_label_path_status.setMinimumSize(QtCore.QSize(150, 0))
        self.live_stream_reader_label_path_status.setObjectName("live_stream_reader_label_path_status")
        self.live_stream_reader_labels_path_horizontal_layout.addWidget(self.live_stream_reader_label_path_status)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_labels_path_horizontal_layout.addItem(spacerItem15)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_labels_path_horizontal_layout)
        self.live_stream_reader_start_stop_buttons_horizontal_layout = QtWidgets.QHBoxLayout()
        self.live_stream_reader_start_stop_buttons_horizontal_layout.setObjectName("live_stream_reader_start_stop_buttons_horizontal_layout")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_start_stop_buttons_horizontal_layout.addItem(spacerItem16)
        self.live_stream_reader_start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.live_stream_reader_start_button.setMinimumSize(QtCore.QSize(125, 0))
        self.live_stream_reader_start_button.setObjectName("live_stream_reader_start_button")
        self.live_stream_reader_start_stop_buttons_horizontal_layout.addWidget(self.live_stream_reader_start_button)
        self.live_stream_reader_stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.live_stream_reader_stop_button.setMinimumSize(QtCore.QSize(125, 0))
        self.live_stream_reader_stop_button.setObjectName("live_stream_reader_stop_button")
        self.live_stream_reader_start_stop_buttons_horizontal_layout.addWidget(self.live_stream_reader_stop_button)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.live_stream_reader_start_stop_buttons_horizontal_layout.addItem(spacerItem17)
        self.live_stream_reader_vertical_layout.addLayout(self.live_stream_reader_start_stop_buttons_horizontal_layout)
        self.readers_horizontal_layout.addLayout(self.live_stream_reader_vertical_layout)
        self.verticalLayout.addLayout(self.readers_horizontal_layout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.video_widget_vertical_layout = QtWidgets.QHBoxLayout()
        self.video_widget_vertical_layout.setObjectName("video_widget_vertical_layout")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.video_widget_vertical_layout.addItem(spacerItem18)
        self.stream_video_widget = QVideoWidget(self.verticalLayoutWidget)
        self.stream_video_widget.setMinimumSize(QtCore.QSize(1080, 720))
        self.stream_video_widget.setObjectName("stream_video_widget")
        self.video_widget_vertical_layout.addWidget(self.stream_video_widget)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.video_widget_vertical_layout.addItem(spacerItem19)
        self.verticalLayout.addLayout(self.video_widget_vertical_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2937, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_reader_title.setText(_translate("MainWindow", "FIle Reader"))
        self.file_reader_status_label.setText(_translate("MainWindow", "Waiting for fields"))
        self.file_reader_file_path_field_title.setText(_translate("MainWindow", "File path to videos"))
        self.file_reader_file_path_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.file_reader_file_path_field_status_label.setText(_translate("MainWindow", "No Filepath"))
        self.file_reader_inference_path_title.setText(_translate("MainWindow", "Inference path"))
        self.file_reader_inference_path_open_nautlus_button.setText(_translate("MainWindow", "..."))
        self.file_reader_inference_path_status.setText(_translate("MainWindow", "No FIlepath"))
        self.file_reader_labels_title.setText(_translate("MainWindow", "Labels path"))
        self.file_reader_labels_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.file_reader_labels_status.setText(_translate("MainWindow", "No FIlepath"))
        self.file_reader_start_button.setText(_translate("MainWindow", "Start"))
        self.file_reader_stop_button.setText(_translate("MainWindow", "Stop"))
        self.live_stream_reader_title_label.setText(_translate("MainWindow", "LIve stream Reader"))
        self.live_stream_reader_status_label.setText(_translate("MainWindow", "Waiting for fields"))
        self.live_stream_reader_ip_field_title.setText(_translate("MainWindow", "Livestream IP"))
        self.live_stream_reader_ip_field_check_connection.setText(_translate("MainWindow", "Check "))
        self.live_stream_reader_ip_field_status.setText(_translate("MainWindow", "No connection"))
        self.live_stream_reader_recordings_title.setText(_translate("MainWindow", "Destination"))
        self.live_stream_reader_recordings_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.live_stream_reader_recordings_status.setText(_translate("MainWindow", "No Filepath"))
        self.live_stream_reader_inference_graph_title.setText(_translate("MainWindow", "inference graph "))
        self.live_stream_reader_inference_graph_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.live_stream_reader_inference_graph_status.setText(_translate("MainWindow", "No Filepath"))
        self.live_stream_reader_label_path_title.setText(_translate("MainWindow", "Labels path"))
        self.live_stream_reader_label_path_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.live_stream_reader_label_path_status.setText(_translate("MainWindow", "No FIlepath"))
        self.live_stream_reader_start_button.setText(_translate("MainWindow", "Start"))
        self.live_stream_reader_stop_button.setText(_translate("MainWindow", "Stop"))


from PyQt5.QtMultimediaWidgets import QVideoWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

