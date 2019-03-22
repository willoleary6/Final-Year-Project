
from PyQt5.QtWidgets import (QApplication)
import sys
from Workspace.ObjectDetector.UserInterface.Coordinator.MainMenuWindowCoordinator import MainMenuWindowCoordinator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenuWindowCoordinator()
    main_menu.go_to_main_menu_window()
    sys.exit(app.exec_())

