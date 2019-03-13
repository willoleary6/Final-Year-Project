from abc import abstractmethod


class ViewController:

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass
