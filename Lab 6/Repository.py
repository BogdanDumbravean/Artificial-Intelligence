# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:48:57 2020

@author: Bogdan
"""

from Domain import Element
import random 

class Repo:
    def __init__(self, filePath):
        self.trainData = []
        self.testData = []
        self.filePath = filePath
        
        
    def loadFromFile(self, trainDataRatio):
        '''
        Reads the data file and splits the information according to a ratio
        
        trainDataRatio - between 0 and 1
        testDataRatio = 1 - trainDataRatio
        '''
        
        
        file = open(self.filePath, 'r')
        lines = file.readlines()
        file.close()
        
        elem = []
        
        for l in lines:
            x = l.strip().split(',')
            '''
            The correct way to find the class is the greater of 
            (left-distance * left-weight) and (right-distance * right-weight).  
            If they are equal, it is balanced.
            '''
            # element has the name (L,B,R) and two attributes: d1*w1 and d2*w2
            e = Element(x[0], {0:int(x[1])*int(x[2]), 1:int(x[3])*int(x[4])})
            
            elem.append(e)
            
        
        random.shuffle(elem)
        trainDataCount = int(trainDataRatio*len(elem))
        self.trainData = elem[:trainDataCount]
        self.testData = elem[trainDataCount:]
        
        
        