from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.View.MainMenuWindowView import MainMenuWindowView


class MainMenuWindowController(QMainWindow, ViewController):

    def __init__(self, coordinator, parent=None):
        super(MainMenuWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        # Window objects
        self.__main_menu_window_view = MainMenuWindowView()
        self.__main_menu_window_reviewer_button = self.__main_menu_window_view.get_reviewer_button()
        self.__main_menu_window_reader_button = self.__main_menu_window_view.get_reader_button()
        self.__main_menu_window_trainer_button = self.__main_menu_window_view.get_trainer_button()
        self.__main_menu_window_documentation_button = self.__main_menu_window_view.get_documentation_button()
        self.connect_ui_elements_to_methods()

    def connect_ui_elements_to_methods(self):
        self.__main_menu_window_reviewer_button.clicked.connect(self.go_to_review_screen)
        self.__main_menu_window_reader_button.clicked.connect(self.go_to_reader_screen)
        self.__main_menu_window_trainer_button.clicked.connect(self.go_to_trainer_screen)
        self.__main_menu_window_documentation_button.clicked.connect(self.go_to_documentation_screen)

    def initialise_view(self):
        self.__main_menu_window_view.show()

    def go_to_review_screen(self):
        self.__coordinator.run_new_instance_of_reviewer()

    def go_to_reader_screen(self):
        self.__coordinator.run_new_instance_of_reader()
        self.__main_menu_window_view.destroy()

    @staticmethod
    def go_to_trainer_screen():
        print("trainer")

    @staticmethod
    def go_to_documentation_screen():
        print("documentation")
