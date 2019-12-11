# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_labelWindow(object):
    def close(self):
        print("çıkıyor")

    def setupUi(self, labelWindow):
        labelWindow.setObjectName("labelWindow")
        labelWindow.resize(640, 329)
        self.centralwidget = QtWidgets.QWidget(labelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 191))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 301, 121))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        labelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(labelWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        labelWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(labelWindow)
        self.statusbar.setObjectName("statusbar")
        labelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(labelWindow)
        QtCore.QMetaObject.connectSlotsByName(labelWindow)

    def retranslateUi(self, labelWindow):
        _translate = QtCore.QCoreApplication.translate
        labelWindow.setWindowTitle(_translate("labelWindow", "MainWindow"))
        self.label.setText(_translate("labelWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    labelWindow = QtWidgets.QMainWindow()
    ui = Ui_labelWindow()
    ui.setupUi(labelWindow)
    labelWindow.show()
    sys.exit(app.exec_())
