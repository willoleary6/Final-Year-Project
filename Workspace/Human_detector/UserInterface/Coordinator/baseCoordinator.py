from Human_detector.UserInterface.Controller.viewController import ViewController


class BaseCoordinator:
    def __init__(self):
        self.__currentViewController = ViewController()

    def set_view_controller(self, controller):
        if controller is not None:
            controller.initialise_view()

        if self.__currentViewController is not None:
            self.__currentViewController.hide()

        self.__currentViewController = controller


