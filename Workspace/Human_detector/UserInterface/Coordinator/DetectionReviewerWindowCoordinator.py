from PyQt5 import QtWidgets
from Workspace.Human_detector.UserInterface.Controller.DetectionReviewerWindowController import DetectionReviewerWindowController
from Workspace.Human_detector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator


class DetectionReviewerWindowCoordinator(BaseCoordinator):
    def go_to_main_window(self):
        main_window_controller = DetectionReviewerWindowController(self)
        self.set_view_controller(main_window_controller)

