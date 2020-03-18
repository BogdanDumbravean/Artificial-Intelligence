# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:30:22 2020

@author: Bogdan
"""

import numpy as np


def arithmRead(reverse):
    A=[]
    
    print("Enter problem:")
    
    while(True):
        line = input()
        A.append(line)
        
        if ('=' in line):
            result = input()
            A.append(result)
            break
        
        if ('-' in line):
            reverse = True
    
    if(reverse):
        A.reverse()
    return A
        
def arithmGenRandom(A):
    B = []
    letters = {}
    for word in A:
        line=[]
        
        if(word[0] not in letters.keys()):
            letters[word[0]] = np.random.randint(1, 16)    
        line.append(letters[word[0]])
        
        for i in range(1, len(word)):
            if(word[i] in "+-="):
                continue
           
            if(word[i] not in letters.keys()):
                letters[word[i]] = np.random.randint(0,16)
            line.append(letters[word[i]])
            
        B.append(line)
        
    return B
        
        
def arithmPrint(A):
    
    L = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    for i in range(len(A)):
        for x in A[i]:
            if(x < 10):
                print(x, end="")
            else:
                print(L[x], end="")
        print()

def arithmCheckSol(A):
    # build result in reverse order
    result = []
    for i in range(len(A) - 1):
        word = A[i][:]
        word.reverse()
        
        for j in range(len(A[i])):
            if(j >= len(result)):
                result.append(word[j])
            else:
                result[j] += word[j]
                
    x = 0
    i = 0
    while(True):
        if(len(result) > i):
            result[i] += x
        else:
            result.append(x)
        
        x = result[i] // 16
        result[i] = result[i] % 16
        
        i += 1
        
        if(x == 0 and i >= len(result)):
            break
        
        
    # reverse the result
    result.reverse()
    return result == A[len(A)-1]


        
def main():
    reverse = False
    A = arithmRead(reverse)
    isSol = False
    
    k = int(input("Enter nr of tries: "))
    for i in range(k):
        B = arithmGenRandom(A)
        
        if (arithmCheckSol(B)):
            isSol = True
            print("Found solution:")     
            
            if(reverse):
                B.reverse()
                
            arithmPrint(B)
            break
    
    if(not isSol):
        print("Didn't find solution")
        
        
        

