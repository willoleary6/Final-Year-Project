from Workspace.ObjectDetector.UserInterface.Controller.DetectionReviewerWindowController import DetectionReviewerWindowController
from Workspace.ObjectDetector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator


class DetectionReviewerWindowCoordinator(BaseCoordinator):
    def go_to_detection_reviewer_window(self):
        detection_reviewer_controller = DetectionReviewerWindowController(self)
        self.set_view_controller(detection_reviewer_controller)

