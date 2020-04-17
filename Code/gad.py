import cv2
import argparse
import numpy as np
from datetime import datetime

from motpy import Detection, MultiObjectTracker
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

from GUI import mainmenu, videoinput, about
import core



class GadGui(mainmenu.Ui_MainWindow, QtWidgets.QMainWindow):

	def __init__(self):
		super(GadGui,self).__init__()
		self.setupUi(self)
		self.centerMain()

		self.videoInputButton.clicked.connect(self.openWindow)
		self.liveInputButton.clicked.connect(self.liveInput)
		self.exitButton.clicked.connect(self.closeWindow)
		self.aboutButton.clicked.connect(self.openAbout)

	def openWindow(self):
		self.window = QtWidgets.QWidget()
		self.ui = videoinput.Ui_VideoInput()
		self.ui.setupUi(self.window)
		MainWindow.hide()
		self.centerVideo()
		self.window.show()
		self.ui.menuButton.clicked.connect(self.openMainWindow)
		self.ui.startButton.clicked.connect(self.takeInput)
		self.ui.exitButton2.clicked.connect(self.closeVideoWindow)

	def openAbout(self):
		self.window = QtWidgets.QWidget()
		self.ui = about.Ui_about()
		self.ui.setupUi(self.window)
		MainWindow.hide()
		self.centerVideo()
		self.window.show()
		self.ui.backButton.clicked.connect(self.openMainWindow)

	def centerMain(self):
		dimension = self.frameGeometry()
		centerPosition = QDesktopWidget().availableGeometry().center()
		dimension.moveCenter(centerPosition)
		self.move(dimension.topLeft())
	
	def centerVideo(self):
		dimension1 = self.window.frameGeometry()
		centerPosition1 = QDesktopWidget().availableGeometry().center()
		dimension1.moveCenter(centerPosition1)
		self.window.move(dimension1.topLeft())

		

	def closeWindow(self):
		MainWindow.close()
		print("Exiting Application..........")

	def closeVideoWindow(self):
		self.window.hide()
		MainWindow.close()
		print("Exiting Application..........")

	def openMainWindow(self):
		self.window.hide()
		MainWindow.show()

	def takeInput(self):
		videoName = self.ui.video_name.text()
		dateVar = self.ui.dateEdit.text()
		timeVar = self.ui.timeEdit.text()
		
		if not videoName:
			QtWidgets.QMessageBox.about(self.window,"Warning !","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:350; color:#ffffff;\">Please Enter Video Name</span></p></body></html>")
			return
		self.window.hide()
		core.run('./Input/'+str(videoName),dateVar,timeVar)
		self.window.show()		

	def liveInput(self):
		MainWindow.hide()
		now = datetime.now()
		dateVar = now.strftime("%d/%m/%Y")
		timeVar = now.strftime("%H:%M:%S")
		core.run(0,dateVar,timeVar)
		MainWindow.show()
		


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GadGui()
    MainWindow.show()
    app.exec_()

