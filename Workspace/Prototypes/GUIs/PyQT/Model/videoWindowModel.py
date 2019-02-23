from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QFileDialog


class videoWindowModel:

    def openFile(self, windowController):
        print('hello')
        fileName, _ = QFileDialog.getOpenFileName(windowController, "Open Movie", QDir.homePath())
        if fileName != '':
            # windowController.play_video(fileName)
            return fileName
        return None
