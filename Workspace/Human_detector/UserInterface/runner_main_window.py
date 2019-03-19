
from PyQt5.QtWidgets import (QApplication)
import sys
from Workspace.Human_detector.UserInterface.Coordinator.DetectionReviewerWindowCoordinator import DetectionReviewerWindowCoordinator
if __name__ == '__main__':
    app = QApplication(sys.argv)
    DetectionReviewerWindowCoordinator().go_to_main_window()
    sys.exit(app.exec_())
