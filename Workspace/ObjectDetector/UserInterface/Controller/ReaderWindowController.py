from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.Model.ReaderWindowModel import ReaderWindowModel
from Workspace.ObjectDetector.UserInterface.View.ReaderWindowView import ReaderWindowView


class ReaderWindowController(QMainWindow, ViewController):

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
        self.__file_reader_file_path_open_nautilus_button.clicked.connect(self.open_nautilus_for_directory)
        self.__file_reader_file_path_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__file_reader_labels_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__file_reader_start_button.clicked.connect(self.file_reader_start_button_click_event)
        self.__file_reader_stop_button.clicked.connect(self.file_reader_stop_button_click_event)

        self.__live_stream_reader_ip_field_check_connection_button.clicked.connect(self.check_ip_connection)
        self.__live_stream_reader_recordings_open_nautilus_button.clicked.connect(self.open_nautilus_for_directory)
        self.__live_stream_reader_inference_graph_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__live_stream_reader_label_path_open_nautilus_button.clicked.connect(self.open_nautilus_for_file)
        self.__live_stream_reader_start_button.clicked.connect(self.live_stream_reader_start_button_click_event)
        self.__live_stream_reader_stop_button.clicked.connect(self.live_stream_reader_stop_button_click_event)

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

    def check_ip_connection(self):
        connection_test_result = self.__reader_window_model.check_connection_with_live_stream(
            self.__live_stream_reader_ip_field.text()
        )
        if connection_test_result:
            # TODO thread this bitch up !
            self.__live_stream_reader_ip_field_status.setText("Connection Established")
            self.__live_stream_reader_ip_field_status.setStyleSheet("background-color: green; color: white ")

        else:
            print("dirty boy!")

    def update_status_label(self, status_label, new_message, stylesheet):
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
