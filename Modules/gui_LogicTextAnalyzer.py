import sys
import logging
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from Modules.text_analyze import TextAnalyzer
from Modules.plot_generator import Plot
from Modules.gui_TextAnalyzer import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.textanalyzer = TextAnalyzer()
        self.plotGen = Plot()
        self.pushButton_3.clicked.connect(self.plotCountVowels)
        self.pushButton_4.clicked.connect(self.plotCountConsonants)
        self.pushButton_5.clicked.connect(self.plotCountEachWord)
        self.actionNew_File.triggered.connect(self.newFileSelector)
        self.actionExit.triggered.connect(self.Exit)
        self.filePath = ""
        self.msg = QMessageBox()
        self.logger = logging.getLogger(__name__)

    def Exit(self):
        sys.exit(app.exec_())

    def newFileSelector(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.filePath = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "TextFile (*.txt)", options=options)
        self.NumberOfWordsResult.setText(str(self.textanalyzer.numberOfWords(str(self.filePath[0]))))
        self.NumberOfLinesResult.setText(str(self.textanalyzer.numberOfLines(str(self.filePath[0]))))
        self.NumberOfAllCharResult.setText(str(self.textanalyzer.numberOfAllCharacters(str(self.filePath[0]))))
        self.NumberOfUppercaseResult.setText(str(self.textanalyzer.numberOfUppercase(str(self.filePath[0]))))
        self.NumberOfLowercaseResult.setText(str(self.textanalyzer.numberOfLowercase(str(self.filePath[0]))))
        self.NumberOfSpecialCharResult.setText(str(self.textanalyzer.numberOfSpecialCharacters(str(self.filePath[0]))))

    def plotCountEachWord(self):
        try:
            self.plotGen.plot_countEachWord(str(self.filePath[0]))
        except:
            self.msg.setWindowTitle("ERROR")
            self.msg.setText("SELECT FILE TO ANALYZE! File - New File")
            self.msg.exec_()
            self.logger.exception("Error no file selected")

    def plotCountVowels(self):
        try:
            self.plotGen.plot_countVowels(str(self.filePath[0]))
        except:
            self.msg.setWindowTitle("ERROR")
            self.msg.setText("SELECT FILE TO ANALYZE! File - New File")
            self.msg.exec_()
            self.logger.exception("Error no file selected")

    def plotCountConsonants(self):
        try:
            self.plotGen.plot_countConsonants(str(self.filePath[0]))
        except:
            self.msg.setWindowTitle("ERROR")
            self.msg.setText("SELECT FILE TO ANALYZE! File - New File")
            self.msg.exec_()
            self.logger.exception("Error no file selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
