# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:03:32 2020

@author: Bogdan
"""


import numpy as np
import math

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x) + ":" + str(self.y)
    
    def __repr__(self):
        return str(self)
    

forms = {1:[P(0,0), P(0,1), P(0,2), P(0,3)],
          2:[P(0,0), P(0,2), P(1,0), P(1,2), P(1,3)],
          3:[P(0,0), P(1,0), P(1,1), P(1,2)],
          4:[P(0,0), P(0,1), P(0,2), P(1,2)],
          5:[P(0,0), P(1,-1), P(1,0), P(1,1)]}


def geoGenRandom():
    A = [[0 for i in range(7)] for i in range(6)]
    # nr of forms
    nr = np.random.randint(6, 8)
    
    for k in range(nr):
        
        x = np.random.randint(0,6)
        y = np.random.randint(0,7)
        while(A[x][y] != 0):
            x = np.random.randint(0,6)
            y = np.random.randint(0,7)
        
        A[x][y] = np.random.randint(-5,0) # generate negative from -1 to -5
        
    return A
        
def geoPrint(A):
    L = {0:' ', 1:'O', 2:'X', 3:'@', 4:'*', 5:'A'}
    for i in range(len(A)):
        for x in A[i]:
            print(x, end="")
        print()

def geoCheckSol(A):
    for i in range(6):
        for j in range(7):
            if(A[i][j] < 0):
                for p in forms[abs(A[i][j])]:
                    if(p.x == 0 and p.y == 0):
                        A[i][j] = -A[i][j]
                        continue
                        
                    x = i + p.x
                    y = j + p.y
                    if(x >= 0 and x < 5 and y >= 0 and y < 6 and A[x][y] == 0):
                        A[x][y] = abs(A[i][j])
                    else:
                        return False
                    
    for l in A:
        if (0 in l):
            return False
                    
    return True

        
def main():
    isSol = False
    
    k = int(input("Enter nr of tries: "))
    for i in range(k):
        B = geoGenRandom()
        
        if (geoCheckSol(B)):
            isSol = True
            print("Found solution:")     
                
            geoPrint(B)
            break
    
    if(not isSol):
        print("Didn't find solution")
        
        
        
