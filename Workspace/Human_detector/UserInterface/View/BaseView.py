from abc import abstractmethod


class BaseView:

    @abstractmethod
    def __update_geometry(self):
        pass

    @abstractmethod
    def __percentage_of_height(self, percentage):
        pass

    @abstractmethod
    def __percentage_of_width(self, percentage):
        pass

    @abstractmethod
    def resizeEvent(self, event):
        pass

    @abstractmethod
    def __set_text_and_icons(self, event):
        pass
