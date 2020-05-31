# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:27:10 2020

@author: Bogdan
"""

'''
Decision Tree
'''

from Repository import Repo
from Controller import Controller
import sys

r = Repo('balance-scale.data')
c = Controller(r)

nrTests = 30

minv = sys.maxsize
maxv = 0
sumv = 0
for i in range(nrTests):
    r.loadFromFile(0.8)
    c.train()
    val = c.test()
    
    sumv += val
    if val > maxv:
        maxv = val
    if val < minv:
        minv = val
    
    print('test', i+1, '-', val)
    
print('\nAverage:', sumv/nrTests)
print('Deviation:', maxv-minv)