# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:38:16 2020

@author: Bogdan
"""

from PyQt5.QtCore import pyqtSlot, QRunnable

class Worker(QRunnable):

    def __init__(self, algorithmFunction, printFunction, *args):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.algorithmFunction = algorithmFunction
        self.printFunction = printFunction
        self.args = args

    @pyqtSlot()
    def run(self):
        for result in self.algorithmFunction(*self.args):
            self.printFunction(result)
        