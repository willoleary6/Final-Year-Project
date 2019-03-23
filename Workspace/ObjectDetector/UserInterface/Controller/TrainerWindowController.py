from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.View.TrainerWindowView import TrainerWindowView


class TrainerWindowController(QMainWindow, ViewController):

    def __init__(self, coordinator, parent=None):
        super(TrainerWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        self.__trainer_window_view = TrainerWindowView()
        self.__trainer_directory_field = self.__trainer_window_view.get_trainer_directory_field()
        self.__trainer_directory_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_directory_open_nautilus_button()
        self.__trainer_directory_status = self.__trainer_window_view.get_trainer_directory_status()
        self.__trainer_image_data_set_field_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_image_data_set_field_open_nautilus_button()
        self.__trainer_image_data_set_field_status = \
            self.__trainer_window_view.get_trainer_image_data_set_field_status()
        self.__trainer_image_data_set_field = self.__trainer_window_view.get_trainer_image_data_set_field()
        self.__trainer_image_data_set_commit_to_training_directory_button = \
            self.__trainer_window_view.get_trainer_image_data_set_commit_to_training_directory_button()
        self.__trainer_image_data_set_file_format_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_format_check_status()
        self.__trainer_image_data_set_file_format_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_file_format_check_fix_button()
        self.__trainer__image_data_set_file_number_of_images_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_number_of_images_check_status()
        self.__trainer_image_data_set_number_of_images_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_number_of_images_check_fix_button()
        self.__trainer_image_data_set_image_size_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_image_size_check_status()
        self.__trainer_image_data_set_image_size_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_image_size_check_fix_button()
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_corresponding_xml_files_check_status()
        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_corresponding_xml_files_check_fix_button()
        self.__trainer_image_data_set_file_xml_file_validity_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_xml_file_validity_check_status()
        self.__trainer_image_data_set_xml_file_validity_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_xml_file_validity_check_fix_button()
        self.__trainer_image_data_set_split_percentage_field = \
            self.__trainer_window_view.get_trainer_image_data_set_split_percentage_field()
        self.__trainer_image_data_set_split_button = \
            self.__trainer_window_view.get_trainer_image_data_set_split_button()
        self.__trainer_image_data_convert_to_tf_record_status = \
            self.__trainer_window_view.get_trainer_image_data_convert_to_tf_record_status()
        self.__trainer_model_field_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_model_field_open_nautilus_button()
        self.__trainer_model_field_status = self.__trainer_window_view.get_trainer_model_field_status()
        self.__trainer_model_field = self.__trainer_window_view.get_trainer_model_field()
        self.__trainer_config_field_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_config_field_open_nautilus_button()
        self.__trainer_config_field_status = self.__trainer_window_view.get_trainer_config_field_status()
        self.__trainer_config_field = self.__trainer_window_view.get_trainer_config_field()
        self.__trainer_model_commit_to_training_directory_button = \
            self.__trainer_window_view.get_trainer_model_commit_to_training_directory_button()
        self.__trainer_model_commit_to_training_directory_status = \
            self.__trainer_window_view.get_trainer_model_commit_to_training_directory_status()
        self.__trainer_control_panel_start_button = self.__trainer_window_view.get_trainer_control_panel_start_button()
        self.__trainer_control_panel_open_tensor_board_button = \
            self.__trainer_window_view.get_trainer_control_panel_open_tensor_board_button()
        self.__trainer_control_panel_stop_button = self.__trainer_window_view.get_trainer_control_panel_stop_button()
        self.__trainer_control_panel_export_inference_graph_button = \
            self.__trainer_window_view.get_trainer_control_panel_export_inference_graph_button()
        self.__trainer_control_panel_output_area = self.__trainer_window_view.get_trainer_control_panel_output_area()

    def initialise_view(self):
        self.__trainer_window_view.show()
