
from PyQt5.QtWidgets import (QApplication)
import sys
from Workspace.Human_detector.UserInterface.Coordinator.DetectionReviewerWindowCoordinator import MainWindowCoordinator
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindowCoordinator().go_to_main_window()
    sys.exit(app.exec_())
