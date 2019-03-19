# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/will/SourceCode/Final-Year-Project/Workspace/Human_detector/UserInterface/misc/mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Workspace.Human_detector.UserInterface.View.BaseView import BaseView
from Workspace.Human_detector.config import Config


class MainMenuWindowView(QMainWindow, BaseView):
    def __init__(self, window_height=Config.MAIN_MENU_WINDOW_HEIGHT,
                 window_width=Config.MAIN_MENU_WINDOW_WIDTH):
        super(QMainWindow, self).__init__(parent=None)
        self.setObjectName("StreamlinedObjectDectector")
        self.resize(window_width, window_height)

        self.setMinimumSize(QtCore.QSize(window_height, window_width))
        self.__central_widget = QtWidgets.QWidget(self)
        self.__central_widget.setObjectName("__central_widget")
        self.__base_layout = QtWidgets.QWidget(self.__central_widget)
        self.__base_layout.setObjectName("__base_layout")
        self.__menu_buttons_layout = QtWidgets.QVBoxLayout(self.__base_layout)
        self.__menu_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.__menu_buttons_layout.setObjectName("__menu_buttons_layout")
        self.__title_label = QtWidgets.QLabel(self.__base_layout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.__title_label.setFont(font)
        self.__title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__title_label.setObjectName("__title_label")
        self.__menu_buttons_layout.addWidget(self.__title_label)
        __title_reviewer_button_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                               QtWidgets.QSizePolicy.Expanding)
        self.__menu_buttons_layout.addItem(__title_reviewer_button_spacer)
        self.__reviewer_button = QtWidgets.QPushButton(self.__base_layout)
        self.__reviewer_button.setObjectName("__reviewer_button")
        self.__menu_buttons_layout.addWidget(self.__reviewer_button)
        __reviewer_reader_button_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                                QtWidgets.QSizePolicy.Expanding)
        self.__menu_buttons_layout.addItem(__reviewer_reader_button_spacer)
        self.__reader_button = QtWidgets.QPushButton(self.__base_layout)
        self.__reader_button.setObjectName("__reader_button")
        self.__menu_buttons_layout.addWidget(self.__reader_button)
        __reader_trainer_button_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                               QtWidgets.QSizePolicy.Expanding)
        self.__menu_buttons_layout.addItem(__reader_trainer_button_spacer)
        self.__trainer_button = QtWidgets.QPushButton(self.__base_layout)
        self.__trainer_button.setObjectName("__trainer_button")
        self.__menu_buttons_layout.addWidget(self.__trainer_button)
        __trainer_documentation_button_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                                      QtWidgets.QSizePolicy.Expanding)
        self.__menu_buttons_layout.addItem(__trainer_documentation_button_spacer)
        self.__documentation_button = QtWidgets.QPushButton(self.__base_layout)
        self.__documentation_button.setObjectName("__documentation_button")
        self.__menu_buttons_layout.addWidget(self.__documentation_button)
        self.setCentralWidget(self.__central_widget)

        self.__set_text_and_icons()
        self.__update_geometry()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __set_text_and_icons(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("StreamlinedObjectDectector", "Main Menu"))
        self.__title_label.setText(_translate("StreamlinedObjectDectector", "Streamlined Object Detector"))
        self.__reviewer_button.setText(_translate("StreamlinedObjectDectector", "Reviewer"))
        self.__reader_button.setText(_translate("StreamlinedObjectDectector", "Reader"))
        self.__trainer_button.setText(_translate("StreamlinedObjectDectector", "Trainer"))
        self.__documentation_button.setText(_translate("StreamlinedObjectDectector", "Documentation"))

    def __update_geometry(self):
        self.__base_layout.setGeometry(
            QtCore.QRect(
                self.__percentage_of_width(20),  # margin - left
                self.__percentage_of_height(5),  # margin - top
                self.__percentage_of_width(60),  # width
                self.__percentage_of_height(60)  # height
            )
        )

    def __percentage_of_height(self, percentage):
        return (percentage / 100) * self.geometry().height()

    def __percentage_of_width(self, percentage):
        return (percentage / 100) * self.geometry().width()

    def resizeEvent(self, event):
        self.__update_geometry()  # call your update method
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def get_reviewer_button(self):
        return self.__reviewer_button

    def get_reader_button(self):
        return self.__reader_button

    def get_trainer_button(self):
        return self.__trainer_button

    def get_documentation_button(self):
        return self.__documentation_button


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    StreamlinedObjectDectector = QtWidgets.QMainWindow()
    ui = MainMenuWindowView()
    ui.show()
    sys.exit(app.exec_())
