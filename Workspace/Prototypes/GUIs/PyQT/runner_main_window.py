
from PyQt5.QtWidgets import (QApplication)
import sys
from Prototypes.GUIs.PyQT.Coordinator.MainWindowCoordinator import MainWindowCoordinator
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindowCoordinator().go_to_trainer_window()
    sys.exit(app.exec_())
