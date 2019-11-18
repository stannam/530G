# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
import sys
from pnn import analysis
import preprocessing
from preprocessing import Language


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(252, 230, 255);")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 60, 113, 21))
        self.lineEdit.setStyleSheet("\n"
                                    "background-color: rgb(255, 255, 255);")

        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(70, 150, 251, 111))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("\n"
                                      "background-color: rgb(97, 146, 255);")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 80, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("\n"
                                        "background-color: rgb(253, 154, 126);")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 100, 130, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("\n"
                                        "background-color: rgb(156, 217, 173);")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.startAnalysis)
        self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)
        self.lineEdit.returnPressed.connect(self.startAnalysis)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def startAnalysis(self):
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
            "Dialog", "Help: Check symbol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
