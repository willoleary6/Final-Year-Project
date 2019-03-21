import _thread
from functools import partial

from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from Workspace.ObjectDetector.UserInterface.Model.ReaderWindowModel import ReaderWindowModel
from Workspace.ObjectDetector.UserInterface.View.ReaderWindowView import ReaderWindowView
from Workspace.ObjectDetector.config import Config


class ReaderWindowController(QMainWindow, ViewController):
    __test_connection_to_livestream_signal = QtCore.pyqtSignal(object)

    def __init__(self, coordinator, parent=None):
        super(ReaderWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        # file reader
        self.__reader_window_view = ReaderWindowView()
        self.__reader_window_model = ReaderWindowModel()

        self.__file_reader_status_label = self.__reader_window_view.get_file_reader_status_label()

        self.__file_reader_file_path_field = self.__reader_window_view.get_file_reader_file_path_field()
        self.__file_reader_file_path_open_nautilus_button = \
            self.__reader_window_view.get_self_file_reader_file_path_open_nautilus_button()
        self.__file_path_field_status_label = self.__reader_window_view.get_file_reader_file_path_field_status_label()

        self.__file_reader_inference_path_field = self.__reader_window_view.get_file_reader_inference_path_field()
        self.__file_reader_inference_path_open_nautilus_button = \
            self.__reader_window_view.get_file_reader_inference_path_open_nautilus_button()
        self.__file_reader_inference_path_status = self.__reader_window_view.get_file_reader_inference_path_status()

        self.__file_reader_labels_field = self.__reader_window_view.get_file_reader_labels_field()
        self.__file_reader_labels_open_nautilus_button = \
            self.__reader_window_view.get_file_reader_labels_open_nautilus_button()
        self.__file_reader_labels_status = self.__reader_window_view.get_file_reader_labels_status()

        self.__file_reader_start_button = self.__reader_window_view.get_file_reader_start_button()
        self.__file_reader_stop_button = self.__reader_window_view.get_file_reader_stop_button()

        # live stream
        self.__live_stream_reader_status_label = self.__reader_window_view.get_live_stream_reader_status_label()
        self.__live_stream_reader_ip_field = self.__reader_window_view.get_live_stream_reader_ip_field()
        self.__live_stream_reader_ip_field_check_connection_button = \
            self.__reader_window_view.get_live_stream_reader_ip_field_check_connection_button()
        self.__live_stream_reader_ip_field_status = self.__reader_window_view.get_live_stream_reader_ip_field_status()

        self.__live_stream_reader_recordings_field = self.__reader_window_view.get_live_stream_reader_recordings_field()
        self.__live_stream_reader_recordings_open_nautilus_button = \
            self.__reader_window_view.get_live_stream_reader_recordings_open_nautilus_button()
        self.__live_stream_reader_recordings_status = \
            self.__reader_window_view.get_live_stream_reader_recordings_status()

        self.__live_stream_reader_inference_graph_field = \
            self.__reader_window_view.get_live_stream_reader_inference_graph_field()
        self.__live_stream_reader_inference_graph_open_nautilus_button = \
            self.__reader_window_view.get_live_stream_reader_inference_graph_open_nautilus_button()
        self.__live_stream_reader_inference_graph_status = \
            self.__reader_window_view.get_live_stream_reader_inference_graph_status()

        self.__live_stream_reader_label_path_field = self.__reader_window_view.get_live_stream_reader_label_path_field()
        self.__live_stream_reader_label_path_open_nautilus_button = \
            self.__reader_window_view.get_live_stream_reader_label_path_open_nautilus_button()
        self.__live_stream_reader_label_path_status = \
            self.__reader_window_view.get_live_stream_reader_label_path_status()

        self.__live_stream_reader_start_button = self.__reader_window_view.get_live_stream_reader_start_button()
        self.__live_stream_reader_stop_button = self.__reader_window_view.get_live_stream_reader_stop_button()

        # others
        self.__media_player = self.__reader_window_view.get_media_player()
        self.connect_ui_elements_to_methods()

        # self.toggle_live_stream_reader_functionality(True)
        # self.toggle_file_reader_functionality(True)

    def connect_ui_elements_to_methods(self):
        # button clicked events
        self.__file_reader_file_path_open_nautilus_button.clicked.connect(self.open_nautilus_for_directory)
        self.__file_reader_inference_path_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__file_reader_labels_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__file_reader_start_button.clicked.connect(self.file_reader_start_button_click_event)
        self.__file_reader_stop_button.clicked.connect(self.file_reader_stop_button_click_event)

        self.__live_stream_reader_ip_field_check_connection_button.clicked.connect(
            self.deploy_thread_to_test_connectivity_with_live_stream)
        self.__live_stream_reader_recordings_open_nautilus_button.clicked.connect(self.open_nautilus_for_directory)
        self.__live_stream_reader_inference_graph_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__live_stream_reader_label_path_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__live_stream_reader_start_button.clicked.connect(self.live_stream_reader_start_button_click_event)
        self.__live_stream_reader_stop_button.clicked.connect(self.live_stream_reader_stop_button_click_event)

        # fields changed event
        self.__file_reader_file_path_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__file_reader_file_path_field,
                self.__file_path_field_status_label,
                is_directory=True,
            )
        )
        self.__file_reader_inference_path_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__file_reader_inference_path_field,
                self.__file_reader_inference_path_status,
                is_directory=False,
                desired_extension=Config.INFERENCE_GRAPH_FILE_EXTENSION
            )
        )
        self.__file_reader_labels_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__file_reader_labels_field,
                self.__file_reader_labels_status,
                is_directory=False,
                desired_extension=Config.OBJECT_LABELS_FILE_EXTENSION
            )
        )

        #OBJECT_LABELS_FILE_EXTENSION

    def open_nautilus_for_directory(self):
        print("nautilus for directory")

    def open_nautilus_for_file(self):
        print("nautilus for file")

    def file_reader_start_button_click_event(self):
        print("file_reader_start_button_click_event ")
        self.toggle_live_stream_reader_functionality(True)

    def file_reader_stop_button_click_event(self):
        print("file_reader_stop_button_click_event ")
        self.toggle_live_stream_reader_functionality(False)

    def live_stream_reader_start_button_click_event(self):
        print("live_stream_start_button_click_event ")
        self.toggle_file_reader_functionality(True)

    def live_stream_reader_stop_button_click_event(self):
        print("live_stream_stop_button_click_event ")
        self.toggle_file_reader_functionality(False)

    def field_text_has_changed_update_status(self, field, status, is_directory, desired_extension):
        file_path_check = self.__reader_window_model.check_if_file_path_is_valid(field, is_directory, desired_extension)
        if file_path_check:
            self.update_status_label(status,
                                     "valid file path",
                                     "background-color: green; color: white"
                                     )
        else:
            self.update_status_label(status,
                                     "Invalid file path",
                                     "background-color: red; color: white"
                                     )

    def deploy_thread_to_test_connectivity_with_live_stream(self):
        try:
            _thread.start_new_thread(
                self.__reader_window_model.check_connection_with_live_stream,
                (
                    self.__test_connection_to_livestream_signal,
                    self.__live_stream_reader_ip_field.text()
                )
            )
        except Exception as e:
            print("Error: unable to start thread")
            print(e)
        self.update_live_stream_connection_status(
            (
                "checking....",
                ""
            )
        )
        self.__test_connection_to_livestream_signal.connect(self.update_live_stream_connection_status)

    def update_live_stream_connection_status(self, message):
        new_status, stylesheet = message
        self.update_status_label(
            self.__live_stream_reader_ip_field_status,
            new_status,
            stylesheet
        )

    @staticmethod
    def update_status_label(status_label, new_message, stylesheet):
        status_label.setText(new_message)
        status_label.setStyleSheet(stylesheet)

    def initialise_view(self):
        self.__reader_window_view.show()

    def toggle_live_stream_reader_functionality(self, toggle_value):
        self.__live_stream_reader_status_label.setDisabled(toggle_value)
        self.__live_stream_reader_ip_field.setDisabled(toggle_value)
        self.__live_stream_reader_ip_field_check_connection_button.setDisabled(toggle_value)
        self.__live_stream_reader_ip_field_status.setDisabled(toggle_value)
        self.__live_stream_reader_recordings_field.setDisabled(toggle_value)
        self.__live_stream_reader_recordings_open_nautilus_button.setDisabled(toggle_value)
        self.__live_stream_reader_recordings_status.setDisabled(toggle_value)
        self.__live_stream_reader_inference_graph_field.setDisabled(toggle_value)
        self.__live_stream_reader_inference_graph_open_nautilus_button.setDisabled(toggle_value)
        self.__live_stream_reader_inference_graph_status.setDisabled(toggle_value)
        self.__live_stream_reader_label_path_field.setDisabled(toggle_value)
        self.__live_stream_reader_label_path_open_nautilus_button.setDisabled(toggle_value)
        self.__live_stream_reader_label_path_status.setDisabled(toggle_value)
        self.__live_stream_reader_start_button.setDisabled(toggle_value)
        self.__live_stream_reader_stop_button.setDisabled(toggle_value)

    def toggle_file_reader_functionality(self, toggle_value):
        self.__file_reader_status_label.setDisabled(toggle_value)
        self.__file_reader_file_path_field.setDisabled(toggle_value)
        self.__file_reader_file_path_open_nautilus_button.setDisabled(toggle_value)
        self.__file_path_field_status_label.setDisabled(toggle_value)
        self.__file_reader_inference_path_field.setDisabled(toggle_value)
        self.__file_reader_inference_path_open_nautilus_button.setDisabled(toggle_value)
        self.__file_reader_inference_path_status.setDisabled(toggle_value)
        self.__file_reader_labels_field.setDisabled(toggle_value)
        self.__file_reader_labels_open_nautilus_button.setDisabled(toggle_value)
        self.__file_reader_labels_status.setDisabled(toggle_value)
        self.__file_reader_start_button.setDisabled(toggle_value)
        self.__file_reader_stop_button.setDisabled(toggle_value)
