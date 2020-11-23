# qt.io
# https://build-system.fman.io/qt-designer-download
# https://www.riverbankcomputing.com/software/pyqt/download5

# pip install PyQt5
# pyuic5 messenger.ui -o clientui.py


from PyQt5 import QtWidgets
import clientui


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # to run on button click:
        # self.some_button.pressed.connect(self.some_method)

        # to run by timer:
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.some_method)
        # self.timer.start(1000)

        # to fix painting:
        # self.some_element.repaint()


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
