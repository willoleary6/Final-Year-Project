from Workspace.ObjectDetector.UserInterface.Controller.MainMenuWindowController import MainMenuWindowController
from Workspace.ObjectDetector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator
from Workspace.ObjectDetector.UserInterface.Coordinator.DetectionReviewerWindowCoordinator import \
    DetectionReviewerWindowCoordinator
from Workspace.ObjectDetector.UserInterface.Coordinator.ReaderWindowCoordinator import ReaderWindowCoordinator
from Workspace.ObjectDetector.UserInterface.Coordinator.TrainerWindowCoordinator import TrainerWindowCoordinator


class MainMenuWindowCoordinator(BaseCoordinator):
    def __init__(self):
        BaseCoordinator.__init__(self)
        self.detection_reviewer_coordinator = DetectionReviewerWindowCoordinator()
        self.reader_coordinator = ReaderWindowCoordinator()
        self.trainer_coordinator = TrainerWindowCoordinator()

    def go_to_main_menu_window(self):
        main_menu_controller = MainMenuWindowController(self)
        self.set_view_controller(main_menu_controller)

    def run_new_instance_of_reviewer(self):
        self.detection_reviewer_coordinator.go_to_detection_reviewer_window()

    def run_new_instance_of_reader(self):
        self.reader_coordinator.go_to_reader_window()

    def run_new_instance_of_trainer(self):
        self.trainer_coordinator.go_to_trainer_window()
