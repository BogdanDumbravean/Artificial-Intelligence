# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:23:53 2020

@author: Bogdan
"""

import sys
from qtpy.QtWidgets import QApplication, QDialog
from EAGUI import EAGUI
from HCGUI import HCGUI
from POSGUI import POSGUI

class GUI:
    def __init__(self):
        app = QApplication(sys.argv)

        
        hcDialog = QDialog()
        hcui = HCGUI()
        hcui.setupUi(hcDialog)
        hcDialog.setWindowTitle("HC")
        hcDialog.show()
        
        eaDialog = QDialog()
        eaui = EAGUI()
        eaui.setupUi(eaDialog)
        eaDialog.setWindowTitle("EA")
        eaDialog.show()
        
        posDialog = QDialog()
        posui = POSGUI()
        posui.setupUi(posDialog)
        posDialog.setWindowTitle("POS")
        posDialog.show()
        
        sys.exit(app.exec_())

