# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/will/SourceCode/Final-Year-Project/Workspace/Human_detector/UserInterface/misc/mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StreamlinedObjectDectector(object):
    def setupUi(self, StreamlinedObjectDectector):
        StreamlinedObjectDectector.setObjectName("StreamlinedObjectDectector")
        StreamlinedObjectDectector.resize(798, 596)
        self.centralwidget = QtWidgets.QWidget(StreamlinedObjectDectector)
        self.centralwidget.setObjectName("__central_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 70, 401, 411))
        self.verticalLayoutWidget.setObjectName("__base_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("__menu_buttons_layout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("__title_label")
        self.verticalLayout.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.reviewer_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reviewer_button.setObjectName("__reviewer_button")
        self.verticalLayout.addWidget(self.reviewer_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.reader_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reader_button.setObjectName("__reader_button")
        self.verticalLayout.addWidget(self.reader_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.trainer_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.trainer_button.setObjectName("__trainer_button")
        self.verticalLayout.addWidget(self.trainer_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.documentation_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.documentation_button.setObjectName("__documentation_button")
        self.verticalLayout.addWidget(self.documentation_button)
        StreamlinedObjectDectector.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StreamlinedObjectDectector)
        self.statusbar.setObjectName("statusbar")
        StreamlinedObjectDectector.setStatusBar(self.statusbar)

        self.retranslateUi(StreamlinedObjectDectector)
        QtCore.QMetaObject.connectSlotsByName(StreamlinedObjectDectector)

    def retranslateUi(self, StreamlinedObjectDectector):
        _translate = QtCore.QCoreApplication.translate
        StreamlinedObjectDectector.setWindowTitle(_translate("StreamlinedObjectDectector", "MainWindow"))
        self.title.setText(_translate("StreamlinedObjectDectector", "Streamlined Object Detector"))
        self.reviewer_button.setText(_translate("StreamlinedObjectDectector", "Reviewer"))
        self.reader_button.setText(_translate("StreamlinedObjectDectector", "Reader"))
        self.trainer_button.setText(_translate("StreamlinedObjectDectector", "Trainer"))
        self.documentation_button.setText(_translate("StreamlinedObjectDectector", "Documentation"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StreamlinedObjectDectector = QtWidgets.QMainWindow()
    ui = Ui_StreamlinedObjectDectector()
    ui.setupUi(StreamlinedObjectDectector)
    StreamlinedObjectDectector.show()
    sys.exit(app.exec_())

