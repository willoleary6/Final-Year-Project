
from PyQt5.QtWidgets import (QApplication)
import sys
from Workspace.ObjectDetector.UserInterface.Coordinator.MainMenuWindowCoordinator import MainMenuWindowCoordinator
from Workspace.ObjectDetector.UserInterface.Coordinator.ReaderWindowCoordinator import ReaderWindowCoordinator
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #MainMenuWindowCoordinator().go_to_main_menu_window()
    ReaderWindowCoordinator().go_to_reader_window()
    sys.exit(app.exec_())

