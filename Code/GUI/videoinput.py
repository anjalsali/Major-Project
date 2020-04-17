# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoinput.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VideoInput(object):
    def setupUi(self, VideoInput):
        VideoInput.setObjectName("VideoInput")
        VideoInput.setFixedSize(720, 480)
        VideoInput.setStyleSheet("background-color: rgb(40,40,40);")
        self.label = QtWidgets.QLabel(VideoInput)
        self.label.setGeometry(QtCore.QRect(240, 160, 201, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Bitstream Vera Sans Mono\";")
        self.label.setObjectName("label")
        self.h1label = QtWidgets.QLabel(VideoInput)
        self.h1label.setGeometry(QtCore.QRect(60, 40, 611, 71))
        self.h1label.setMinimumSize(QtCore.QSize(591, 71))
        self.h1label.setStyleSheet("")
        self.h1label.setObjectName("h1label")
        self.exitButton2 = QtWidgets.QPushButton(VideoInput)
        self.exitButton2.setGeometry(QtCore.QRect(240, 420, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton2.sizePolicy().hasHeightForWidth())
        self.exitButton2.setSizePolicy(sizePolicy)
        self.exitButton2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.exitButton2.setObjectName("exitButton2")
        self.startButton = QtWidgets.QPushButton(VideoInput)
        self.startButton.setGeometry(QtCore.QRect(240, 320, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.startButton.setObjectName("startButton")
        self.video_name = QtWidgets.QLineEdit(VideoInput)
        self.video_name.setGeometry(QtCore.QRect(240, 194, 271, 31))
        self.video_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.video_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.video_name.setText("")
        self.video_name.setObjectName("video_name")
        self.menuButton = QtWidgets.QPushButton(VideoInput)
        self.menuButton.setGeometry(QtCore.QRect(240, 370, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 75 16pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.menuButton.setObjectName("menuButton")
        self.dateEdit = QtWidgets.QDateEdit(VideoInput)
        self.dateEdit.setGeometry(QtCore.QRect(240, 270, 131, 25))
        self.dateEdit.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(VideoInput)
        self.timeEdit.setGeometry(QtCore.QRect(380, 270, 131, 25))
        self.timeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.timeEdit.setObjectName("timeEdit")
        self.label_2 = QtWidgets.QLabel(VideoInput)
        self.label_2.setGeometry(QtCore.QRect(240, 240, 191, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Bitstream Vera Sans Mono\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(VideoInput)
        QtCore.QMetaObject.connectSlotsByName(VideoInput)
        VideoInput.setTabOrder(self.video_name, self.startButton)
        VideoInput.setTabOrder(self.startButton, self.menuButton)
        VideoInput.setTabOrder(self.menuButton, self.exitButton2)

    def retranslateUi(self, VideoInput):
        _translate = QtCore.QCoreApplication.translate
        VideoInput.setWindowTitle(_translate("VideoInput", "AGE AND GENDER DETECTOR"))
        self.label.setText(_translate("VideoInput", "Enter Video Name"))
        self.h1label.setText(_translate("VideoInput", "<html><head/><body><p><span style=\" font-size:32pt; font-weight:600; color:#ffffff;\">AGE AND GENDER DETECTOR</span></p></body></html>"))
        self.exitButton2.setText(_translate("VideoInput", "EXIT"))
        self.startButton.setText(_translate("VideoInput", "START"))
        self.video_name.setPlaceholderText(_translate("VideoInput", "Video name or Location"))
        self.menuButton.setText(_translate("VideoInput", "MAIN MENU"))
        self.dateEdit.setDisplayFormat(_translate("VideoInput", "dd/MM/yyyy"))
        self.timeEdit.setDisplayFormat(_translate("VideoInput", "H:mm:ss"))
        self.label_2.setText(_translate("VideoInput", "Enter Date and Time"))

