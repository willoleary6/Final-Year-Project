import _thread
from functools import partial

from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui
from Workspace.ObjectDetector.UserInterface.Model.ReaderWindowModel import ReaderWindowModel
from Workspace.ObjectDetector.UserInterface.View.ReaderWindowView import ReaderWindowView
from Workspace.ObjectDetector.config import Config


class ReaderWindowController(QMainWindow, ViewController):
    __test_connection_to_live_stream_signal = QtCore.pyqtSignal(object)
    __get_file_path_from_nautilus_signal = QtCore.pyqtSignal(object)
    __update_frame_display_signal = QtCore.pyqtSignal(object)

    def __init__(self, coordinator, parent=None):
        super(ReaderWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        # file reader
        self.__reader_window_view = ReaderWindowView()
        self.__reader_window_model = ReaderWindowModel()

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
        self.__frame_display = self.__reader_window_view.get_frame_display()
        self.connect_ui_elements_to_methods()

        # setting both start buttons to disabled
        self.__live_stream_reader_start_button.setDisabled(True)
        self.__file_reader_start_button.setDisabled(True)



    def update_frame_display(self, image):
        self.__frame_display.setPixmap(image)

    def connect_ui_elements_to_methods(self):
        # button clicked events
        self.__file_reader_file_path_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__file_reader_file_path_field,
                is_directory=True,
            )
        )

        self.__file_reader_inference_path_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__file_reader_inference_path_field,
                is_directory=False,
            )
        )

        self.__file_reader_labels_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__file_reader_labels_field,
                is_directory=False,
            )
        )

        self.__file_reader_start_button.clicked.connect(self.file_reader_start_button_click_event)
        self.__file_reader_stop_button.clicked.connect(self.file_reader_stop_button_click_event)

        self.__live_stream_reader_ip_field_check_connection_button.clicked.connect(
            self.deploy_thread_to_test_connectivity_with_live_stream
        )
        self.__live_stream_reader_recordings_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__live_stream_reader_recordings_field,
                is_directory=True,
            )
        )

        self.__live_stream_reader_inference_graph_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__live_stream_reader_inference_graph_field,
                is_directory=False,
            )
        )
        self.__live_stream_reader_label_path_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__live_stream_reader_label_path_field,
                is_directory=False,
            )
        )

        self.__live_stream_reader_start_button.clicked.connect(self.live_stream_reader_start_button_click_event)
        self.__live_stream_reader_stop_button.clicked.connect(self.live_stream_reader_stop_button_click_event)

        # fields changed event
        self.__file_reader_file_path_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__file_reader_file_path_field,
                self.__file_path_field_status_label,
                True,  # is_directory
            )
        )
        self.__file_reader_inference_path_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__file_reader_inference_path_field,
                self.__file_reader_inference_path_status,
                False,  # is_directory
                desired_extension=Config.INFERENCE_GRAPH_FILE_EXTENSION
            )
        )
        self.__file_reader_labels_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__file_reader_labels_field,
                self.__file_reader_labels_status,
                False,  # is_directory
                desired_extension=Config.OBJECT_LABELS_FILE_EXTENSION
            )
        )

        # live_stream_files_changed
        self.__live_stream_reader_recordings_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__live_stream_reader_recordings_field,
                self.__live_stream_reader_recordings_status,
                True,  # is_directory
            )
        )

        self.__live_stream_reader_inference_graph_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__live_stream_reader_inference_graph_field,
                self.__live_stream_reader_inference_graph_status,
                False,  # is_directory
                desired_extension=Config.INFERENCE_GRAPH_FILE_EXTENSION
            )
        )

        self.__live_stream_reader_label_path_field.textChanged.connect(
            partial(
                self.field_text_has_changed_update_status,
                self.__live_stream_reader_label_path_field,
                self.__live_stream_reader_label_path_status,
                False,  # is_directory
                desired_extension=Config.OBJECT_LABELS_FILE_EXTENSION
            )
        )

    def open_nautilus(self, field_to_fill_in, is_directory):
        self.__get_file_path_from_nautilus_signal.connect(self.update_input_field)
        self.__reader_window_model.get_file_path_through_nautilus(
            self.__get_file_path_from_nautilus_signal,
            is_directory,
            field_to_fill_in
        )

    @staticmethod
    def update_input_field(message):
        field, message_to_insert = message
        field.setText(message_to_insert)

    def file_reader_start_button_click_event(self):
        self.toggle_live_stream_reader_functionality(True)
        self.__file_reader_start_button.setDisabled(True)
        videos_directory_path = self.__file_reader_file_path_field.text()
        inference_graph_path = self.__file_reader_inference_path_field.text()
        object_labels_path = self.__file_reader_labels_field.text()
        self.__reader_window_model.tensor_flow_import_object_detections(inference_graph_path)
        try:
            _thread.start_new_thread(
                self.__reader_window_model.file_reader,
                (
                    self.__update_frame_display_signal,
                    videos_directory_path,
                    object_labels_path
                )
            )
        except Exception as e:
            print("Error: unable to start thread")
            print(e)
        self.__update_frame_display_signal.connect(self.update_frame_display)

    def file_reader_stop_button_click_event(self):
        self.__reader_window_model.stop_reader_now()
        self.toggle_live_stream_reader_functionality(False)
        self.toggle_file_reader_functionality(False)
        self.__reader_window_model = ReaderWindowModel()

    def live_stream_reader_start_button_click_event(self):
        self.toggle_file_reader_functionality(True)
        self.__live_stream_reader_start_button.setDisabled(True)
        live_stream_address = self.__live_stream_reader_ip_field.text()
        videos_directory_path = self.__live_stream_reader_recordings_field.text()
        inference_graph_path = self.__live_stream_reader_inference_graph_field.text()
        object_labels_path = self.__live_stream_reader_label_path_field.text()
        self.__reader_window_model.tensor_flow_import_object_detections(inference_graph_path)
        try:
            _thread.start_new_thread(
                self.__reader_window_model.live_stream_reader,
                (
                    self.__update_frame_display_signal,
                    live_stream_address,
                    videos_directory_path,
                    object_labels_path
                )
            )
        except Exception as e:
            print("Error: unable to start thread")
            print(e)
        self.__update_frame_display_signal.connect(self.update_frame_display)

    def live_stream_reader_stop_button_click_event(self):
        self.__reader_window_model.stop_reader_now()
        self.toggle_file_reader_functionality(False)
        self.toggle_live_stream_reader_functionality(False)
        self.__reader_window_model = ReaderWindowModel()

    def field_text_has_changed_update_status(self, field, status, is_directory, desired_extension):
        file_path_check = self.__reader_window_model.check_if_file_path_is_valid(field, is_directory, desired_extension)
        if file_path_check:
            self.update_status_label(status,
                                     "valid file path",
                                     "background-color: green; color: white",
                                     True,
                                     )
        else:
            self.update_status_label(status,
                                     "Invalid file path",
                                     "background-color: red; color: white",
                                     False,
                                     )

    def deploy_thread_to_test_connectivity_with_live_stream(self):
        try:
            _thread.start_new_thread(
                self.__reader_window_model.check_connection_with_live_stream,
                (
                    self.__test_connection_to_live_stream_signal,
                    self.__live_stream_reader_ip_field.text()
                )
            )
        except Exception as e:
            print("Error: unable to start thread")
            print(e)
        self.update_live_stream_connection_status(
            (
                "checking....",
                "",
                False
            )
        )
        self.__test_connection_to_live_stream_signal.connect(self.update_live_stream_connection_status)

    def update_live_stream_connection_status(self, message):
        new_status, stylesheet, valid_to_run = message
        self.update_status_label(
            self.__live_stream_reader_ip_field_status,
            new_status,
            stylesheet,
            valid_to_run
        )

    def update_status_label(self, status_label, new_message, stylesheet, valid_to_run):
        status_label.setText(new_message)
        status_label.setStyleSheet(stylesheet)
        status_label.setProperty("valid_to_run", valid_to_run)

        self.check_if_start_buttons_are_ready_to_be_clicked()

    def check_if_start_buttons_are_ready_to_be_clicked(self):
        # checking if its time to enable the file reader start button
        if self.__file_path_field_status_label.property("valid_to_run") and \
                self.__file_reader_inference_path_status.property("valid_to_run") and \
                self.__file_reader_labels_status.property("valid_to_run"):
            self.__file_reader_start_button.setDisabled(False)
        else:
            self.__file_reader_start_button.setDisabled(True)
        # ok to run the live stream reader
        if self.__live_stream_reader_recordings_status.property("valid_to_run") and \
                self.__live_stream_reader_inference_graph_status.property("valid_to_run") and \
                self.__live_stream_reader_ip_field_status.property("valid_to_run") and \
                self.__live_stream_reader_label_path_status.property("valid_to_run"):
            self.__live_stream_reader_start_button.setDisabled(False)
        else:
            self.__live_stream_reader_start_button.setDisabled(True)

    def initialise_view(self):
        self.__reader_window_view.show()

    def toggle_live_stream_reader_functionality(self, toggle_value):
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
