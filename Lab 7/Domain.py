# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:30:37 2020

@author: Bogdan
"""


class Element:
    def __init__(self, res, attr):
        self.res = res
        self.attr = attr
        
    def __str__(self):
        return str(self.res) + ',' + str(self.attr)
    
    def __repr__(self):
        return self.__str__()