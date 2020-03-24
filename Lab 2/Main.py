# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:10:53 2020

@author: Bogdan
"""

'''
Queen's problem on nxn matrix
'''

from UI import UI
from Controller import Controller
from Problem import Problem
from State import State


n = int(input("Enter n: "))

A = [[0 for i in range(n)] for i in range(n)]
init = State(A, 0)
pb = Problem(init)
ctrl = Controller(pb)
ui = UI(ctrl)

ui.mainMenu()
