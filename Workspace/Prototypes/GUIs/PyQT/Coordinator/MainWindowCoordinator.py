from PyQt5 import QtWidgets
from Prototypes.GUIs.PyQT.Controller.MainWindowController import MainWindowController
from Prototypes.GUIs.PyQT.Coordinator.baseCoordinator import BaseCoordinator


class MainWindowCoordinator(BaseCoordinator):
    def go_to_main_window(self):
        main_window = QtWidgets.QMainWindow()
        main_window_controller = MainWindowController(self, main_window)
        self.set_view_controller(main_window_controller)
