from PyQt5.QtWidgets import QFileDialog


class MainWindowModel:

    def openFile(self):
        file_name, _ = QFileDialog.getOpenFileName()
        if file_name != '':
            return file_name
        return None
