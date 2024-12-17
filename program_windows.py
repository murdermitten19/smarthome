import sys
from PyQt5 import QtWidgets, uic
# from main_handler import main_window


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('z_main_window.ui', self)
        self.pushButton.clicked.connect(self.show_view_devices)
        self.pushButton_2.clicked.connect(self.show_edit_devices)
        self.pushButton_3.clicked.connect(self.close)
        
    def show_view_devices(self):
        view_devices_dialog = ViewDevicesDialog()
        view_devices_dialog.show()
        self.close()
        view_devices_dialog.exec_()
        
        
    def show_edit_devices(self):
        edit_devices_dialog = EditDevicesDialog()
        edit_devices_dialog.show()
        self.close()
        edit_devices_dialog.exec_()

        
    def showMainWindow(self):
        pass

        
        



class ViewDevicesDialog(QtWidgets.QDialog):
    def __init__(self):
        super(ViewDevicesDialog, self).__init__()
        uic.loadUi('z_view_devices.ui', self)
        
        self.pushButton.clicked.connect(self.return_to_main)
        
    def return_to_main(self):
        MainWindow.showMainWindow()
        
class EditDevicesDialog(QtWidgets.QDialog):
    def __init__(self):
        super(EditDevicesDialog, self).__init__()
        uic.loadUi('z_edit_devices.ui', self)
        
        self.pushButton.clicked.connect(self.return_to_main)
        
    def return_to_main(self):
        MainWindow.showMainWindow()
