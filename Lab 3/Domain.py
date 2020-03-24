# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:12:09 2020

@author: Bogdan
"""
import random


class State:
    def __init__(self, A):
        self._A = A
        self.n = len(A)
        self._fitness = self.evaluate()
        #POS stuff:
        #the memory of that particle
        self.velocity = [0 for i in range(self.n)]
        self.bestA=self.A.copy()
        self.bestFitness=self.fitness

    @property
    def A(self):
        """getter for A"""
        return self._A

    @property
    def fitness(self):
        """getter for fitness """
        return self._fitness
    
    @A.setter
    def A(self, newA):
        self._A=newA.copy()
        self.n = len(self._A)
        self.evaluate()
        # automatic update of particle's memory 
        if (self.fitness < self.bestFitness):
            self.bestA = self._A
            self.bestFitness  = self._fitness
        
    def __str__(self):
        res = ""
        for x in self.A:
            res = res + str(x) + "\n"
        return res + "fitness (closer to 0 is better): " + str(self._fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def create(n):
        l = [x + 1 for x in range(n)]
        s = []
        for i in range(n * 2):
            s.append(random.sample(l, n))
        return State(s)
    
    
    def evaluate(self):
        c = 0
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
                
        self._fitness = c
        return c
    
    
    def getNeighbours(self):
        '''
        Get the HC neighbours 
        '''
        res = []
        for k in range(self.n):
            p = self.A[k]
            for i in range(len(p) - 1):
                for j in range(i + 1, len(p)):            
                    neighbour = []    
                    for l in range(k):
                        neighbour.append(self.A[l][:])
                        
                    aux = p[:]
                    aux2 = aux[i]
                    aux[i] = aux[j]
                    aux[j] = aux2
                    neighbour.append(aux)
                    
                    for l in range(k+1, self.n):
                        neighbour.append(self.A[l][:])
                        
                    res.append(State(neighbour))
        return res
        
    
        