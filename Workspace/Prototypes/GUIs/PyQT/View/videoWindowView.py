from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QHBoxLayout, QLabel,
                             QSizePolicy, QSlider, QStyle, QVBoxLayout)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon


class videoWindowView(QMainWindow):

    def __init__(self, parent=None):
        super(videoWindowView, self).__init__(parent)
        self.setWindowTitle("PyQt Video Player Widget Example - pythonprogramminglanguage.com")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.video_widget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        #self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        #self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                                      QSizePolicy.Maximum)

        # Create a widget for window contents
        contents_widget = QWidget(self)
        self.setCentralWidget(contents_widget)

        # Create layouts to place inside widget
        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.playButton)
        control_layout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addLayout(control_layout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        contents_widget.setLayout(layout)

        #self.mediaPlayer.setVideoOutput(self.video_widget)
    def get_video_widget(self):
        return self.video_widget

    def get_media_player(self):
        return self.mediaPlayer

    def get_play_button(self):
        return self.playButton

    def get_position_slider(self):
        return self.positionSlider

    def get_error_label(self):
        return self.errorLabel

    def get_menu_bar(self):
        return self.menuBar()

