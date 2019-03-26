# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/will/SourceCode/Final-Year-Project/Workspace/ObjectDetector/UserInterface/misc/trainer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.View.BaseView import BaseView
from Workspace.ObjectDetector.config import Config


class TrainerWindowView(QMainWindow, BaseView):

    def __init__(self, window_height=Config.TRAINER_WINDOW_HEIGHT,
                 window_width=Config.TRAINER_WINDOW_HEIGHT):
        super(QMainWindow, self).__init__(parent=None)
        self.setObjectName("MainWindow")
        self.resize(window_height, window_width)
        self.setMinimumSize(QtCore.QSize(window_height, window_width))
        self.__central_widget = QtWidgets.QWidget(self)
        self.__central_widget.setObjectName("__central_widget")
        self.__vertical_layout_widget = QtWidgets.QWidget(self.__central_widget)
        self.__vertical_layout_widget.setObjectName("__vertical_layout_widget")

        self.__trainer_main_layout = QtWidgets.QVBoxLayout(self.__vertical_layout_widget)
        self.__trainer_main_layout.setObjectName("__trainer_main_layout")

        self.__trainer_directory_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_directory_vertical_layout.setObjectName("__trainer_directory_vertical_layout")

        self.__trainer_title_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_title_vertical_layout.setObjectName("__trainer_title_vertical_layout")
        self.__trainer_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(20)
        self.__trainer_title.setFont(font)
        self.__trainer_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_title.setObjectName("__trainer_title")
        self.__trainer_title_vertical_layout.addWidget(self.__trainer_title)

        self.__trainer_directory_vertical_layout.addLayout(self.__trainer_title_vertical_layout)
        self.__trainer_directory_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.__trainer_directory_title.setFont(font)
        self.__trainer_directory_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_directory_title.setObjectName("__trainer_directory_title")
        self.__trainer_directory_vertical_layout.addWidget(self.__trainer_directory_title)

        self.line_7 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.__trainer_directory_vertical_layout.addWidget(self.line_7)
        self.__trainer_directory_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_directory_horizontal_layout.setObjectName("__trainer_directory_horizontal_layout")
        self.__spacer_item = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_directory_horizontal_layout.addItem(self.__spacer_item)

        self.__trainer_directory_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_directory_field_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_directory_field_title.setObjectName("__trainer_directory_field")
        self.__trainer_directory_horizontal_layout.addWidget(self.__trainer_directory_field_title)
        self.__trainer_directory_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        self.__trainer_directory_field.setObjectName("__trainer_directory_field")
        self.__trainer_directory_horizontal_layout.addWidget(self.__trainer_directory_field)

        self.__trainer_directory_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_directory_open_nautilus_button.setObjectName("__trainer_directory_open_nautilus_button")
        self.__trainer_directory_horizontal_layout.addWidget(self.__trainer_directory_open_nautilus_button)

        self.__trainer_directory_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_directory_status.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_directory_status.setObjectName("__trainer_directory_status")
        self.__trainer_directory_horizontal_layout.addWidget(self.__trainer_directory_status)

        self.__spacer_item_1 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_directory_horizontal_layout.addItem(self.__spacer_item_1)
        self.__trainer_directory_vertical_layout.addLayout(self.__trainer_directory_horizontal_layout)
        self.__trainer_main_layout.addLayout(self.__trainer_directory_vertical_layout)

        self.line_8 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.__trainer_main_layout.addWidget(self.line_8)
        self.__trainer_image_data_set_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_image_data_set_vertical_layout.setObjectName("__trainer_image_data_set_vertical_layout")
        self.__trainer_image_data_set_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.__trainer_image_data_set_title.setFont(font)
        self.__trainer_image_data_set_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_image_data_set_title.setObjectName("__trainer_image_data_set_title")
        self.__trainer_image_data_set_vertical_layout.addWidget(self.__trainer_image_data_set_title)

        self.line = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.__trainer_image_data_set_vertical_layout.addWidget(self.line)
        self.__trainer_image_data_set_directory_field_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_directory_field_horizontal_layout.setObjectName(
            "__trainer_image_data_set_directory_field_horizontal_layout"
        )
        self.__spacer_item_2 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_directory_field_horizontal_layout.addItem(self.__spacer_item_2)

        self.__trainer_image_data_set_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__trainer_image_data_set_field_title.sizePolicy().hasHeightForWidth())
        self.__trainer_image_data_set_field_title.setSizePolicy(sizePolicy)
        self.__trainer_image_data_set_field_title.setObjectName("__trainer_image_data_set_field_title")
        self.__trainer_image_data_set_directory_field_horizontal_layout.addWidget(
            self.__trainer_image_data_set_field_title)

        self.__trainer_image_data_set_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__trainer_image_data_set_field.sizePolicy().hasHeightForWidth())
        self.__trainer_image_data_set_field.setSizePolicy(sizePolicy)
        self.__trainer_image_data_set_field.setObjectName("__trainer_image_data_set_field")

        self.__trainer_image_data_set_directory_field_horizontal_layout.addWidget(self.__trainer_image_data_set_field)
        self.__trainer_image_data_set_field_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_image_data_set_field_open_nautilus_button.setObjectName(
            "__trainer_image_data_set_field_open_nautilus_button"
        )
        self.__trainer_image_data_set_directory_field_horizontal_layout.addWidget(
            self.__trainer_image_data_set_field_open_nautilus_button)
        self.__trainer_image_data_set_field_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_image_data_set_field_status.setObjectName("__trainer_image_data_set_field_status")
        self.__trainer_image_data_set_directory_field_horizontal_layout.addWidget(
            self.__trainer_image_data_set_field_status)
        self.__spacer_item_3 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_directory_field_horizontal_layout.addItem(self.__spacer_item_3)
        self.__trainer_image_data_set_vertical_layout.addLayout(
            self.__trainer_image_data_set_directory_field_horizontal_layout)

        self.__trainer_image_data_set_commit_to_training_directory_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_commit_to_training_directory_horizontal_layout.setObjectName(
            "__trainer_image_data_set_commit_to_training_directory_horizontal_layout"
        )
        self.__spacer_item_4 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_commit_to_training_directory_horizontal_layout.addItem(self.__spacer_item_4)
        self.__trainer_image_data_set_commit_to_training_directory_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__trainer_image_data_set_commit_to_training_directory_button.setObjectName(
            "__trainer_image_data_set_commit_to_training_directory_button")
        self.__trainer_image_data_set_commit_to_training_directory_horizontal_layout.addWidget(
            self.__trainer_image_data_set_commit_to_training_directory_button)
        self.__spacer_item_5 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_commit_to_training_directory_horizontal_layout.addItem(self.__spacer_item_5)
        self.__trainer_image_data_set_vertical_layout.addLayout(
            self.__trainer_image_data_set_commit_to_training_directory_horizontal_layout)

        self.line_6 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.__trainer_image_data_set_vertical_layout.addWidget(self.line_6)
        self.__trainer_image_data_set_checks_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_image_data_set_checks_vertical_layout.setObjectName(
            "__trainer_image_data_set_checks_vertical_layout"
        )
        self.__trainer_image_data_set_file_format_check_title_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_file_format_check_title_horizontal_layout.setObjectName(
            "__trainer_image_data_set_file_format_check_title_horizontal_layout"
        )

        self.__trainer_image_data_set_checks_title_label = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_checks_title_label.setFont(font)
        self.__trainer_image_data_set_checks_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_image_data_set_checks_title_label.setObjectName("__trainer_image_data_set_checks_title_label")
        self.__trainer_image_data_set_file_format_check_title_horizontal_layout.addWidget(
            self.__trainer_image_data_set_checks_title_label)
        self.__trainer_image_data_set_checks_vertical_layout.addLayout(
            self.__trainer_image_data_set_file_format_check_title_horizontal_layout)

        self.__trainer_image_data_set_file_format_check_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_file_format_check_horizontal_layout.setObjectName(
            "__trainer_image_data_set_file_format_check_horizontal_layout"
        )
        self.__spacer_item_6 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addItem(self.__spacer_item_6)

        self.__trainer_image_data_set_file_format_check_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_file_format_check_title.setFont(font)
        self.__trainer_image_data_set_file_format_check_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_file_format_check_title.setObjectName(
            "__trainer_image_data_set_file_format_check_title"
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_file_format_check_title)
        self.__spacer_item_7 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addItem(self.__spacer_item_7)
        self.__trainer_image_data_set_file_format_check_status = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_file_format_check_status.setFont(font)
        self.__trainer_image_data_set_file_format_check_status.setStyleSheet("")
        self.__trainer_image_data_set_file_format_check_status.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_file_format_check_status.setObjectName(
            "__trainer_image_data_set_file_format_check_status"
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_file_format_check_status)

        self.__spacer_item_8 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addItem(self.__spacer_item_8)
        self.__trainer_image_data_set_file_format_check_fix_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__trainer_image_data_set_file_format_check_fix_button.setObjectName(
            "__trainer_image_data_set_file_format_check_fix_button"
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_file_format_check_fix_button)
        self.__spacer_item_9 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_format_check_horizontal_layout.addItem(self.__spacer_item_9)
        self.__trainer_image_data_set_checks_vertical_layout.addLayout(
            self.__trainer_image_data_set_file_format_check_horizontal_layout)

        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.setObjectName(
            "__trainer_image_data_set_file_number_of_images_check_horizontal_layout"
        )
        self.__spacer_item_10 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addItem(self.__spacer_item_10)

        self.__trainer_image_data_set_number_of_images_check_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_number_of_images_check_title.setFont(font)
        self.__trainer_image_data_set_number_of_images_check_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_number_of_images_check_title.setObjectName(
            "__trainer_image_data_set_number_of_images_check_title"
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_number_of_images_check_title)

        self.__spacer_item_11 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addItem(self.__spacer_item_11)
        self.__trainer_image_data_set_file_number_of_images_check_status = QtWidgets.QLabel(
            self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_file_number_of_images_check_status.setFont(font)
        self.__trainer_image_data_set_file_number_of_images_check_status.setStyleSheet("")
        self.__trainer_image_data_set_file_number_of_images_check_status.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_file_number_of_images_check_status.setObjectName(
            "__trainer_image_data_set_file_number_of_images_check_status"
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_file_number_of_images_check_status)

        self.__spacer_item_12 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addItem(self.__spacer_item_12)
        self.__trainer_image_data_set_number_of_images_check_fix_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__trainer_image_data_set_number_of_images_check_fix_button.setObjectName(
            "__trainer_image_data_set_number_of_images_check_fix_button"
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_number_of_images_check_fix_button)
        self.__spacer_item_13 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout.addItem(self.__spacer_item_13)
        self.__trainer_image_data_set_checks_vertical_layout.addLayout(
            self.__trainer_image_data_set_file_number_of_images_check_horizontal_layout)

        self.__trainer_image_data_set_file_image_size_check_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.setObjectName(
            "__trainer_image_data_set_file_image_size_check_horizontal_layout"
        )
        self.__spacer_item_14 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addItem(self.__spacer_item_14)
        self.__trainer_image_data_set_image_size_check_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_image_size_check_title.setFont(font)
        self.__trainer_image_data_set_image_size_check_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_image_size_check_title.setObjectName(
            "__trainer_image_data_set_image_size_check_title"
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_image_size_check_title)
        self.__spacer_item_15 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addItem(self.__spacer_item_15)

        self.__trainer_image_data_set_image_size_check_status = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_image_size_check_status.setFont(font)
        self.__trainer_image_data_set_image_size_check_status.setStyleSheet("")
        self.__trainer_image_data_set_image_size_check_status.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_image_size_check_status.setObjectName(
            "__trainer_image_data_set_image_size_check_status"
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_image_size_check_status)

        self.__spacer_item_16 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addItem(self.__spacer_item_16)
        self.__trainer_image_data_set_image_size_check_fix_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_image_data_set_image_size_check_fix_button.setObjectName(
            "__trainer_image_data_set_image_size_check_fix_button"
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_image_size_check_fix_button)
        self.__spacer_item_17 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_image_size_check_horizontal_layout.addItem(self.__spacer_item_17)
        self.__trainer_image_data_set_checks_vertical_layout.addLayout(
            self.__trainer_image_data_set_file_image_size_check_horizontal_layout)

        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.setObjectName(
            "__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout"
        )
        self.__spacer_item_18 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addItem(self.__spacer_item_18)
        self.__trainer_image_data_set_corresponding_xml_files_check_title = QtWidgets.QLabel(
            self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_corresponding_xml_files_check_title.setFont(font)
        self.__trainer_image_data_set_corresponding_xml_files_check_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_corresponding_xml_files_check_title.setObjectName(
            "__trainer_image_data_set_corresponding_xml_files_check_title"
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_corresponding_xml_files_check_title)

        self.__spacer_item_19 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addItem(self.__spacer_item_19)
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status = QtWidgets.QLabel(
            self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setFont(font)
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setStyleSheet("")
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setObjectName(
            "__trainer_image_data_set_file_corresponding_xml_files_check_status"
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_file_corresponding_xml_files_check_status)

        self.__spacer_item_20 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addItem(self.__spacer_item_20)

        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button.setObjectName(
            "__trainer_image_data_set_corresponding_xml_files_check_fix_button"
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_corresponding_xml_files_check_fix_button)

        self.__spacer_item_21 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout.addItem(self.__spacer_item_21)
        self.__trainer_image_data_set_checks_vertical_layout.addLayout(
            self.__trainer_image_data_set_file_corresponding_xml_check_horizontal_layout)
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.setObjectName(
            "__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout"
        )

        self.__spacer_item_22 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addItem(self.__spacer_item_22)
        self.__trainer_image_data_set_xml_file_validity_check_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_xml_file_validity_check_title.setFont(font)
        self.__trainer_image_data_set_xml_file_validity_check_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_xml_file_validity_check_title.setObjectName(
            "__trainer_image_data_set_xml_file_validity_check_title"
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_xml_file_validity_check_title)

        self.__spacer_item_23 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addItem(self.__spacer_item_23)
        self.__trainer_image_data_set_file_xml_file_validity_check_status = QtWidgets.QLabel(
            self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setFont(font)
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setStyleSheet("")
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setObjectName(
            "__trainer_image_data_set_file_xml_file_validity_check_status"
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_file_xml_file_validity_check_status)

        self.__spacer_item_24 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addItem(self.__spacer_item_24)
        self.__trainer_image_data_set_xml_file_validity_check_fix_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__trainer_image_data_set_xml_file_validity_check_fix_button.setObjectName(
            "__trainer_image_data_set_xml_file_validity_check_fix_button"
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addWidget(
            self.__trainer_image_data_set_xml_file_validity_check_fix_button)

        self.__spacer_item_25 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout.addItem(self.__spacer_item_25)
        self.__trainer_image_data_set_checks_vertical_layout.addLayout(
            self.__trainer_image_data_set_file_xml_file_validity_check_horizontal_layout)
        self.__trainer_image_data_set_vertical_layout.addLayout(self.__trainer_image_data_set_checks_vertical_layout)
        self.line_3 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.__trainer_image_data_set_vertical_layout.addWidget(self.line_3)
        self.__trainer_image_data_set_split_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_image_data_set_split_vertical_layout.setObjectName(
            "__trainer_image_data_set_split_vertical_layout"
        )
        self.__trainer_image_data_set_split_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_set_split_title.setFont(font)
        self.__trainer_image_data_set_split_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_image_data_set_split_title.setObjectName("__trainer_image_data_set_split_title")
        self.__trainer_image_data_set_split_vertical_layout.addWidget(self.__trainer_image_data_set_split_title)
        self.__trainer_image_data_set_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_set_horizontal_layout.setObjectName("__trainer_image_data_set_horizontal_layout")

        self.__spacer_item_26 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_horizontal_layout.addItem(self.__spacer_item_26)
        self.__trainer_image_data_set_split_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.__trainer_image_data_set_split_field_title.setFont(font)
        self.__trainer_image_data_set_split_field_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.__trainer_image_data_set_split_field_title.setObjectName("__trainer_image_data_set_split_field_title")
        self.__trainer_image_data_set_horizontal_layout.addWidget(self.__trainer_image_data_set_split_field_title)
        self.__trainer_image_data_set_split_percentage_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)

        self.__trainer_image_data_set_split_percentage_field.setInputMask("")
        self.__trainer_image_data_set_split_percentage_field.setObjectName(
            "__trainer_image_data_set_split_percentage_field"
        )
        self.__trainer_image_data_set_horizontal_layout.addWidget(self.__trainer_image_data_set_split_percentage_field)

        self.__trainer_image_data_set_split_button = QtWidgets.QPushButton(self.__vertical_layout_widget)

        self.__trainer_image_data_set_split_button.setObjectName("__trainer_image_data_set_split_button")
        self.__trainer_image_data_set_horizontal_layout.addWidget(self.__trainer_image_data_set_split_button)

        self.__spacer_item_27 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_set_horizontal_layout.addItem(self.__spacer_item_27)
        self.__trainer_image_data_set_split_vertical_layout.addLayout(self.__trainer_image_data_set_horizontal_layout)
        self.__trainer_image_data_set_vertical_layout.addLayout(self.__trainer_image_data_set_split_vertical_layout)

        self.line_9 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.__trainer_image_data_set_vertical_layout.addWidget(self.line_9)
        self.__trainer_image_data_commit_to_tensorflow = QtWidgets.QVBoxLayout()
        self.__trainer_image_data_commit_to_tensorflow.setObjectName("__trainer_image_data_commit_to_tensorflow")
        self.__trainer_image_data_convert_to_tf_record_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.__trainer_image_data_convert_to_tf_record_title.setFont(font)
        self.__trainer_image_data_convert_to_tf_record_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_image_data_convert_to_tf_record_title.setObjectName("__trainer_image_data_convert_to_tf_record_title")
        self.__trainer_image_data_commit_to_tensorflow.addWidget(self.__trainer_image_data_convert_to_tf_record_title)
        self.__trainer_image_data_commit_to_tensorflow_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_image_data_commit_to_tensorflow_horizontal_layout.setObjectName(
            "__trainer_image_data_commit_to_tensorflow_horizontal_layout"
        )

        self.__spacer_item_28 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_commit_to_tensorflow_horizontal_layout.addItem(self.__spacer_item_28)
        self.__trainer_image_data_convert_to_tf_record_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_image_data_convert_to_tf_record_button.setObjectName(
            "__trainer_image_data_convert_to_tf_record_button"
        )
        self.__trainer_image_data_commit_to_tensorflow_horizontal_layout.addWidget(
            self.__trainer_image_data_convert_to_tf_record_button)
        self.__trainer_image_data_convert_to_tf_record_status = QtWidgets.QLabel(self.__vertical_layout_widget)

        self.__trainer_image_data_convert_to_tf_record_status.setObjectName(
            "__trainer_image_data_convert_to_tf_record_status"
        )
        self.__trainer_image_data_commit_to_tensorflow_horizontal_layout.addWidget(
            self.__trainer_image_data_convert_to_tf_record_status)

        self.__spacer_item_29 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_image_data_commit_to_tensorflow_horizontal_layout.addItem(self.__spacer_item_29)
        self.__trainer_image_data_commit_to_tensorflow.addLayout(
            self.__trainer_image_data_commit_to_tensorflow_horizontal_layout)
        self.__trainer_image_data_set_vertical_layout.addLayout(self.__trainer_image_data_commit_to_tensorflow)
        self.__trainer_main_layout.addLayout(self.__trainer_image_data_set_vertical_layout)

        self.line_5 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.__trainer_main_layout.addWidget(self.line_5)
        self.__trainer_model_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_model_vertical_layout.setObjectName("__trainer_model_vertical_layout")
        self.__trainer_model_selection_title = QtWidgets.QLabel(self.__vertical_layout_widget)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.__trainer_model_selection_title.setFont(font)
        self.__trainer_model_selection_title.setAlignment(QtCore.Qt.AlignCenter)
        self.__trainer_model_selection_title.setObjectName("__trainer_model_selection_title")
        self.__trainer_model_vertical_layout.addWidget(self.__trainer_model_selection_title)
        self.__trainer_field_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_field_horizontal_layout.setObjectName("__trainer_field_horizontal_layout")

        self.__spacer_item_30 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_field_horizontal_layout.addItem(self.__spacer_item_30)
        self.__trainer_model_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_model_field_title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.__trainer_model_field_title.setObjectName("__trainer_model_field_title")
        self.__trainer_field_horizontal_layout.addWidget(self.__trainer_model_field_title)
        self.__trainer_model_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)

        self.__trainer_model_field.setObjectName("__trainer_model_field")
        self.__trainer_field_horizontal_layout.addWidget(self.__trainer_model_field)
        self.__trainer_model_field_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_model_field_open_nautilus_button.setObjectName("__trainer_model_field_open_nautilus_button")
        self.__trainer_field_horizontal_layout.addWidget(self.__trainer_model_field_open_nautilus_button)
        self.__trainer_model_field_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_model_field_status.setObjectName("__trainer_model_field_status")
        self.__trainer_field_horizontal_layout.addWidget(self.__trainer_model_field_status)

        self.__spacer_item_31 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_field_horizontal_layout.addItem(self.__spacer_item_31)
        self.__trainer_model_vertical_layout.addLayout(self.__trainer_field_horizontal_layout)
        self.__trainer_config_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_config_horizontal_layout.setObjectName("__trainer_config_horizontal_layout")

        self.__spacer_item_32 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_config_horizontal_layout.addItem(self.__spacer_item_32)
        self.__trainer_config_field_title = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_config_field_title.setObjectName("__trainer_config_field_title")
        self.__trainer_config_horizontal_layout.addWidget(self.__trainer_config_field_title)
        self.__trainer_config_field = QtWidgets.QLineEdit(self.__vertical_layout_widget)

        self.__trainer_config_field.setObjectName("__trainer_config_field")
        self.__trainer_config_horizontal_layout.addWidget(self.__trainer_config_field)
        self.__trainer_config_field_open_nautilus_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_config_field_open_nautilus_button.setObjectName("__trainer_config_field_open_nautilus_button")
        self.__trainer_config_horizontal_layout.addWidget(self.__trainer_config_field_open_nautilus_button)
        self.__trainer_config_field_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_config_field_status.setObjectName("__trainer_config_field_status")
        self.__trainer_config_horizontal_layout.addWidget(self.__trainer_config_field_status)

        self.__spacer_item_33 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_config_horizontal_layout.addItem(self.__spacer_item_33)
        self.__trainer_model_vertical_layout.addLayout(self.__trainer_config_horizontal_layout)
        self.__trainer_model_commit_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_model_commit_horizontal_layout.setObjectName("__trainer_model_commit_horizontal_layout")

        self.__spacer_item_34 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_model_commit_horizontal_layout.addItem(self.__spacer_item_34)
        self.__trainer_model_commit_to_training_directory_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_model_commit_to_training_directory_button.setObjectName(
            "__trainer_model_commit_to_training_directory_button"
        )
        self.__trainer_model_commit_horizontal_layout.addWidget(
            self.__trainer_model_commit_to_training_directory_button)
        self.__trainer_model_commit_to_training_directory_status = QtWidgets.QLabel(self.__vertical_layout_widget)
        self.__trainer_model_commit_to_training_directory_status.setObjectName(
            "__trainer_model_commit_to_training_directory_status"
        )
        self.__trainer_model_commit_horizontal_layout.addWidget(
            self.__trainer_model_commit_to_training_directory_status)

        self.__spacer_item_35 = QtWidgets.QSpacerItem(
            self.__percentage_of_width(3),
            self.__percentage_of_height(1.5),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.__trainer_model_commit_horizontal_layout.addItem(self.__spacer_item_35)
        self.__trainer_model_vertical_layout.addLayout(self.__trainer_model_commit_horizontal_layout)
        self.__trainer_main_layout.addLayout(self.__trainer_model_vertical_layout)

        self.line_4 = QtWidgets.QFrame(self.__vertical_layout_widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.__trainer_main_layout.addWidget(self.line_4)
        self.__trainer_control_panel_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_control_panel_vertical_layout.setObjectName("__trainer_control_panel_vertical_layout")
        self.__trainer_control_panel_horizontal_layout = QtWidgets.QHBoxLayout()
        self.__trainer_control_panel_horizontal_layout.setObjectName("__trainer_control_panel_horizontal_layout")
        self.__trainer_control_panel_controls_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_control_panel_controls_vertical_layout.setObjectName(
            "__trainer_control_panel_controls_vertical_layout"
        )

        self.__trainer_control_panel_start_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_control_panel_start_button.setObjectName("__trainer_control_panel_start_button")
        self.__trainer_control_panel_controls_vertical_layout.addWidget(self.__trainer_control_panel_start_button)
        self.__trainer_control_panel_open_tensor_board_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        self.__trainer_control_panel_open_tensor_board_button.setObjectName(
            "__trainer_control_panel_open_tensor_board_button"
        )
        self.__trainer_control_panel_controls_vertical_layout.addWidget(
            self.__trainer_control_panel_open_tensor_board_button)

        #self.__trainer_control_panel_stop_button = QtWidgets.QPushButton(self.__vertical_layout_widget)
        #self.__trainer_control_panel_stop_button.setObjectName("__trainer_control_panel_stop_button")
        #self.__trainer_control_panel_controls_vertical_layout.addWidget(self.__trainer_control_panel_stop_button)
        self.__trainer_control_panel_export_inference_graph_button = QtWidgets.QPushButton(
            self.__vertical_layout_widget)
        self.__trainer_control_panel_export_inference_graph_button.setObjectName(
            "__trainer_control_panel_export_inference_graph_button"
        )
        self.__trainer_control_panel_controls_vertical_layout.addWidget(
            self.__trainer_control_panel_export_inference_graph_button)

        self.__trainer_control_panel_horizontal_layout.addLayout(self.__trainer_control_panel_controls_vertical_layout)
        self.__trainer_control_panel_output_vertical_layout = QtWidgets.QVBoxLayout()
        self.__trainer_control_panel_output_vertical_layout.setObjectName(
            "__trainer_control_panel_output_vertical_layout"
        )
        # self.__trainer_control_panel_output_area = QtWidgets.QTextEdit(self.__vertical_layout_widget)
        # self.__trainer_control_panel_output_area.setStyleSheet("background-color:black;\n"
        #                                                      "color:white;")
        # self.__trainer_control_panel_output_area.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        # self.__trainer_control_panel_output_area.setObjectName("__trainer_control_panel_output_area")
        # self.__trainer_control_panel_output_vertical_layout.addWidget(self.__trainer_control_panel_output_area)
        self.__trainer_control_panel_horizontal_layout.addLayout(self.__trainer_control_panel_output_vertical_layout)
        self.__trainer_control_panel_vertical_layout.addLayout(self.__trainer_control_panel_horizontal_layout)
        self.__trainer_main_layout.addLayout(self.__trainer_control_panel_vertical_layout)
        self.setCentralWidget(self.__central_widget)

        self.__set_text_and_icons()
        self.__update_geometry()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __set_text_and_icons(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.__trainer_title.setText(_translate("MainWindow", "Trainer"))
        self.__trainer_directory_title.setText(_translate("MainWindow", "Training Directory"))
        self.__trainer_directory_field_title.setText(_translate("MainWindow", "Training Directory"))
        self.__trainer_directory_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__trainer_directory_status.setText(_translate("MainWindow", "No Directory set"))
        self.__trainer_image_data_set_title.setText(_translate("MainWindow", "Image Dataset"))
        self.__trainer_image_data_set_field_title.setText(_translate("MainWindow", "Directory Of Image Dataset"))
        self.__trainer_image_data_set_field_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__trainer_image_data_set_field_status.setText(_translate("MainWindow", "No Directory Set"))
        self.__trainer_image_data_set_commit_to_training_directory_button.setText(
            _translate("MainWindow", "Commit Dataset to Training Directory"))
        self.__trainer_image_data_set_checks_title_label.setText(_translate("MainWindow", "Checking Dataset"))
        self.__trainer_image_data_set_file_format_check_title.setText(_translate("MainWindow", "File Format:"))
        self.__trainer_image_data_set_file_format_check_status.setText(_translate("MainWindow", "Waiting to start..."))
        self.__trainer_image_data_set_file_format_check_fix_button.setText(_translate("MainWindow", "Fix"))
        self.__trainer_image_data_set_number_of_images_check_title.setText(
            _translate("MainWindow", "Number Of Images:"))
        self.__trainer_image_data_set_file_number_of_images_check_status.setText(
            _translate("MainWindow", "Waiting for previous Check."))
        self.__trainer_image_data_set_number_of_images_check_fix_button.setText(_translate("MainWindow", "Fix"))
        self.__trainer_image_data_set_image_size_check_title.setText(_translate("MainWindow", "Image Size:"))
        self.__trainer_image_data_set_image_size_check_status.setText(
            _translate("MainWindow", "Waiting for previous Check."))
        self.__trainer_image_data_set_image_size_check_fix_button.setText(_translate("MainWindow", "Fix"))
        self.__trainer_image_data_set_corresponding_xml_files_check_title.setText(
            _translate("MainWindow", "Corresponding XML files:"))
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setText(
            _translate("MainWindow", "Waiting for previous Check."))
        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button.setText(_translate("MainWindow", "Fix"))
        self.__trainer_image_data_set_xml_file_validity_check_title.setText(
            _translate("MainWindow", "XML File Validity:"))
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setText(
            _translate("MainWindow", "Waiting for previous Check."))
        self.__trainer_image_data_set_xml_file_validity_check_fix_button.setText(_translate("MainWindow", "Fix"))
        self.__trainer_image_data_set_split_title.setText(
            _translate("MainWindow", "Splitting the data set into test and train sets"))
        self.__trainer_image_data_set_split_field_title.setText(_translate("MainWindow", "Percentage of test images:"))
        self.__trainer_image_data_set_split_percentage_field.setText(_translate("MainWindow", "10"))
        self.__trainer_image_data_set_split_button.setText(_translate("MainWindow", "Split"))
        self.__trainer_image_data_convert_to_tf_record_title.setText(_translate("MainWindow", "Convert to TF Record"))
        self.__trainer_image_data_convert_to_tf_record_button.setText(_translate("MainWindow", "Convert"))
        self.__trainer_image_data_convert_to_tf_record_status.setText(
            _translate("MainWindow", "Waiting for Checks to Clear"))

        self.__trainer_model_selection_title.setText(_translate("MainWindow", "Model Selection"))
        self.__trainer_model_field_title.setText(_translate("MainWindow", "Model Directory:"))
        self.__trainer_model_field_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__trainer_model_field_status.setText(_translate("MainWindow", "No Directory Set"))
        self.__trainer_config_field_title.setText(_translate("MainWindow", "Model Config File:"))
        self.__trainer_config_field_open_nautilus_button.setText(_translate("MainWindow", "..."))
        self.__trainer_config_field_status.setText(_translate("MainWindow", "No File Path Set"))
        self.__trainer_model_commit_to_training_directory_button.setText(_translate("MainWindow", "Commit Model"))
        self.__trainer_model_commit_to_training_directory_status.setText(_translate("MainWindow", "Waiting for models"))
        self.__trainer_control_panel_start_button.setText(_translate("MainWindow", "Start Training"))
       # self.__trainer_control_panel_start_button.s(QtCore.Qt.AlignCenter)
        self.__trainer_control_panel_open_tensor_board_button.setText(_translate("MainWindow", "Open Tensorboard"))
        #self.__trainer_control_panel_stop_button.setText(_translate("MainWindow", "Stop Training"))
        self.__trainer_control_panel_export_inference_graph_button.setText(
            _translate("MainWindow", "Export Inference Graph"))
        #self.__trainer_control_panel_output_area.setPlaceholderText(_translate("MainWindow", "Waiting to start....."))

    # training directory
    def get_trainer_directory_title(self):
        return self.__trainer_directory_title

    def get_trainer_directory_title(self):
        return self.__trainer_directory_title

    def get_trainer_directory_field_title(self):
        return self.__trainer_directory_field_title

    def get_trainer_directory_field(self):
        return self.__trainer_directory_field

    def get_trainer_directory_open_nautilus_button(self):
        return self.__trainer_directory_open_nautilus_button

    def get_trainer_directory_status(self):
        return self.__trainer_directory_status

    # image dataset location
    def get_trainer_image_data_set_title(self):
        return self.__trainer_image_data_set_title

    def get_trainer_image_data_set_field_open_nautilus_button(self):
        return self.__trainer_image_data_set_field_open_nautilus_button

    def get_trainer_image_data_set_field_status(self):
        return self.__trainer_image_data_set_field_status

    def get_trainer_image_data_set_field_title(self):
        return self.__trainer_image_data_set_field_title

    def get_trainer_image_data_set_field(self):
        return self.__trainer_image_data_set_field

    def get_trainer_image_data_set_commit_to_training_directory_button(self):
        return self.__trainer_image_data_set_commit_to_training_directory_button

    # checks
    def get_trainer_image_data_set_checks_title_label(self):
        return self.__trainer_image_data_set_checks_title_label

    def get_trainer_image_data_set_file_format_check_title(self):
        return self.__trainer_image_data_set_file_format_check_title

    def get_trainer_image_data_set_file_format_check_status(self):
        return self.__trainer_image_data_set_file_format_check_status

    def get_trainer_image_data_set_file_format_check_fix_button(self):
        return self.__trainer_image_data_set_file_format_check_fix_button

    def get_trainer_image_data_set_file_number_of_images_check_status(self):
        return self.__trainer_image_data_set_file_number_of_images_check_status

    def get_trainer_image_data_set_number_of_images_check_title(self):
        return self.__trainer_image_data_set_number_of_images_check_title

    def get_trainer_image_data_set_number_of_images_check_fix_button(self):
        return self.__trainer_image_data_set_number_of_images_check_fix_button

    def get_trainer_image_data_set_image_size_check_title(self):
        return self.__trainer_image_data_set_image_size_check_title

    def get_trainer_image_data_set_image_size_check_status(self):
        return self.__trainer_image_data_set_image_size_check_status

    def get_trainer_image_data_set_image_size_check_fix_button(self):
        return self.__trainer_image_data_set_image_size_check_fix_button

    def get_trainer_image_data_set_corresponding_xml_files_check_title(self):
        return self.__trainer_image_data_set_corresponding_xml_files_check_title

    def get_trainer_image_data_set_file_corresponding_xml_files_check_status(self):
        return self.__trainer_image_data_set_file_corresponding_xml_files_check_status

    def get_trainer_image_data_set_corresponding_xml_files_check_fix_button(self):
        return self.__trainer_image_data_set_corresponding_xml_files_check_fix_button

    def get_trainer_image_data_set_xml_file_validity_check_title(self):
        return self.__trainer_image_data_set_xml_file_validity_check_title

    def get_trainer_image_data_set_file_xml_file_validity_check_status(self):
        return self.__trainer_image_data_set_file_xml_file_validity_check_status

    def get_trainer_image_data_set_xml_file_validity_check_fix_button(self):
        return self.__trainer_image_data_set_xml_file_validity_check_fix_button

    def get_trainer_image_data_set_split_title(self):
        return self.__trainer_image_data_set_split_title

    def get_trainer_image_data_set_split_field_title(self):
        return self.__trainer_image_data_set_split_field_title

    def get_trainer_image_data_set_split_percentage_field(self):
        return self.__trainer_image_data_set_split_percentage_field

    def get_trainer_image_data_set_split_button(self):
        return self.__trainer_image_data_set_split_button

    def get_trainer_image_data_convert_to_tf_record_title(self):
        return self.__trainer_image_data_convert_to_tf_record_title

    def get_trainer_image_data_convert_to_tf_record_button(self):
        return self.__trainer_image_data_convert_to_tf_record_button

    def get_trainer_image_data_convert_to_tf_record_status(self):
        return self.__trainer_image_data_convert_to_tf_record_status

    def get_trainer_model_selection_title(self):
        return self.__trainer_model_selection_title

    def get_trainer_model_field_title(self):
        return self.__trainer_model_field_title

    def get_trainer_model_field_open_nautilus_button(self):
        return self.__trainer_model_field_open_nautilus_button

    def get_trainer_model_field_status(self):
        return self.__trainer_model_field_status

    def get_trainer_model_field(self):
        return self.__trainer_model_field

    def get_trainer_config_field_title(self):
        return self.__trainer_config_field_title

    def get_trainer_config_field_open_nautilus_button(self):
        return self.__trainer_config_field_open_nautilus_button

    def get_trainer_config_field_status(self):
        return self.__trainer_config_field_status

    def get_trainer_config_field(self):
        return self.__trainer_config_field

    def get_trainer_model_commit_to_training_directory_button(self):
        return self.__trainer_model_commit_to_training_directory_button

    def get_trainer_model_commit_to_training_directory_status(self):
        return self.__trainer_model_commit_to_training_directory_status

    def get_trainer_control_panel_start_button(self):
        return self.__trainer_control_panel_start_button

    def get_trainer_control_panel_open_tensor_board_button(self):
        return self.__trainer_control_panel_open_tensor_board_button

    #def get_trainer_control_panel_stop_button(self):
        #return self.__trainer_control_panel_stop_button

    def get_trainer_control_panel_export_inference_graph_button(self):
        return self.__trainer_control_panel_export_inference_graph_button

    # def get_trainer_control_panel_output_area(self):
        #return self.__trainer_control_panel_output_area

    def __update_geometry(self):
        self.__vertical_layout_widget.setGeometry(
            QtCore.QRect(
                self.__percentage_of_width(.925),  # margin - left
                self.__percentage_of_height(1),  # margin - top
                self.__percentage_of_width(99),  # width
                self.__percentage_of_height(99)  # height
            )
        )
        self.__trainer_main_layout.setContentsMargins(
            self.__percentage_of_width(0),
            self.__percentage_of_height(0),
            self.__percentage_of_height(0),
            self.__percentage_of_width(0)
        )
        self.__trainer_directory_field.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(52),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_field_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(15),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_field.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(52),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_checks_title_label.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(22),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_file_format_check_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(18.5),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_file_format_check_status.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(22),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_number_of_images_check_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(18.5),
                self.__percentage_of_height(0)
            ))
        self.__trainer_image_data_set_number_of_images_check_title.setSizeIncrement(
            QtCore.QSize(
                self.__percentage_of_width(0),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_file_number_of_images_check_status.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(22),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_image_size_check_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(18.5),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_image_size_check_title.setSizeIncrement(
            QtCore.QSize(
                self.__percentage_of_width(0),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_image_size_check_status.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(22),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_corresponding_xml_files_check_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(18.5),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_corresponding_xml_files_check_title.setSizeIncrement(
            QtCore.QSize(
                self.__percentage_of_width(0),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(22),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_xml_file_validity_check_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(18.5),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_xml_file_validity_check_title.setSizeIncrement(
            QtCore.QSize(
                self.__percentage_of_width(0),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(22),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_split_field_title.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(11),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_split_field_title.setSizeIncrement(
            QtCore.QSize(
                self.__percentage_of_width(0),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_split_percentage_field.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(52),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_set_split_button.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(11),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_image_data_convert_to_tf_record_status.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(11),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_model_field.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(52),
                self.__percentage_of_height(0)
            )
        )
        self.__trainer_config_field.setMinimumSize(
            QtCore.QSize(
                self.__percentage_of_width(52),
                self.__percentage_of_height(0)
            )
        )



    def __percentage_of_height(self, percentage):
        return (percentage / 100) * self.geometry().height()

    def __percentage_of_width(self, percentage):
        return (percentage / 100) * self.geometry().width()

    def resizeEvent(self, event):
        self.__update_geometry()  # call your update method
        QtWidgets.QMainWindow.resizeEvent(self, event)
