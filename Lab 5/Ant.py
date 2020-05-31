# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:38:12 2020

@author: Bogdan
"""

from random import random, choice, sample
import itertools
import sys

class Ant:
    def __init__(self, n):
        #initialize firts element randomly
        l = [x + 1 for x in range(n)]
        s1 = sample(l, n)
        s2 = sample(l, n)
        self.A = [[] for i in range(2*n)]
        for i in range(n):
            self.A[i].append(s1[i])
        for i in range(n, 2*n):
            self.A[i].append(s2[i - n])
        self.n = len(self.A)
        self.fitness = sys.maxsize
        
    def evaluate(self):
        # fitness
        # start from 1, so we don't divide by 0
        c = 1
        p = []
        for i in range(self.n // 2):
            col1 = []
            col2 = []
            for j in range(self.n // 2):
                # a(i,j) != a(k,l)
                pair = (self.A[i][j], self.A[i + self.n//2][j])
                if(pair in p):
                    c += 1
                else:
                    p.append(pair)
                    
                # check columns
                if (self.A[j][i] in col1):
                    c += 1
                else:
                    col1.append(self.A[j][i])
                
                if (self.A[j + self.n//2][i] in col2):
                    c += 1
                else:
                    col2.append(self.A[j + self.n//2][i])
                
        self.fitness = c
        return c
        
    def nextMoves(self):
        # returneaza o lista de posibile adaugari la permutarile din matrice
        new = []
        for i in range(self.n):
            newLine = []
            for j in range(self.n // 2):
                nextX = j + 1
                if (nextX not in self.A[i]):
                    newLine.append(nextX)
            new.append(newLine)
        return new.copy()

    def distMove(self, a):
        # returns reverse fitness (higher is better) on vertical (on the elements that want to be added this step)
        c = self.n
        col1 = []
        col2 = []
        for i in range(self.n // 2):
            if (a[i] in col1):
                c -= 1
            else:
                col1.append(a[i])
            
            if (a[i + self.n // 2] in col2):
                c -= 1
            else:
                col2.append(a[i + self.n // 2])
        return c
    
    def getNext(self, nextSteps, i):
        # Generate all possibilities of adding the next step
        # A step is to add one column to the matrix (an element in each permutation)
        '''
        if len(nextSteps) == i: 
            return [[]] 
      
        sol = []
      
        for j in range(len(nextSteps[i])): 
           m = nextSteps[i][j] 
           nxt = self.getNext(nextSteps, i + 1)
           for p in nxt: 
               sol.append([m] + p) 
       
        return sol
    '''
        return list(itertools.product(*nextSteps))
        
    def addMove(self, q0, trace, alpha, beta):
        #update
        # adauga o noua pozitie in solutia furnicii daca este posibil
        
        # solutions are (1:n), but indexes are (0:n-1), so we add one more
        p = [[0 for i in range(self.n // 2 + 1)] for i in range(self.n)]
        # pozitiile ce nu sunt valide vor fi marcate cu zero
        nextSteps = self.nextMoves()
        # determina urmatoarele pozitii valide in nextSteps
        # daca nu avem astfel de pozitii iesim 
        if (len(nextSteps[0]) == 0):
            return False
        # punem pe pozitiile valide valoarea distantei empirice
        for i in self.getNext(nextSteps, 0):
            for j in range(len(i)):
                p[j][i[j]] += self.distMove(i)
        # calculam produsul trace^alpha si vizibilitate^beta
        for i in range(self.n):
            #idx = self.A[i][-1]
            idx = len(self.A[i]) - 1
            p[i]=[ (p[i][j]**beta)*(trace[i][idx][j]**alpha) for j in range(len(p[i]))]
        if (random()<q0):
            # adaugam cea mai buna dintre mutarile posibile
            for i in range(self.n):
                p[i] = [ [j, p[i][j]] for j in range(len(p[i])) ]
                #print("p[i]: " + str(p[i]))
                p[i] = max(p[i], key=lambda a: a[1])
                self.A[i].append(p[i][0])
                #print(self.A)
        else:
            # adaugam cu o probabilitate un drum posibil (ruleta)
            for i in range(self.n):
                s = sum(p[i])
                if (s==0):
                    #print("aici era return")
                    self.A[i].append(choice(nextSteps[i]))
                    return self.A[i][-1]
                    
                p[i] = [ p[i][j]/s for j in range(len(p[i])) ]
                p[i] = [ sum(p[i][0:j+1]) for j in range(len(p[i])) ]
                r=random()
                j=0
                while (r > p[i][j]):
                    j += 1
                self.A[i].append(j)
        return True
    
    
        
    def __str__(self):
        res = ""
        for x in self.A:
            res = res + str(x) + "\n"
        return res + "fitness (closer to 1 is better): " + str(self.fitness)
    
    def __repr__(self):
        return self.__str__()
    
    