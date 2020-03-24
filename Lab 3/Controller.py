# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:03:00 2020

@author: Bogdan
"""

import time
from random import randint, random
import sys

class Controller:
    def __init__(self, repo, pM):
        self.repo = repo
        self.pM = pM
        self.bestState = self.getBestState()
        self.stop = False
    
    def printPop(self):
        for x in self.repo.population:
            print(x)
        print()

    def getBestState(self):
        minf = self.repo.n * self.repo.n
        mins = self.repo.population[0]
        for s in self.repo.population:
            f = s.evaluate()
            if f < minf:
                minf = f
                mins = s
        return mins
    
    # -------------------------------------------- EA:
    
    def iteration(self):
        pop = self.repo.population
        i1=randint(0,len(pop)-1)
        i2=randint(0,len(pop)-1)
        if (i1!=i2):
            c=self.repo.crossover(pop[i1],pop[i2])
            c=self.repo.mutate(c, self.pM)
            f1=pop[i1].evaluate()
            f2=pop[i2].evaluate()
            
            fc = c.evaluate()
            if(f1>f2) and (f1>fc):
                pop[i1]=c
            if(f2>f1) and (f2>fc):
                pop[i2]=c
        return pop
        
    def EA(self, iterations):
        #self.printPop()
        print("Start solving")
        for i in range(iterations):
            if self.stop:
                self.stop = False
                break
            
            if i % 1000 == 0:
                self.bestState = self.getBestState()
                yield self.bestState
            self.iteration()
            
        #self.printPop()
        print("Done solving")
        yield self.bestState
    
    # -------------------------------------------- HC:
    
    def iterationHC(self):
        s = self.repo.population[0]
        neighbours = s.getNeighbours()
        bestFitness = sys.maxsize
        bestNeighbour = s
        for n in neighbours:
            fit = n.fitness
            if fit < bestFitness:
                bestFitness = fit
                bestNeighbour = n
        if bestFitness < s.fitness:
            self.repo.population[0].A = bestNeighbour.A
    
    def HC(self, iterations):
        print("Start solving")
        for i in range(iterations):
            if self.stop:
                self.stop = False
                break
            
            #i += 1
            #if i % 100 == 0:
            self.bestState = self.getBestState()
            #print(self.bestState.fitness)
            yield self.bestState
                
            self.iterationHC()
        
        print("Done solving")
        yield self.getBestState()
        
    # -------------------------------------------- POS:
        
    
    def manhattenDistance(self, p1, p2):
        s = 0
        for i in range(len(p1)):
            s += abs(p1[i] - p2[i])
        return s
    
    def iterationPOS(self, neighbors, c1, c2, w ):
        """
        an iteration
    
        pop: the current state of the population
        
    
        for each particle we update the velocity and the position
        according to the particle's memory and the best neighbor's position 
        """
        pop = self.repo.population
        bestNeighbours=[]
        #determine the best neighbor for each particle
        for i in range(len(pop)):
            bestNeighbours.append(neighbors[i][0])
            for j in range(1,len(neighbors[i])):
                if (pop[bestNeighbours[i]].fitness>pop[neighbors[i][j]].fitness):
                    bestNeighbours[i]=neighbors[i][j]
                    
        #update the velocity for each particle
        newAs = []
        for i in range(len(pop)):
            newA = []
            for j in range(len(pop[0].A)):
                newVelocity = w * pop[i].velocity[j]
                newVelocity = newVelocity + c1*random()*self.manhattenDistance(pop[bestNeighbours[i]].A[j],pop[i].A[j])    
                newVelocity = newVelocity + c2*random()*self.manhattenDistance(pop[i].bestA[j],pop[i].A[j])
                pop[i].velocity[j]=newVelocity
                if newVelocity > random():
                    newA.append(pop[bestNeighbours[i]].A[j].copy())
                else:
                    newA.append(pop[i].A[j].copy())
            newAs.append(newA.copy())
        
        #update the position for each particle
        for i in range(len(pop)):
            pop[i].A=newAs[i]
        return pop
    
    def POS(self, iterations=100):
        #PARAMETERS:
        
        #specific parameters for PSO
        w=1.0
        c1=1.
        c2=2.5
        sizeOfNeighbourhood=20
    
        # we establish the particles' neighbors 
        neighbourhoods=self.repo.selectNeighbours(sizeOfNeighbourhood)
        
        print("Start solving")
        
        for i in range(iterations):
            
            if self.stop:
                self.stop = False
                break
            
            if iterations < 30:
                time.sleep(.5)
                self.bestState = self.getBestState()
                #print(self.bestState.fitness)
                yield self.bestState
            else:
                if i % 100 == 0:
                    self.bestState = self.getBestState()
                    print(self.bestState.fitness)
                    yield self.bestState
                
            self.iterationPOS(neighbourhoods, c1,c2, w/(i+1))
        
        print("Done solving")
        yield self.getBestState()
    