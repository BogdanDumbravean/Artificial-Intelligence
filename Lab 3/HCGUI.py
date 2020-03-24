# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QScrollArea
import time

from Repository import Repository
from Controller import Controller
from Worker import Worker    


class HCGUI(object):
        
    def setupUi(self, Dialog):
        
        self.threadpool = QThreadPool()
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(619, 373)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditN = QtWidgets.QLineEdit(Dialog)
        self.lineEditN.setGeometry(QtCore.QRect(20, 40, 113, 22))
        self.lineEditN.setObjectName("lineEditN")
        self.lineEditGenerations = QtWidgets.QLineEdit(Dialog)
        self.lineEditGenerations.setGeometry(QtCore.QRect(20, 240, 113, 22))
        self.lineEditGenerations.setObjectName("lineEditGenerations")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(30, 280, 93, 28))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startHC)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stopButton = QtWidgets.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(30, 320, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stopHC)
        
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(270, 60, 311, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.outputLabel = QtWidgets.QLabel(Dialog)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 311, 291)) #270, 60, 311, 291
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outputLabel.setFont(font)
        self.outputLabel.setObjectName("outputLabel")
        self.scrollArea.setWidget(self.outputLabel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "N:"))
        self.label_4.setText(_translate("Dialog", "Number of Generations:"))
        self.startButton.setText(_translate("Dialog", "Start"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Best solution yet:</span></p></body></html>"))
        self.stopButton.setText(_translate("Dialog", "Stop"))

    def stopHC(self):
        try:
            print("Stop signal")
            self.ctrl.stop = True
        except NameError:
            pass
        
    def startHC(self):
        # start button fct
        
        n = int(self.lineEditN.text())
        nrGens = int(self.lineEditGenerations.text())
        
        repo = Repository(1, n)
        self.ctrl = Controller(repo, 0)
        
        worker = Worker(self.ctrl.HC, self.threadPrintHC, nrGens)
        self.threadpool.start(worker)
        
    def threadPrintHC(self, bestState):
        if bestState.n < 24:
            time.sleep(.5)
        self.outputLabel.setText(str(bestState))

