# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:13:52 2020

@author: Bogdan
"""

from random import randint, random
from Domain import State

class Repository:
    def __init__(self, size, n):
        self.n = n
        self.size = size
        self.population = []
        for x in range(size):
            s = State.create(n)
            self.population.append(s)
        
    def mutate(self, state, pM): 
        '''
        state that is possible to mutate
        pM = probability to mutate
        '''
        if pM > random():
            return State.create(state.n)
        return state
    
    def crossover(self, state1, state2):
        o = [[] for i in range(state1.n)]
        
        c1 = randint(0, state1.n-1)
        c2 = randint(c1+1, state1.n)
        
        for i in range(state1.n):
            if i >= c1 and i < c2:
                o[i] = state1.A[i][:]
            else:
                o[i] = state2.A[i][:]
                
        return State(o)
    
    def selectNeighbours(self, nSize):
        """  the selection of the neighbours for each particle
        
        input --
           nSize: the number of neighbours of a particle
    
        output--
           ln: list of neighblours for each particle
        """
        pop = self.population
    
        if (nSize>len(pop)):
            nSize=len(pop)
    
        # Attention if nSize==len(pop) this selection is not a propper one
        # use a different approach (like surfle to form a permutation)
        neighbors=[]
        for i in range(len(pop)):
            localNeighbor=[]
            for j in range(nSize):
                x=randint(0, len(pop)-1)
                while (x in localNeighbor):
                    x=randint(0, len(pop)-1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        return neighbors