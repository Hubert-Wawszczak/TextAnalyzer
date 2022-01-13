
from PyQt5.uic.properties import QtWidgets

import sys

from Modules.gui_TextAnalyzer import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.menuNew_File.clicked.connect(self.selectFile)

    def selectFile(self):
        self.NumberOfAllCharResult.setText("1")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
