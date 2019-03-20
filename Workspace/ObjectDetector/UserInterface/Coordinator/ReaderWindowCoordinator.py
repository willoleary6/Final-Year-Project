from Workspace.ObjectDetector.UserInterface.Controller.ReaderWindowController import ReaderWindowController
from Workspace.ObjectDetector.UserInterface.Coordinator.baseCoordinator import BaseCoordinator


class ReaderWindowCoordinator(BaseCoordinator):
    def go_to_reader_window(self):
        reader_controller = ReaderWindowController(self)
        self.set_view_controller(reader_controller)

