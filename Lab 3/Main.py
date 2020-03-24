# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:23:27 2020

@author: Bogdan
"""

from GUI import GUI
from Repository import Repository
from Controller import Controller

import sys
import matplotlib


def testsEA():
    fittestList = []
    bestFittest = sys.maxsize
    worstFittest = 0
    #variation = []
    
    for i in range(30):
        n = 5
        popSize = 40
        mutationProbability = .5
        nrGens = 1000
        
        repo = Repository(popSize, n)
        ctrl = Controller(repo, mutationProbability)
        
        
        ctrl.EA(nrGens)
        fit = ctrl.getBestState().fitness 
        fittestList.append(fit)
        
        if fit < bestFittest:
            bestFittest = fit
        if fit > worstFittest:
            worstFittest = fit
        
    print("Average fittest: " + str(sum(fittestList) / len(fittestList)))
    print("Deviation of fittest: " + str(worstFittest - bestFittest))
    matplotlib.pyplot.subplot(1,2,1)
    matplotlib.pyplot.plot(fittestList)

def testsPOS():
    fittestList = []
    bestFittest = sys.maxsize
    worstFittest = 0
    #variation = []
    
    for i in range(30):
        n = 5
        popSize = 40
        mutationProbability = .5
        nrGens = 1000
        
        repo = Repository(popSize, n)
        ctrl = Controller(repo, mutationProbability)
        
        ctrl.POS(nrGens)
        fit = ctrl.getBestState().evaluate()
        fittestList.append(fit)
        
        if fit < bestFittest:
            bestFittest = fit
        if fit > worstFittest:
            worstFittest = fit
        
    print("Average fittest: " + str(sum(fittestList) / len(fittestList)))
    print("Deviation of fittest: " + str(worstFittest - bestFittest))
    #print(variation)
    matplotlib.pyplot.subplot(1,2,2)
    matplotlib.pyplot.plot(fittestList)
    
print("Tests for EA:")
testsEA()
print("Tests for POS:")
testsPOS()


gui = GUI()



        