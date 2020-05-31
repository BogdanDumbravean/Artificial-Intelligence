# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:37:47 2020

@author: Bogdan
"""

'''
Euler Square with Ant Colony O
'''

from Controller import Controller
import matplotlib
import sys

def tests():
    fittestList = []
    bestFittest = sys.maxsize
    worstFittest = 0
    #variation = []
    
    for i in range(30):
        print("running test ", i + 1)
        ctrl = Controller()
        
        
        fit = ctrl.runAlg().fitness 
        fittestList.append(fit)
        
        if fit < bestFittest:
            bestFittest = fit
        if fit > worstFittest:
            worstFittest = fit
        
    print("Average fittest: " + str(sum(fittestList) / len(fittestList)))
    print("Deviation of fittest: " + str(worstFittest - bestFittest))
    matplotlib.pyplot.plot(fittestList)

tests()

n = int(input("Enter n: "))
noEpoch = int(input("Enter nr of epochs: "))
noAnts = int(input("Enter nr of ants: "))

ctrl = Controller()
ctrl.callAlg(n, noEpoch, noAnts)
