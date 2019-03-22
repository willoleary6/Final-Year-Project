from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.View.TrainerWindowView import TrainerWindowView


class TrainerWindowController(QMainWindow, ViewController):

    def __init__(self, coordinator, parent=None):
        super(TrainerWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        self.__trainer_window_view = TrainerWindowView()

    def initialise_view(self):
        self.__trainer_window_view.show()
