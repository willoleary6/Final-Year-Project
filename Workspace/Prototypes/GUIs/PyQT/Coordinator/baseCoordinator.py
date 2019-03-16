from Prototypes.GUIs.PyQT.Controller.viewController import ViewController


class BaseCoordinator:
    def __init__(self):
        self.__currentViewController = ViewController()

    def set_view_controller(self, controller):
        if controller is not None:
            controller.initialise_media_player()

        if self.__currentViewController is not None:
            self.__currentViewController.hide()

        self.__currentViewController = controller


'''
package ui.coordinator;

import ui.controller.ViewController;

abstract class BaseCoordinator {

    private ViewController currentViewController;

    void set_view_controller(ViewController controller) {
        if (controller != null) {
            controller.show();
        }

        if (currentViewController != null) {
            currentViewController.hide();
        }

        currentViewController = controller;
    }
}

'''
