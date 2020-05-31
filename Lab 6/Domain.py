# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:30:37 2020

@author: Bogdan
"""


class Element:
    def __init__(self, name, attr):
        self.name = name
        self.attr = attr
        
    def __str__(self):
        return self.name + ',' + str(self.attr.values())
    
    def __repr__(self):
        return self.__str__()
    
    
class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        