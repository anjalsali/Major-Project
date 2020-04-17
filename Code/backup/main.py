# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(720, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(40,40,40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.h1label = QtWidgets.QLabel(self.centralwidget)
        self.h1label.setGeometry(QtCore.QRect(60, 40, 611, 71))
        self.h1label.setMinimumSize(QtCore.QSize(591, 71))
        self.h1label.setStyleSheet("")
        self.h1label.setObjectName("h1label")
        self.videoInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoInputButton.setGeometry(QtCore.QRect(230, 180, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoInputButton.sizePolicy().hasHeightForWidth())
        self.videoInputButton.setSizePolicy(sizePolicy)
        self.videoInputButton.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.videoInputButton.setObjectName("videoInputButton")
        self.liveInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.liveInputButton.setGeometry(QtCore.QRect(230, 230, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liveInputButton.sizePolicy().hasHeightForWidth())
        self.liveInputButton.setSizePolicy(sizePolicy)
        self.liveInputButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.liveInputButton.setObjectName("liveInputButton")
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(230, 330, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        self.aboutButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.aboutButton.setObjectName("aboutButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(230, 280, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.exitButton.setObjectName("exitButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.videoInputButton, self.liveInputButton)
        MainWindow.setTabOrder(self.liveInputButton, self.exitButton)
        MainWindow.setTabOrder(self.exitButton, self.aboutButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AGE AND GENDER DETECTIOR"))
        self.h1label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:32pt; font-weight:600; color:#ffffff;\">AGE AND GENDER DETECTOR</span></p></body></html>"))
        self.videoInputButton.setText(_translate("MainWindow", "VIDEO INPUT"))
        self.liveInputButton.setText(_translate("MainWindow", "LIVE INPUT"))
        self.aboutButton.setText(_translate("MainWindow", "ABOUT"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))

