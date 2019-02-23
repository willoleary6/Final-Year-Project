from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import (QStyle)
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtGui import QIcon

from Prototypes.GUIs.PyQT.View.videoWindowView import videoWindowView
from Prototypes.GUIs.PyQT.Model.videoWindowModel import videoWindowModel


class videoWindowController(QMainWindow):
    def __init__(self, coordinator, parent=None):
        super(videoWindowController, self).__init__(parent)
        self.__video_window_view = videoWindowView()

        # self.__video_window_controller
        self.__video_window_media_player = self.__video_window_view.get_media_player()

        self.__video_window_play_button = self.__video_window_view.get_play_button()
        self.__video_window_play_button.clicked.connect(self.play)

        self.__video_window_error_label = self.__video_window_view.get_error_label()

        self.__video_window_position_slider = self.__video_window_view.get_position_slider()
        self.__video_window_position_slider.sliderMoved.connect(self.setPosition)

        self.__video_window_menu_bar = self.__video_window_view.get_menu_bar()

        self.__coordinator = coordinator
        self.__video_window_model = videoWindowModel()

        self.__video_widget = self.__video_window_view.get_video_widget()
        self.initialise_actions()

        self.__video_window_media_player.setVideoOutput(self.__video_widget)
        self.__video_window_media_player.stateChanged.connect(self.mediaStateChanged)
        self.__video_window_media_player.positionChanged.connect(self.positionChanged)
        self.__video_window_media_player.durationChanged.connect(self.durationChanged)
        self.__video_window_media_player.error.connect(self.handleError)

    def initialise_view(self):
        self.__video_window_view.resize(1280, 960)
        self.__video_window_view.show()

    def initialise_actions(self):
        # Create new action
        open_action = QAction(QIcon('open.png'), '&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open movie')
        open_action.triggered.connect(self.open_file)

        # Create exit action
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.exitCall)

        # Create menu bar and add action

        file_menu = self.__video_window_menu_bar.addMenu('&File')
        # file_menu.addAction(newAction)
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

    def open_file(self):
        file_path = self.__video_window_model.openFile(self.__video_window_view)
        if file_path is not None:
            self.__video_window_media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.__video_window_play_button.setEnabled(True)

    def exitCall(self):
        # sys.exit(app.exec_())
        print('Exiting')

    def play(self):
        if self.__video_window_media_player.state() == QMediaPlayer.PlayingState:
            self.__video_window_media_player.pause()
        else:
            self.__video_window_media_player.play()

    def mediaStateChanged(self, state):
        if self.__video_window_media_player.state() == QMediaPlayer.PlayingState:
            self.__video_window_play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.__video_window_play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.__video_window_position_slider.setValue(position)

    def durationChanged(self, duration):
        self.__video_window_position_slider.setRange(0, duration)

    def setPosition(self, position):
        self.__video_window_media_player.setPosition(position)

    def handleError(self):
        self.__video_window_play_button.setEnabled(False)
        self.__video_window_error_label.setText("Error: " + self.__video_window_media_player.errorString())


'''

package ui.controller;
import ui.coordinator.ILoginCoordinator;
import ui.model.LoginModel;
import ui.view.LoginFrame;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.security.InvalidParameterException;

public class LoginFrameController extends BaseFrameController {
    private ILoginCoordinator coordinator;
    private LoginModel model;
    private JButton loginButton, backButton;
    private JTextField usernameField;
    private JPasswordField passwordField;
    private JLabel errorLabel;

    public LoginFrameController(ILoginCoordinator coordinator) {
        this.coordinator = coordinator;
        model = new LoginModel();
        initComponents();
        initListeners();
    }

    private void initComponents() {
        LoginFrame loginFrame = new LoginFrame();
        frame = loginFrame;
        loginButton = loginFrame.getLoginButton();
        backButton = loginFrame.getBackButton();
        usernameField = loginFrame.getUsernameField();
        passwordField = loginFrame.getPasswordField();
        errorLabel = loginFrame.getErrorLabel();
    }

    private void initListeners() {
        loginButton.addActionListener(new LoginButtonListener());
        backButton.addActionListener(e -> coordinator.start());
    }

    private class LoginButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                model.setUsername(usernameField.getText());
                model.setPassword(passwordField.getText());
                if(model.login())
                    coordinator.goToMainMenu();
                else
                    errorLabel.setText("Invalid username or password");
            } catch (InvalidParameterException exception) {
                errorLabel.setText(exception.getMessage());
            }
        }
    }
}

'''
