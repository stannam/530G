# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import subprocess
import os
import platform
from pnn import analysis
import preprocessing
from preprocessing import Language


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(500, 500)
        Dialog.setStyleSheet("background-color: rgb(252, 230, 255);")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 125, 30))
        self.lineEdit.setStyleSheet("\n"
                                    "background-color: rgb(255, 255, 255);")

        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 180, 320, 240))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("\n"
                                      "background-color: rgb(97, 146, 255);")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 110, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("\n"
                                        "background-color: rgb(253, 154, 126);")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 110, 150, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("\n"
                                        "background-color: rgb(156, 217, 173);")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.startAnalysis)
        self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_3.clicked.connect(self.loadHelp)
        self.lineEdit.returnPressed.connect(self.startAnalysis)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def loadHelp(self):
        """
         This function prompts the table of IPA and DISC phonetic systems. The table is provided as an external pdf file,
         so different method was used by the user OS, and different way of defining the path was used by cases where
         the program is run (whether it is run from the codes, or as the frozen executable).
          For this we used conditionals.
        """
        if hasattr(sys, "frozen"):
            bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            path = os.path.join(bundle_dir, 'data', 'Celex_DISC.pdf')

        else:
            path = os.path.join(os.getcwd(), 'data', 'Celex_DISC.pdf')

        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(path)
        else:  # linux variants
            subprocess.call(('xdg-open', path))

    def startAnalysis(self):
        """
        This function is activated when the user clicks on the 'Search'. It starts the analysis, by connecting
        to the 'analysis' function of pnn.py.
        When the back-end part finishes all the operation and returns a text output, it clears the textbox and writes
        the result on it.
        """
        userInput = self.lineEdit.text()
        result = analysis(userInput)
        result = str(result)
        self.textEdit.clear()
        self.textEdit.append(result)
        return

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Language Guessing"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate(
            "Dialog", "Help: Phonetic symbols"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
