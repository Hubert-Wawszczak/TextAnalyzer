# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextAnalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 326)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(50, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.NumberOfWords = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfWords.setGeometry(QtCore.QRect(0, 70, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfWords.setFont(font)
        self.NumberOfWords.setObjectName("NumberOfWords")
        self.NumberOfWordsResult = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfWordsResult.setGeometry(QtCore.QRect(230, 70, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberOfWordsResult.setFont(font)
        self.NumberOfWordsResult.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberOfWordsResult.setObjectName("NumberOfWordsResult")
        self.NumberOfLines = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfLines.setGeometry(QtCore.QRect(0, 90, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfLines.setFont(font)
        self.NumberOfLines.setObjectName("NumberOfLines")
        self.NumberOfLinesResult = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfLinesResult.setGeometry(QtCore.QRect(230, 90, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.NumberOfLinesResult.setFont(font)
        self.NumberOfLinesResult.setLineWidth(0)
        self.NumberOfLinesResult.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberOfLinesResult.setObjectName("NumberOfLinesResult")
        self.NumberOfAllChar = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfAllChar.setGeometry(QtCore.QRect(0, 110, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfAllChar.setFont(font)
        self.NumberOfAllChar.setObjectName("NumberOfAllChar")
        self.NumberOfAllCharResult = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfAllCharResult.setGeometry(QtCore.QRect(230, 110, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberOfAllCharResult.setFont(font)
        self.NumberOfAllCharResult.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberOfAllCharResult.setObjectName("NumberOfAllCharResult")
        self.NumberOfUppercase = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfUppercase.setGeometry(QtCore.QRect(0, 130, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfUppercase.setFont(font)
        self.NumberOfUppercase.setObjectName("NumberOfUppercase")
        self.NumberOfUppercaseResult = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfUppercaseResult.setGeometry(QtCore.QRect(230, 130, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberOfUppercaseResult.setFont(font)
        self.NumberOfUppercaseResult.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberOfUppercaseResult.setObjectName("NumberOfUppercaseResult")
        self.NumberOfLowercase = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfLowercase.setGeometry(QtCore.QRect(0, 150, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfLowercase.setFont(font)
        self.NumberOfLowercase.setObjectName("NumberOfLowercase")
        self.NumberOfLowercaseResult = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfLowercaseResult.setGeometry(QtCore.QRect(230, 150, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberOfLowercaseResult.setFont(font)
        self.NumberOfLowercaseResult.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberOfLowercaseResult.setObjectName("NumberOfLowercaseResult")
        self.NumberOfSpecialChar = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfSpecialChar.setGeometry(QtCore.QRect(0, 170, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfSpecialChar.setFont(font)
        self.NumberOfSpecialChar.setObjectName("NumberOfSpecialChar")
        self.NumberOfSpecialCharResult = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfSpecialCharResult.setGeometry(QtCore.QRect(230, 170, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberOfSpecialCharResult.setFont(font)
        self.NumberOfSpecialCharResult.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberOfSpecialCharResult.setObjectName("NumberOfSpecialCharResult")
        self.CountEachWord = QtWidgets.QLabel(self.centralwidget)
        self.CountEachWord.setGeometry(QtCore.QRect(320, 160, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CountEachWord.setFont(font)
        self.CountEachWord.setAlignment(QtCore.Qt.AlignCenter)
        self.CountEachWord.setObjectName("CountEachWord")
        self.CountVowels = QtWidgets.QLabel(self.centralwidget)
        self.CountVowels.setGeometry(QtCore.QRect(300, 0, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CountVowels.setFont(font)
        self.CountVowels.setAlignment(QtCore.Qt.AlignCenter)
        self.CountVowels.setObjectName("CountVowels")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 80, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 40, 171, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 120, 171, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 210, 171, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 33))
        self.menubar.setObjectName("menubar")
        self.menuNew_File = QtWidgets.QMenu(self.menubar)
        self.menuNew_File.setObjectName("menuNew_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.menuNew_File.addAction(self.actionNew_File)
        self.menuNew_File.addAction(self.actionExit)
        self.menubar.addAction(self.menuNew_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TextAnalyzer"))
        self.Title.setText(_translate("MainWindow", "Statystyki"))
        self.NumberOfWords.setText(_translate("MainWindow", "Liczba S????w"))
        self.NumberOfWordsResult.setText(_translate("MainWindow", "0"))
        self.NumberOfLines.setText(_translate("MainWindow", "Liczba Linii W Pliku"))
        self.NumberOfLinesResult.setText(_translate("MainWindow", "0"))
        self.NumberOfAllChar.setText(_translate("MainWindow", "Liczba Znak??w W Pliku"))
        self.NumberOfAllCharResult.setText(_translate("MainWindow", "0"))
        self.NumberOfUppercase.setText(_translate("MainWindow", "Liczba Du??ych Znak??w"))
        self.NumberOfUppercaseResult.setText(_translate("MainWindow", "0"))
        self.NumberOfLowercase.setText(_translate("MainWindow", "Liczba Ma??ych Znak??w"))
        self.NumberOfLowercaseResult.setText(_translate("MainWindow", "0"))
        self.NumberOfSpecialChar.setText(_translate("MainWindow", "Liczba Znak??w Specialnych"))
        self.NumberOfSpecialCharResult.setText(_translate("MainWindow", "0"))
        self.CountEachWord.setText(_translate("MainWindow", "Wykres Wyst??pie?? S????w"))
        self.CountVowels.setText(_translate("MainWindow", "Wykres Wyst??pie?? Samog??osek"))
        self.label_3.setText(_translate("MainWindow", "Wykres Wyst??pie?? Sp????g??osek"))
        self.pushButton_3.setText(_translate("MainWindow", "Generuj Wykres"))
        self.pushButton_4.setText(_translate("MainWindow", "Generuj Wykres"))
        self.pushButton_5.setText(_translate("MainWindow", "Generuj Wykres"))
        self.menuNew_File.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
