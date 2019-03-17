from PyQt5 import QtWidgets
from Human_detector.UserInterface.Controller.DetectionReviewerWindowController import DetectionReviewerWindowController
from Human_detector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator


class MainWindowCoordinator(BaseCoordinator):
    def go_to_main_window(self):
        main_window_controller = DetectionReviewerWindowController(self)
        self.set_view_controller(main_window_controller)

