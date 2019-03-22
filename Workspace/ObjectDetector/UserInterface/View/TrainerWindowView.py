# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/will/SourceCode/Final-Year-Project/Workspace/ObjectDetector/UserInterface/misc/trainer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.View.BaseView import BaseView
from Workspace.ObjectDetector.config import Config


class TrainerWindowView(QMainWindow, BaseView):
    def __init__(self, window_height=Config.MAIN_MENU_WINDOW_HEIGHT,
                 window_width=Config.MAIN_MENU_WINDOW_WIDTH):
        super(QMainWindow, self).__init__(parent=None)
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 70, 67, 17))
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Trainer"))




