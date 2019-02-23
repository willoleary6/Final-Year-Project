
from PyQt5.QtWidgets import (QApplication)
import sys
from Prototypes.GUIs.PyQT.Coordinator.videoWindowCoordinator import VideoWindowCoordinator
if __name__ == '__main__':
    app = QApplication(sys.argv)
    VideoWindowCoordinator().go_to_video_window()
    #player = videoWindow()
    #player.resize(1280, 960)
    #player.show()
    sys.exit(app.exec_())
