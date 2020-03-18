# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:28:02 2020

@author: Bogdan
"""

import numpy as np
import math


def sudokuRead():
    n = int(input("Enter n: "))
    A=[[0 for i in range(n)] for i in range(n)]
    
    print("Enter lines of sudoku: ", end="")
    for i in range(n):
        A[i] = [int(s) for s in input().split()]
    return A
        
def sudokuGenRandom(n, A):
    B = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (A[i][j] == 0):
                B[i][j] = np.random.randint(1, n + 1)
            else:
                B[i][j] = A[i][j]
    return B
        
def sudokuPrint(n, A):
    for i in range(n):
        print(A[i])

def sudokuCheckSol(n, A):
    for i in range(n):
        nrLine = []
        nrCol = []
        
        for j in range(n):
            if (A[i][j] in nrLine):
                return False
            nrLine.append(A[i][j])
            
            if (A[j][i] in nrCol):
                return False
            nrCol.append(A[j][i])
            
    square = int(math.sqrt(n))
    for i in range(square):
        for j in range(square):
            nr = []
            for x in range(square):
                for y in range(square):
                    if (A[i * square + x][j * square + y] in nr):
                        return False
                    nr.append(A[i * square + x][j * square + y])
    
    return True


        
def main():
    A = sudokuRead()
    n = len(A)
    isSol = False
    
    k = int(input("Enter nr of tries: "))
    for i in range(k):
        B = sudokuGenRandom(n, A)
        
        if (sudokuCheckSol(n, B)):
            isSol = True
            print("Found solution:")        
            sudokuPrint(n, B)
            break
    
    if(not isSol):
        print("Didn't find solution")