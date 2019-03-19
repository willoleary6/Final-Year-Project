from Workspace.ObjectDetector.UserInterface.Controller.MainMenuWindowController import MainMenuWindowController
from Workspace.ObjectDetector.UserInterface.Controller.DetectionReviewerWindowController import \
    DetectionReviewerWindowController
from Workspace.ObjectDetector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator
from PyQt5.QtWidgets import (QApplication)
import sys
from Workspace.ObjectDetector.UserInterface.Coordinator.DetectionReviewerWindowCoordinator import \
    DetectionReviewerWindowCoordinator


class MainMenuWindowCoordinator(BaseCoordinator):
    def go_to_main_menu_window(self):
        main_menu_controller = MainMenuWindowController(self)
        self.set_view_controller(main_menu_controller)

    def run_new_instance_of_reviewer(self):
        DetectionReviewerWindowCoordinator().go_to_detection_reviewer_window()
