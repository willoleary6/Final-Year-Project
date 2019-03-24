from functools import partial

from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow

from Workspace.ObjectDetector.UserInterface.View.TrainerWindowView import TrainerWindowView
from Workspace.ObjectDetector.UserInterface.Model.TrainerWindowModel import TrainerWindowModel

import _thread
from functools import partial

from Workspace.ObjectDetector.UserInterface.Controller.viewController import ViewController
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from Workspace.ObjectDetector.config import Config


class TrainerWindowController(QMainWindow, ViewController):
    __get_file_path_from_nautilus_signal = QtCore.pyqtSignal(object)
    __get_label_img_update_signal = QtCore.pyqtSignal()

    def __init__(self, coordinator, parent=None):
        super(TrainerWindowController, self).__init__(parent)
        self.__coordinator = coordinator
        self.__trainer_window_view = TrainerWindowView()
        self.__trainer_window_model = TrainerWindowModel()

        self.__trainer_directory_title = self.__trainer_window_view.get_trainer_directory_title()
        self.__trainer_directory_field_title = self.__trainer_window_view.get_trainer_directory_field_title()
        self.__trainer_directory_field = self.__trainer_window_view.get_trainer_directory_field()
        self.__trainer_directory_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_directory_open_nautilus_button()
        self.__trainer_directory_status = self.__trainer_window_view.get_trainer_directory_status()

        self.__trainer_image_data_set_title = self.__trainer_window_view.get_trainer_image_data_set_title()
        self.__trainer_image_data_set_field_title = self.__trainer_window_view.get_trainer_image_data_set_field_title()
        self.__trainer_image_data_set_field_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_image_data_set_field_open_nautilus_button()
        self.__trainer_image_data_set_field_status = \
            self.__trainer_window_view.get_trainer_image_data_set_field_status()
        self.__trainer_image_data_set_field = self.__trainer_window_view.get_trainer_image_data_set_field()
        self.__trainer_image_data_set_commit_to_training_directory_button = \
            self.__trainer_window_view.get_trainer_image_data_set_commit_to_training_directory_button()

        self.__trainer_image_data_set_checks_title = \
            self.__trainer_window_view.get_trainer_image_data_set_checks_title_label()

        self.__trainer_image_data_set_file_format_check_title = \
            self.__trainer_window_view.get_trainer_image_data_set_file_format_check_title()
        self.__trainer_image_data_set_file_format_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_format_check_status()
        self.__trainer_image_data_set_file_format_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_file_format_check_fix_button()

        self.__trainer_image_data_set_number_of_images_check_title = \
            self.__trainer_window_view.get_trainer_image_data_set_number_of_images_check_title()
        self.__trainer__image_data_set_file_number_of_images_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_number_of_images_check_status()
        self.__trainer_image_data_set_number_of_images_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_number_of_images_check_fix_button()

        self.__trainer_image_data_set_image_size_check_title = \
            self.__trainer_window_view.get_trainer_image_data_set_image_size_check_title()
        self.__trainer_image_data_set_image_size_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_image_size_check_status()
        self.__trainer_image_data_set_image_size_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_image_size_check_fix_button()

        self.__trainer_image_data_set_corresponding_xml_files_check_title = \
            self.__trainer_window_view.get_trainer_image_data_set_corresponding_xml_files_check_title()
        self.__trainer_image_data_set_file_corresponding_xml_files_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_corresponding_xml_files_check_status()
        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_corresponding_xml_files_check_fix_button()

        self.__trainer_image_data_set_xml_file_validity_check_title = \
            self.__trainer_window_view.get_trainer_image_data_set_xml_file_validity_check_title()
        self.__trainer_image_data_set_file_xml_file_validity_check_status = \
            self.__trainer_window_view.get_trainer_image_data_set_file_xml_file_validity_check_status()
        self.__trainer_image_data_set_xml_file_validity_check_fix_button = \
            self.__trainer_window_view.get_trainer_image_data_set_xml_file_validity_check_fix_button()

        self.__trainer_image_data_set_split_title = \
            self.__trainer_window_view.get_trainer_image_data_set_split_title()
        self.__trainer_image_data_set_split_field_title = \
            self.__trainer_window_view.get_trainer_image_data_set_split_field_title()
        self.__trainer_image_data_set_split_percentage_field = \
            self.__trainer_window_view.get_trainer_image_data_set_split_percentage_field()
        self.__trainer_image_data_set_split_button = \
            self.__trainer_window_view.get_trainer_image_data_set_split_button()

        self.__trainer_image_data_convert_to_tf_record_title = \
            self.__trainer_window_view.get_trainer_image_data_convert_to_tf_record_title()
        self.__trainer_image_data_convert_to_tf_record_button = \
            self.__trainer_window_view.get_trainer_image_data_convert_to_tf_record_button()
        self.__trainer_image_data_convert_to_tf_record_status = \
            self.__trainer_window_view.get_trainer_image_data_convert_to_tf_record_status()

        self.__trainer_model_selection_title = \
            self.__trainer_window_view.get_trainer_model_selection_title()
        self.__trainer_model_field_title = \
            self.__trainer_window_view.get_trainer_model_field_title()
        self.__trainer_model_field = self.__trainer_window_view.get_trainer_model_field()
        self.__trainer_model_field_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_model_field_open_nautilus_button()
        self.__trainer_model_field_status = self.__trainer_window_view.get_trainer_model_field_status()

        self.__trainer_config_field_open_nautilus_button = \
            self.__trainer_window_view.get_trainer_config_field_open_nautilus_button()

        self.__trainer_config_field_title = self.__trainer_window_view.get_trainer_config_field_title()
        self.__trainer_config_field = self.__trainer_window_view.get_trainer_config_field()
        self.__trainer_config_field_status = self.__trainer_window_view.get_trainer_config_field_status()
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

        # self.toggle_training_directory_functionality(True)
        self.toggle_image_fields_functionality(True)
        self.toggle_image_data_set_checks_functionality(True)
        self.toggle_split_data_set_functionality(True)
        self.toggle_convert_to_tf_record_functionality(True)
        self.toggle_trainer_model_selection_functionality(True)
        self.toggle_control_panel_functionality(True)
        self.connect_ui_elements_to_methods()

        # initialising variables
        self.__directory_of_image_data_set = ''
        self.__currently_check_image_data_set = False

        self.__trainer_directory_field.setText('/home/will/Documents/training_test')
        self.__trainer_image_data_set_field.setText('/home/will/Documents/Stanford40_JPEGImages')
        #self.__trainer_image_data_set_field.setText('/home/will/Documents/empty')
        self.__trainer_image_data_set_commit_to_training_directory_button.click()

    def connect_ui_elements_to_methods(self):
        # self.__trainer_directory_field
        # self.__trainer_directory_status
        # button clicks
        self.__trainer_directory_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__trainer_directory_field,
                True,
            )
        )

        self.__trainer_image_data_set_field_open_nautilus_button.clicked.connect(
            partial(
                self.open_nautilus,
                self.__trainer_image_data_set_field,
                True,
            )
        )

        self.__trainer_image_data_set_commit_to_training_directory_button.clicked.connect(
            self.commit_image_data_set_to_training_directory
        )

        # on change events
        self.__trainer_directory_field.textChanged.connect(
            partial(
                self.file_path_set_check_validity,
                self.__trainer_directory_field,
                self.__trainer_directory_status,
                True,  # is_directory
            )
        )

        self.__trainer_image_data_set_field.textChanged.connect(
            partial(
                self.file_path_set_check_validity,
                self.__trainer_image_data_set_field,
                self.__trainer_image_data_set_field_status,
                True,  # is_directory
            )
        )

    def commit_image_data_set_to_training_directory(self):
        training_directory_file_path = self.__trainer_directory_field.text()
        image_data_set_directory_file_path = self.__trainer_image_data_set_field.text()
        self.__directory_of_image_data_set = self.__trainer_window_model.move_image_data_set_to_training_directory(
            training_directory_file_path,
            image_data_set_directory_file_path
        )
        self.sections_that_can_be_unlocked()

    def file_path_set_check_validity(self, field, status, is_directory, desired_extension):
        file_path_check = self.__trainer_window_model.check_if_file_path_is_valid(field, is_directory,
                                                                                  desired_extension)
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

    def update_status_label(self, status_label, new_message, stylesheet, valid_to_run):
        status_label.setText(new_message)
        status_label.setStyleSheet(stylesheet)
        status_label.setProperty("valid_to_run", valid_to_run)

        self.sections_that_can_be_unlocked()

    def sections_that_can_be_unlocked(self):
        # checking if its time to enable the file reader start button
        if self.__trainer_directory_status.property("valid_to_run"):
            self.toggle_image_input_fields_functionality(False)
        else:
            self.toggle_image_input_fields_functionality(True)

        if self.__trainer_image_data_set_field_status.property("valid_to_run"):
            self.toggle_image_data_set_commit_to_training_directory_button_functionality(False)
        else:
            self.toggle_image_data_set_commit_to_training_directory_button_functionality(True)

        if self.__directory_of_image_data_set != '':
            self.toggle_image_format_checks(False)
            if self.__currently_check_image_data_set is False:
                self.initialise_image_data_set_checks()
        else:
            self.toggle_image_format_checks(True)

        if self.__trainer_image_data_set_file_format_check_status.property("valid_to_run"):
            self.toggle_number_of_images_check_functionality(False)
        else:
            self.toggle_number_of_images_check_functionality(True)

        if self.__trainer__image_data_set_file_number_of_images_check_status.property("valid_to_run"):
            self.toggle_image_size_check_functionality(False)
        else:
            self.toggle_image_size_check_functionality(True)

        if self.__trainer_image_data_set_file_corresponding_xml_files_check_status.property("valid_to_run"):
            self.toggle_corresponding_xml_check_functionality(False)
        else:
            self.toggle_corresponding_xml_check_functionality(True)

    def initialise_image_data_set_checks(self):
        print('test')
        self.__currently_check_image_data_set = True
        self.update_status_label(self.__trainer_image_data_set_file_format_check_status, 'Checking...', '', False)
        image_format_results = self.__trainer_window_model.image_data_set_file_format_test(
            self.__directory_of_image_data_set
        )
        corresponding_xml_stylesheet = ''
        if image_format_results['check_outcome']:
            format_stylesheet = "background-color: green; color: white"
            self.__trainer_image_data_set_file_format_check_fix_button.setDisabled(True)

            self.update_status_label(
                self.__trainer__image_data_set_file_number_of_images_check_status,
                'Checking...',
                '',
                False
            )
            image_number_results = self.__trainer_window_model.image_data_set_file_format_test(
                self.__directory_of_image_data_set
            )
            if image_number_results['check_outcome']:
                image_stylesheet = "background-color: green; color: white"
                self.__trainer_image_data_set_number_of_images_check_fix_button.setDisabled(True)


                self.update_status_label(
                    self.__trainer_image_data_set_image_size_check_status,
                    'Checking...',
                    '',
                    False
                )
                image_size_results = self.__trainer_window_model.image_size_test(
                    self.__directory_of_image_data_set
                )

                if image_size_results['check_outcome']:
                    image_size_stylesheet = "background-color: green; color: white"

                    self.update_status_label(
                        self.__trainer_image_data_set_file_corresponding_xml_files_check_status,
                        'Checking...',
                        '',
                        False
                    )
                    corresponding_xml_results = self.__trainer_window_model.corresponding_xml_file_test(
                        self.__directory_of_image_data_set
                    )
                    if corresponding_xml_results['check_outcome']:
                        corresponding_xml_stylesheet = "background-color: green; color: white"
                        print('proceed')
                    else:
                        corresponding_xml_stylesheet = "background-color: red; color: white"
                        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button.setDisabled(False)
                        self.__trainer_image_data_set_corresponding_xml_files_check_fix_button.clicked.connect(
                            partial(
                                self.open_label_img_on_invalid_files,
                                corresponding_xml_results['invalid_files']
                            )
                        )




                else:
                    image_size_stylesheet = "background-color: red; color: white"
                    self.__trainer_image_data_set_image_size_check_fix_button.setDisabled(False)
                    self.__trainer_image_data_set_image_size_check_fix_button.clicked.connect(
                      self.downscale_over_sized_images
                    )

            else:
                image_stylesheet = "background-color: red; color: white"

        else:
            format_stylesheet = "background-color: red; color: white"
            if image_format_results['description'] == 'Invalid files present':
                self.__trainer_image_data_set_file_format_check_fix_button.setDisabled(False)
                self.__trainer_image_data_set_file_format_check_fix_button.clicked.connect(
                    partial(
                        self.remove_or_convert_invalid_files,
                        image_format_results['invalid_files']
                    )
                )

        self.update_status_label(
            self.__trainer_image_data_set_file_format_check_status,
            image_format_results['description'],
            format_stylesheet,
            image_format_results['check_outcome']
        )

        self.update_status_label(
            self.__trainer__image_data_set_file_number_of_images_check_status,
            image_number_results['description'],
            image_stylesheet,
            image_number_results['check_outcome']
        )

        self.update_status_label(
            self.__trainer_image_data_set_image_size_check_status,
            image_size_results['description'],
            image_size_stylesheet,
            image_size_results['check_outcome']
        )

        self.update_status_label(
            self.__trainer_image_data_set_file_corresponding_xml_files_check_status,
            corresponding_xml_results['description'],
            corresponding_xml_stylesheet,
            corresponding_xml_results['check_outcome']
        )

        self.__currently_check_image_data_set = False

    def open_label_img_on_invalid_files(self, invalid_files):
        self.__trainer_window_model.open_label_img_with_invalid_files(
            invalid_files,
            self.__get_label_img_update_signal,
        )
        self.__get_label_img_update_signal.connect(self.initialise_image_data_set_checks)
        #self.initialise_image_data_set_checks()

    def downscale_over_sized_images(self):
        self.__trainer_window_model.downscale_images(self.__directory_of_image_data_set)
        self.initialise_image_data_set_checks()

    def remove_or_convert_invalid_files(self, invalid_files):
        self.__trainer_window_model.remove_invalid_files(invalid_files)
        self.initialise_image_data_set_checks()

    def open_nautilus(self, field_to_fill_in, is_directory):
        self.__get_file_path_from_nautilus_signal.connect(self.update_input_field)
        self.__trainer_window_model.get_file_path_through_nautilus(
            self.__get_file_path_from_nautilus_signal,
            is_directory,
            field_to_fill_in
        )

    @staticmethod
    def update_input_field(message):
        field, message_to_insert = message
        field.setText(message_to_insert)

    def initialise_view(self):
        self.__trainer_window_view.show()

    def toggle_training_directory_functionality(self, toggle_value):
        self.__trainer_directory_title.setDisabled(toggle_value)
        self.__trainer_directory_field_title.setDisabled(toggle_value)
        self.__trainer_directory_field.setDisabled(toggle_value)
        self.__trainer_directory_open_nautilus_button.setDisabled(toggle_value)
        self.__trainer_directory_status.setDisabled(toggle_value)

    def toggle_image_fields_functionality(self, toggle_value):
        self.__trainer_image_data_set_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_field_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_field_open_nautilus_button.setDisabled(toggle_value)
        self.__trainer_image_data_set_field_status.setDisabled(toggle_value)
        self.__trainer_image_data_set_field.setDisabled(toggle_value)
        self.__trainer_image_data_set_commit_to_training_directory_button.setDisabled(toggle_value)

    def toggle_image_input_fields_functionality(self, toggle_value):
        self.__trainer_image_data_set_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_field_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_field_open_nautilus_button.setDisabled(toggle_value)
        self.__trainer_image_data_set_field_status.setDisabled(toggle_value)
        self.__trainer_image_data_set_field.setDisabled(toggle_value)

    def toggle_image_data_set_commit_to_training_directory_button_functionality(self, toggle_value):
        self.__trainer_image_data_set_commit_to_training_directory_button.setDisabled(toggle_value)

    def toggle_image_data_set_checks_functionality(self, toggle_value):
        self.__trainer_image_data_set_checks_title.setDisabled(toggle_value)
        self.toggle_file_format_check_functionality(toggle_value)

        self.toggle_number_of_images_check_functionality(toggle_value)
        self.toggle_image_size_check_functionality(toggle_value)
        self.toggle_corresponding_xml_check_functionality(toggle_value)
        self.toggle_xml_file_validity_check_functionality(toggle_value)

    def toggle_image_format_checks(self, toggle_value):
        self.__trainer_image_data_set_checks_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_file_format_check_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_file_format_check_status.setDisabled(toggle_value)

    def toggle_file_format_check_functionality(self, toggle_value):
        self.__trainer_image_data_set_file_format_check_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_file_format_check_status.setDisabled(toggle_value)
        self.__trainer_image_data_set_file_format_check_fix_button.setDisabled(toggle_value)

    def toggle_number_of_images_check_functionality(self, toggle_value):
        self.__trainer_image_data_set_number_of_images_check_title.setDisabled(toggle_value)
        self.__trainer__image_data_set_file_number_of_images_check_status.setDisabled(toggle_value)
        self.__trainer_image_data_set_number_of_images_check_fix_button.setDisabled(toggle_value)

    def toggle_image_size_check_functionality(self, toggle_value):
        self.__trainer_image_data_set_image_size_check_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_image_size_check_status.setDisabled(toggle_value)
        self.__trainer_image_data_set_image_size_check_fix_button.setDisabled(toggle_value)

    def toggle_corresponding_xml_check_functionality(self, toggle_value):
        print('')
        #self.__trainer_image_data_set_corresponding_xml_files_check_title.setDisabled(toggle_value)
        #self.__trainer_image_data_set_file_corresponding_xml_files_check_status.setDisabled(toggle_value)
        #self.__trainer_image_data_set_corresponding_xml_files_check_fix_button.setDisabled(toggle_value)

    def toggle_xml_file_validity_check_functionality(self, toggle_value):
        self.__trainer_image_data_set_xml_file_validity_check_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_file_xml_file_validity_check_status.setDisabled(toggle_value)
        self.__trainer_image_data_set_xml_file_validity_check_fix_button.setDisabled(toggle_value)

    def toggle_split_data_set_functionality(self, toggle_value):
        self.__trainer_image_data_set_split_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_split_field_title.setDisabled(toggle_value)
        self.__trainer_image_data_set_split_percentage_field.setDisabled(toggle_value)
        self.__trainer_image_data_set_split_button.setDisabled(toggle_value)

    def toggle_convert_to_tf_record_functionality(self, toggle_value):
        self.__trainer_image_data_convert_to_tf_record_title.setDisabled(toggle_value)
        self.__trainer_image_data_convert_to_tf_record_button.setDisabled(toggle_value)
        self.__trainer_image_data_convert_to_tf_record_status.setDisabled(toggle_value)

    def toggle_trainer_model_selection_functionality(self, toggle_value):
        self.__trainer_model_selection_title.setDisabled(toggle_value)
        self.__trainer_model_field_title.setDisabled(toggle_value)
        self.__trainer_model_field.setDisabled(toggle_value)
        self.__trainer_model_field_open_nautilus_button.setDisabled(toggle_value)
        self.__trainer_model_field_status.setDisabled(toggle_value)

        self.__trainer_config_field_title.setDisabled(toggle_value)
        self.__trainer_config_field.setDisabled(toggle_value)
        self.__trainer_config_field_open_nautilus_button.setDisabled(toggle_value)
        self.__trainer_config_field_status.setDisabled(toggle_value)
        self.__trainer_model_commit_to_training_directory_button.setDisabled(toggle_value)
        self.__trainer_model_commit_to_training_directory_status.setDisabled(toggle_value)

    def toggle_control_panel_functionality(self, toggle_value):
        self.__trainer_control_panel_start_button.setDisabled(toggle_value)
        self.__trainer_control_panel_open_tensor_board_button.setDisabled(toggle_value)
        self.__trainer_control_panel_stop_button.setDisabled(toggle_value)
        self.__trainer_control_panel_export_inference_graph_button.setDisabled(toggle_value)
        self.__trainer_control_panel_output_area.setDisabled(toggle_value)
