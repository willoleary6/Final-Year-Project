# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/will/SourceCode/Final-Year-Project/Workspace/ObjectDetector/UserInterface/misc/Reader.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from Workspace.ObjectDetector.config import Config
from Workspace.ObjectDetector.UserInterface.View.BaseView import BaseView


class ReaderWindowView(QMainWindow, BaseView):
    def __init__(self, window_height=Config.READER_REVIEWER_WINDOW_HEIGHT,
                 window_width=Config.READER_REVIEWER_WINDOW_WIDTH):
        super(QMainWindow, self).__init__(parent=None)
        self.setObjectName("Reader")
        self.resize(window_width, window_height)
        self.setMinimumSize(QtCore.QSize(window_width, window_height))
        self.__window_height = window_height
        self.__window_width = window_width

        self.__central_widget = QtWidgets.QWidget(self)
        self.__central_widget.setObjectName("central_widget")

        self.__vertical_layout_widget = QtWidgets.QWidget(self.__central_widget)
        self.__vertical_layout_widget.setObjectName("__vertical_layout_widget")

        self.__main_layout = QtWidgets.QVBoxLayout(self.__vertical_layout_widget)
        self.__main_layout.setObjectName("main_layout")

        self.__readers_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__readers_horizontal_layout.setObjectName("readers_horizontal_layout")

        self.__saved_file_reader_vertical_layout = QtWidgets.QVBoxLayout()
        self.__saved_file_reader_vertical_layout.setObjectName("saved_file_reader_vertical_layout")

        self.__file_reader_title_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__file_reader_title_horizontal_layout.setObjectName("file_reader_title_horizontal_layout")

        self.__file_reader_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__file_reader_title.setObjectName("file_reader_title")

        self.__file_reader_title_horizontal_layout.addWidget(self.__file_reader_title)

        self.__saved_file_reader_vertical_layout.addLayout(self.__file_reader_title_horizontal_layout)

        self.__file_reader_status_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__file_reader_status_horizontal_layout.setObjectName("file_reader_status_horizontal_layout")

        self.__saved_file_reader_vertical_layout.addLayout(self.__file_reader_status_horizontal_layout)

        self.__file_reader_file_path_field_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__file_reader_file_path_field_horizontal_layout.setObjectName(
            "file_reader_file_path_field_horizontal_layout")

        self.__spacer_item = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3.7),  # margin - left
            self.__percentage_of_height(1),  # margin - top
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_file_path_field_horizontal_layout.addItem(self.__spacer_item)

        self.__file_reader_file_path_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_file_path_field_title.setObjectName("file_reader_file_path_field_title")

        self.__file_reader_file_path_field_horizontal_layout.addWidget(self.__file_reader_file_path_field_title)

        self.__file_reader_file_path_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__file_reader_file_path_field.setObjectName("file_reader_file_path_field")

        self.__file_reader_file_path_field_horizontal_layout.addWidget(self.__file_reader_file_path_field)

        self.__file_reader_file_path_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__file_reader_file_path_open_nautilus_button.setObjectName("file_reader_file_path_open_nautilus_button")

        self.__file_reader_file_path_field_horizontal_layout.addWidget(
            self.__file_reader_file_path_open_nautilus_button
        )

        self.__file_reader_file_path_field_status_label = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_file_path_field_status_label.setObjectName("file_reader_file_path_field_status_label")

        self.__file_reader_file_path_field_horizontal_layout.addWidget(self.__file_reader_file_path_field_status_label)

        self.__spacer_item_1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_file_path_field_horizontal_layout.addItem(self.__spacer_item_1)

        self.__saved_file_reader_vertical_layout.addLayout(self.__file_reader_file_path_field_horizontal_layout)

        self.__file_reader_inference_path_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__file_reader_inference_path_horizontal_layout.setObjectName(
            "file_reader_inference_path_horizontal_layout"
        )

        self.__spacer_item_2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_inference_path_horizontal_layout.addItem(self.__spacer_item_2)

        self.__file_reader_inference_path_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_inference_path_title.setObjectName("file_reader_inference_path_title")

        self.__file_reader_inference_path_horizontal_layout.addWidget(self.__file_reader_inference_path_title)

        self.__file_reader_inference_path_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__file_reader_inference_path_field.setObjectName("file_reader_inference_path_field")

        self.__file_reader_inference_path_horizontal_layout.addWidget(self.__file_reader_inference_path_field)

        self.__file_reader_inference_path_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__file_reader_inference_path_open_nautilus_button.setObjectName(
            "file_reader_inference_path_open_nautilus_button")

        self.__file_reader_inference_path_horizontal_layout.addWidget(
            self.__file_reader_inference_path_open_nautilus_button
        )

        self.__file_reader_inference_path_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_inference_path_status.setObjectName("file_reader_inference_path_status")

        self.__file_reader_inference_path_horizontal_layout.addWidget(self.__file_reader_inference_path_status)

        self.__spacer_item_3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_inference_path_horizontal_layout.addItem(self.__spacer_item_3)

        self.__saved_file_reader_vertical_layout.addLayout(self.__file_reader_inference_path_horizontal_layout)

        self.__file_reader_labels_path = QtWidgets.QHBoxLayout()
        self.__file_reader_labels_path.setObjectName("file_reader_labels_path")

        self.__spacer_item_4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_labels_path.addItem(self.__spacer_item_4)

        self.__file_reader_labels_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_labels_title.setObjectName("file_reader_labels_title")

        self.__file_reader_labels_path.addWidget(self.__file_reader_labels_title)

        self.__file_reader_labels_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__file_reader_labels_field.setObjectName("file_reader_labels_field")

        self.__file_reader_labels_path.addWidget(self.__file_reader_labels_field)

        self.__file_reader_labels_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__file_reader_labels_open_nautilus_button.setObjectName("file_reader_labels_open_nautilus_button")

        self.__file_reader_labels_path.addWidget(self.__file_reader_labels_open_nautilus_button)

        self.__file_reader_labels_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__file_reader_labels_status.setObjectName("file_reader_labels_status")

        self.__file_reader_labels_path.addWidget(self.__file_reader_labels_status)

        self.__spacer_item_5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_labels_path.addItem(self.__spacer_item_5)

        self.__saved_file_reader_vertical_layout.addLayout(self.__file_reader_labels_path)

        self.__file_reader_start_stop_buttons_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__file_reader_start_stop_buttons_horizontal_layout.setObjectName(
            "file_reader_start_stop_buttons_horizontal_layout")

        self.__spacer_item_6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_start_stop_buttons_horizontal_layout.addItem(self.__spacer_item_6)

        self.__file_reader_start_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__file_reader_start_button.setObjectName("file_reader_start_button")

        self.__file_reader_start_stop_buttons_horizontal_layout.addWidget(self.__file_reader_start_button)

        self.__file_reader_stop_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__file_reader_stop_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_stop_button.setObjectName("file_reader_stop_button")
        self.__file_reader_start_stop_buttons_horizontal_layout.addWidget(self.__file_reader_stop_button)

        self.__spacer_item_7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__file_reader_start_stop_buttons_horizontal_layout.addItem(self.__spacer_item_7)

        self.__saved_file_reader_vertical_layout.addLayout(self.__file_reader_start_stop_buttons_horizontal_layout)
        self.__readers_horizontal_layout.addLayout(self.__saved_file_reader_vertical_layout)

        self.__vertical_centre_line = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.__vertical_centre_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.__vertical_centre_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__vertical_centre_line.setObjectName("vertical_centre_line")

        self.__readers_horizontal_layout.addWidget(self.__vertical_centre_line)
        self.__live_stream_reader_vertical_layout = QtWidgets.QVBoxLayout()
        self.__live_stream_reader_vertical_layout.setObjectName("live_stream_reader_vertical_layout")

        self.__live_stream_reader_title_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_title_horizontal_layout.setObjectName("live_stream_reader_title_horizontal_layout")

        self.__live_stream_reader_title_label = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__live_stream_reader_title_label.setObjectName("live_stream_reader_title_label")

        self.__live_stream_reader_title_horizontal_layout.addWidget(self.__live_stream_reader_title_label)
        self.__live_stream_reader_vertical_layout.addLayout(self.__live_stream_reader_title_horizontal_layout)

        self.__live_stream_reader_status_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_status_horizontal_layout.setObjectName("live_stream_reader_status_horizontal_layout")

        self.__live_stream_reader_vertical_layout.addLayout(self.__live_stream_reader_status_horizontal_layout)

        self.__live_stream_reader_ip_field_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_ip_field_horizontal_layout.setObjectName(
            "live_stream_reader_ip_field_horizontal_layout")

        self.__spacer_item_8 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_ip_field_horizontal_layout.addItem(self.__spacer_item_8)

        self.__live_stream_reader_ip_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_ip_field_title.setObjectName("live_stream_reader_ip_field_title")

        self.__live_stream_reader_ip_field_horizontal_layout.addWidget(self.__live_stream_reader_ip_field_title)

        self.__live_stream_reader_ip_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__live_stream_reader_ip_field.setAlignment(QtCore.Qt.AlignCenter)
        self.__live_stream_reader_ip_field.setObjectName("live_stream_reader_ip_field")

        self.__live_stream_reader_ip_field_horizontal_layout.addWidget(self.__live_stream_reader_ip_field)

        self.__live_stream_reader_ip_field_check_connection_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__live_stream_reader_ip_field_check_connection_button.setObjectName(
            "live_stream_reader_ip_field_check_connection"
        )

        self.__live_stream_reader_ip_field_horizontal_layout.addWidget(
            self.__live_stream_reader_ip_field_check_connection_button
        )

        self.__live_stream_reader_ip_field_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_ip_field_status.setObjectName("live_stream_reader_ip_field_status")

        self.__live_stream_reader_ip_field_horizontal_layout.addWidget(self.__live_stream_reader_ip_field_status)

        self.__spacer_item_9 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_ip_field_horizontal_layout.addItem(self.__spacer_item_9)

        self.__live_stream_reader_vertical_layout.addLayout(self.__live_stream_reader_ip_field_horizontal_layout)

        self.__live_stream_reader_recordings_file_path_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_recordings_file_path_horizontal_layout.setObjectName(
            "live_stream_reader_recordings_file_path_horizontal_layout")

        self.__spacer_item_10 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_recordings_file_path_horizontal_layout.addItem(self.__spacer_item_10)

        self.__live_stream_reader_recordings_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_recordings_title.setObjectName("live_stream_reader_recordings_title")

        self.__live_stream_reader_recordings_file_path_horizontal_layout.addWidget(
            self.__live_stream_reader_recordings_title)

        self.__live_stream_reader_recordings_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__live_stream_reader_recordings_field.setObjectName("live_stream_reader_recordings_field")

        self.__live_stream_reader_recordings_file_path_horizontal_layout.addWidget(
            self.__live_stream_reader_recordings_field)

        self.__live_stream_reader_recordings_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__live_stream_reader_recordings_open_nautilus_button.setObjectName(
            "live_stream_reader_recordings_open_nautilus_button")

        self.__live_stream_reader_recordings_file_path_horizontal_layout.addWidget(
            self.__live_stream_reader_recordings_open_nautilus_button)

        self.__live_stream_reader_recordings_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_recordings_status.setObjectName("live_stream_reader_recordings_status")
        self.__live_stream_reader_recordings_file_path_horizontal_layout.addWidget(
            self.__live_stream_reader_recordings_status)

        self.__spacer_item_11 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )

        self.__live_stream_reader_recordings_file_path_horizontal_layout.addItem(self.__spacer_item_11)

        self.__live_stream_reader_vertical_layout.addLayout(
            self.__live_stream_reader_recordings_file_path_horizontal_layout)

        self.__live_stream_reader_inference_graph_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_inference_graph_horizontal_layout.setObjectName(
            "live_stream_reader_inference_graph_horizontal_layout")

        self.__spacer_item_12 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_inference_graph_horizontal_layout.addItem(self.__spacer_item_12)

        self.__live_stream_reader_inference_graph_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_inference_graph_title.setObjectName("live_stream_reader_inference_graph_title")

        self.__live_stream_reader_inference_graph_horizontal_layout.addWidget(
            self.__live_stream_reader_inference_graph_title)

        self.__live_stream_reader_inference_graph_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__live_stream_reader_inference_graph_field.setObjectName("live_stream_reader_inference_graph_field")
        self.__live_stream_reader_inference_graph_horizontal_layout.addWidget(
            self.__live_stream_reader_inference_graph_field)

        self.__live_stream_reader_inference_graph_open_nautilus_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__live_stream_reader_inference_graph_open_nautilus_button.setObjectName(
            "live_stream_reader_inference_graph_open_nautilus_button")
        self.__live_stream_reader_inference_graph_horizontal_layout.addWidget(
            self.__live_stream_reader_inference_graph_open_nautilus_button)

        self.__live_stream_reader_inference_graph_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_inference_graph_status.setObjectName("live_stream_reader_inference_graph_status")

        self.__live_stream_reader_inference_graph_horizontal_layout.addWidget(
            self.__live_stream_reader_inference_graph_status)
        self.__spacer_item_13 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_inference_graph_horizontal_layout.addItem(self.__spacer_item_13)
        self.__live_stream_reader_vertical_layout.addLayout(self.__live_stream_reader_inference_graph_horizontal_layout)

        self.__live_stream_reader_labels_path_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_labels_path_horizontal_layout.setObjectName(
            "live_stream_reader_labels_path_horizontal_layout")

        self.__spacer_item_14 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_labels_path_horizontal_layout.addItem(self.__spacer_item_14)

        self.__live_stream_reader_label_path_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_label_path_title.setObjectName("live_stream_reader_label_path_title")

        self.__live_stream_reader_labels_path_horizontal_layout.addWidget(self.__live_stream_reader_label_path_title)

        self.__live_stream_reader_label_path_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__live_stream_reader_label_path_field.setObjectName("live_stream_reader_label_path_field")
        self.__live_stream_reader_labels_path_horizontal_layout.addWidget(self.__live_stream_reader_label_path_field)

        self.__live_stream_reader_label_path_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__live_stream_reader_label_path_open_nautilus_button.setObjectName(
            "live_stream_reader_label_path_open_nautilus_button")
        self.__live_stream_reader_labels_path_horizontal_layout.addWidget(
            self.__live_stream_reader_label_path_open_nautilus_button)

        self.__live_stream_reader_label_path_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__live_stream_reader_label_path_status.setObjectName("live_stream_reader_label_path_status")
        self.__live_stream_reader_labels_path_horizontal_layout.addWidget(self.__live_stream_reader_label_path_status)

        self.__spacer_item_15 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_labels_path_horizontal_layout.addItem(self.__spacer_item_15)
        self.__live_stream_reader_vertical_layout.addLayout(self.__live_stream_reader_labels_path_horizontal_layout)

        self.__live_stream_reader_start_stop_buttons_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__live_stream_reader_start_stop_buttons_horizontal_layout.setObjectName(
            "live_stream_reader_start_stop_buttons_horizontal_layout")

        self.__spacer_item_16 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_start_stop_buttons_horizontal_layout.addItem(self.__spacer_item_16)

        self.__live_stream_reader_start_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__live_stream_reader_start_button.setObjectName("live_stream_reader_start_button")
        self.__live_stream_reader_start_stop_buttons_horizontal_layout.addWidget(self.__live_stream_reader_start_button)

        self.__live_stream_reader_stop_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__live_stream_reader_stop_button.setObjectName("live_stream_reader_stop_button")
        self.__live_stream_reader_start_stop_buttons_horizontal_layout.addWidget(self.__live_stream_reader_stop_button)

        self.__spacer_item_17 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__live_stream_reader_start_stop_buttons_horizontal_layout.addItem(self.__spacer_item_17)
        self.__live_stream_reader_vertical_layout.addLayout(
            self.__live_stream_reader_start_stop_buttons_horizontal_layout)

        self.__readers_horizontal_layout.addLayout(self.__live_stream_reader_vertical_layout)
        self.__main_layout.addLayout(self.__readers_horizontal_layout)

        self.__horizontal_centre_line = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.__horizontal_centre_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.__horizontal_centre_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__horizontal_centre_line.setObjectName("horizontal_centre_line")
        self.__main_layout.addWidget(self.__horizontal_centre_line)

        self.__frame_display_vertical_layout = QtWidgets.QHBoxLayout()
        self.__frame_display_vertical_layout.setObjectName("video_widget_vertical_layout")

        self.__spacer_item_18 = QtWidgets.QSpacerItem(
            0,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__frame_display_vertical_layout.addItem(self.__spacer_item_18)

        self.__frame_display = QtWidgets.QLabel(self) # QVideoWidget(self.__vertical_layout_widget)
        self.__frame_display.setObjectName("frame_display")
        # place holder image!
        image = QtGui.QPixmap(
            self.__percentage_of_width(95),  # margin - left
            self.__percentage_of_height(70),  # margin - top
        )
        self.__frame_display.setPixmap(image)
        self.__frame_display_vertical_layout.addWidget(self.__frame_display)


        self.__spacer_item_19 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )

        self.__frame_display_vertical_layout.addItem(self.__spacer_item_19)
        self.__main_layout.addLayout(self.__frame_display_vertical_layout)

        self.setCentralWidget(self.__central_widget)

        self.__menu_bar = QtWidgets.QMenuBar(self)
        self.__menu_bar.setObjectName("menubar")
        self.setMenuBar(self.__menu_bar)

        self.__status_bar = QtWidgets.QStatusBar(self)
        self.__status_bar.setObjectName("statusbar")
        self.setStatusBar(self.__status_bar)

        self.__set_text_and_icons()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.__update_geometry()

    def __set_text_and_icons(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.__file_reader_title.setText(_translate("MainWindow", "File Reader"))
        self.__file_reader_file_path_field_title.setText(_translate("MainWindow", "Directory of videos"))
        self.__file_reader_file_path_field.setPlaceholderText(
            _translate("MainWindow", "/home/will/SourceCode/Final-Year-Project/Workspace/ObjectDetector/test_videos"))
        self.__file_reader_file_path_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__file_reader_file_path_field_status_label.setText(_translate("MainWindow", "No File Path"))
        self.__file_reader_inference_path_title.setText(_translate("MainWindow", "Inference path (.pb)"))
        self.__file_reader_inference_path_field.setPlaceholderText(
            _translate("MainWindow",
                       "/Model/faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28/frozen_inference_graph.pb"
                       ))
        self.__file_reader_inference_path_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__file_reader_inference_path_status.setText(_translate("MainWindow", "No File Path"))
        self.__file_reader_labels_title.setText(_translate("MainWindow", "Labels Path (.pbtxt)"))
        self.__file_reader_labels_field.setPlaceholderText(
            _translate("MainWindow",
                       "/TensorFlowObjectDetectionCoinPrototype/training_resnet/object_detection.pbtxt\'"
                       ))
        self.__file_reader_labels_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__file_reader_labels_status.setText(_translate("MainWindow", "No File Path"))
        self.__file_reader_start_button.setText(_translate("MainWindow", "Start"))
        self.__file_reader_stop_button.setText(_translate("MainWindow", "Stop"))
        self.__live_stream_reader_title_label.setText(_translate("MainWindow", "Live stream Reader"))
        self.__live_stream_reader_ip_field_title.setText(_translate("MainWindow", "Live-stream Address"))
        self.__live_stream_reader_ip_field.setPlaceholderText(_translate("MainWindow", "192.168.0.56"))
        self.__live_stream_reader_ip_field_check_connection_button.setText(_translate("MainWindow", "Check "))
        self.__live_stream_reader_ip_field_status.setText(_translate("MainWindow", "No connection"))
        self.__live_stream_reader_recordings_title.setText(_translate("MainWindow", "Directory of Videos"))
        self.__live_stream_reader_recordings_field.setPlaceholderText(
            _translate("MainWindow", "/home/will/SourceCode/Final-Year-Project/Workspace/ObjectDetector/test_videos"))
        self.__live_stream_reader_recordings_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__live_stream_reader_recordings_status.setText(_translate("MainWindow", "No File Path"))
        self.__live_stream_reader_inference_graph_title.setText(_translate("MainWindow", "Inference Graph (.pb)"))
        self.__live_stream_reader_inference_graph_field.setPlaceholderText(
            _translate("MainWindow",
                       "/Model/faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28/frozen_inference_graph.pb"
                       ))
        self.__live_stream_reader_inference_graph_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__live_stream_reader_inference_graph_status.setText(_translate("MainWindow", "No File Path "))
        self.__live_stream_reader_label_path_title.setText(_translate("MainWindow", "Labels Path (.pbtxt)"))
        self.__live_stream_reader_label_path_field.setPlaceholderText(
            _translate("MainWindow",
                       "/TensorFlowObjectDetectionCoinPrototype/training_resnet/object_detection.pbtxt\'"
                       ))
        self.__live_stream_reader_label_path_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__live_stream_reader_label_path_status.setText(_translate("MainWindow", "No File Path"))
        self.__live_stream_reader_start_button.setText(_translate("MainWindow", "Start"))
        self.__live_stream_reader_stop_button.setText(_translate("MainWindow", "Stop"))

    # file reader getters

    def get_file_reader_file_path_field(self):
        return self.__file_reader_file_path_field

    def get_self_file_reader_file_path_open_nautilus_button(self):
        return self.__file_reader_file_path_open_nautilus_button

    def get_file_reader_file_path_field_status_label(self):
        return self.__file_reader_file_path_field_status_label

    def get_file_reader_inference_path_field(self):
        return self.__file_reader_inference_path_field

    def get_file_reader_inference_path_open_nautilus_button(self):
        return self.__file_reader_inference_path_open_nautilus_button

    def get_file_reader_inference_path_status(self):
        return self.__file_reader_inference_path_status

    def get_file_reader_labels_field(self):
        return self.__file_reader_labels_field

    def get_file_reader_labels_open_nautilus_button(self):
        return self.__file_reader_labels_open_nautilus_button

    def get_file_reader_labels_status(self):
        return self.__file_reader_labels_status

    def get_file_reader_start_button(self):
        return self.__file_reader_start_button

    def get_file_reader_stop_button(self):
        return self.__file_reader_stop_button

    # live stream getters

    def get_live_stream_reader_ip_field(self):
        return self.__live_stream_reader_ip_field

    def get_live_stream_reader_ip_field_check_connection_button(self):
        return self.__live_stream_reader_ip_field_check_connection_button

    def get_live_stream_reader_ip_field_status(self):
        return self.__live_stream_reader_ip_field_status

    def get_live_stream_reader_recordings_field(self):
        return self.__live_stream_reader_recordings_field

    def get_live_stream_reader_recordings_open_nautilus_button(self):
        return self.__live_stream_reader_recordings_open_nautilus_button

    def get_live_stream_reader_recordings_status(self):
        return self.__live_stream_reader_recordings_status

    def get_live_stream_reader_inference_graph_field(self):
        return self.__live_stream_reader_inference_graph_field

    def get_live_stream_reader_inference_graph_open_nautilus_button(self):
        return self.__live_stream_reader_inference_graph_open_nautilus_button

    def get_live_stream_reader_inference_graph_status(self):
        return self.__live_stream_reader_inference_graph_status

    def get_live_stream_reader_label_path_field(self):
        return self.__live_stream_reader_label_path_field

    def get_live_stream_reader_label_path_open_nautilus_button(self):
        return self.__live_stream_reader_label_path_open_nautilus_button

    def get_live_stream_reader_label_path_status(self):
        return self.__live_stream_reader_label_path_status

    def get_live_stream_reader_start_button(self):
        return self.__live_stream_reader_start_button

    def get_live_stream_reader_stop_button(self):
        return self.__live_stream_reader_stop_button

    # additional getters
    def get_frame_display(self):
        return self.__frame_display

    def __update_geometry(self):
        self.__main_layout.setContentsMargins(
            self.__percentage_of_width(1),  # margin - left
            self.__percentage_of_height(1),  # margin - top
            self.__percentage_of_height(0),  # height
            self.__percentage_of_width(0)  # width
        )
        self.__vertical_layout_widget.setGeometry(QtCore.QRect(
            self.__percentage_of_width(.925),  # margin - left
            self.__percentage_of_height(1),  # margin - top
            self.__percentage_of_width(99),  # width
            self.__percentage_of_height(99)  # height
        ))
        self.__file_reader_file_path_field_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0)
        ))
        self.__file_reader_file_path_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_file_path_open_nautilus_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_inference_path_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # margin - left
            self.__percentage_of_height(0)
        ))
        self.__file_reader_inference_path_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_labels_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_labels_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_inference_path_status.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_file_path_field_status_label.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_inference_path_open_nautilus_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_labels_open_nautilus_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_ip_field_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_ip_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_recordings_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_recordings_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_ip_field_check_connection_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_inference_graph_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_ip_field_status.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_recordings_open_nautilus_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_inference_graph_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_label_path_field.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(20),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_inference_graph_open_nautilus_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_recordings_status.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_inference_graph_status.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_label_path_title.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_label_path_open_nautilus_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_label_path_status.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__frame_display.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(75),  # width
            self.__percentage_of_height(37.5),  # height
        ))
        self.__menu_bar.setGeometry(QtCore.QRect(
            self.__percentage_of_width(0),  # margin-left
            self.__percentage_of_height(0),  # margin-top
            self.__percentage_of_width(100),
            22
        ))
        self.__live_stream_reader_stop_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__live_stream_reader_start_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_start_button.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(5),  # width
            self.__percentage_of_height(0),  # height
        ))
        self.__file_reader_labels_status.setMinimumSize(QtCore.QSize(
            self.__percentage_of_width(7.5),  # width
            self.__percentage_of_height(0),  # height
        ))

    def __percentage_of_height(self, percentage):
        return (percentage / 100) * self.geometry().height()

    def __percentage_of_width(self, percentage):
        return (percentage / 100) * self.geometry().width()

    def resizeEvent(self, event):
        self.__update_geometry()  # call your update method
        QtWidgets.QMainWindow.resizeEvent(self, event)

