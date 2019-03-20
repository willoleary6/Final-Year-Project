from Workspace.ObjectDetector.UserInterface.Controller.MainMenuWindowController import MainMenuWindowController
from Workspace.ObjectDetector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator
from Workspace.ObjectDetector.UserInterface.Coordinator.DetectionReviewerWindowCoordinator import \
    DetectionReviewerWindowCoordinator
from Workspace.ObjectDetector.UserInterface.Coordinator.ReaderWindowCoordinator import \
    ReaderWindowCoordinator


class MainMenuWindowCoordinator(BaseCoordinator):
    def go_to_main_menu_window(self):
        main_menu_controller = MainMenuWindowController(self)
        self.set_view_controller(main_menu_controller)

    @staticmethod
    def run_new_instance_of_reviewer():
        DetectionReviewerWindowCoordinator().go_to_detection_reviewer_window()

    @staticmethod
    def run_new_instance_of_reader():
        ReaderWindowCoordinator().go_to_reader_window()
