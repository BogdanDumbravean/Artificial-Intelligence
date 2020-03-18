# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:07:03 2020

@author: Bogdan
"""


class State:
    def __init__(self, A, s):
        self.n = len(A)
        self.A = A
        self.sum = s
        
    def __str__(self):
        s = ""
        for l in self.A:
            s += str(l) + "\n"
        return s
            
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        if(other.n != self.n):
            return False
        if(other.sum != self.sum):
            return False
        
        for i in range(self.n):
            for j in range(self.n):
                if(self.A[i][j] != other.A[i][j]):
                    return False
        return True