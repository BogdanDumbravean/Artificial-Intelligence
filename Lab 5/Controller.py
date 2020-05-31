# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:38:52 2020

@author: Bogdan
"""

from Ant import Ant

class Controller:
    def iteration(self, noAnts, n, trace, alpha, beta, q0, rho):
        antSet=[Ant(n) for i in range(noAnts)]
        for i in range(2 * n):
            # numarul maxim de iteratii intr-o epoca este lungimea solutiei
            for x in antSet:
                x.addMove(q0, trace, alpha, beta)
        
        # generate fitness
        for x in antSet:
            x.evaluate()
            
        # actualizam trace-ul cu feromonii lasati de toate furnicile
        dTrace=[ 1.0 / antSet[i].fitness for i in range(len(antSet))]
        for i in range(2 * n):
            for j in range (n):
                for k in range (1, n + 1):
                    trace[i][j][k] = (1 - rho) * trace[i][j][k]
        
        for i in range(len(antSet)):
            for x in range(len(antSet[i].A)):
                for y in range(len(antSet[i].A[x])):
                    # update the trace of element from pos (x,y)
                    elem = antSet[i].A[x][y]
                    trace[x][y][elem] = trace[x][y][elem] + dTrace[i]
            
        # return best ant
        f=[ [antSet[i].fitness, i] for i in range(len(antSet))]
        f=max(f)
        return antSet[f[1]]
    
    def runAlg(self, n = 3,noEpoch = 30,noAnts = 3,alpha = 1.9,beta = 0.9,rho = 0.05,q0 = 0.5):
        bestSol = Ant(n)
        # create a trace matrix for each element (elements from 1 to n) at each position (n positions)
        # of every permutation (2 * n permutations)
        trace=[[[1 for i in range(n + 1)] for j in range (n)] for k in range(2 * n)] 
        #print("Programul ruleaza! Dureaza ceva timp pana va termina!")
        for i in range(noEpoch):
            #print("iteration:", i)
            sol=self.iteration(noAnts, n, trace, alpha, beta, q0, rho)
            if sol.fitness < bestSol.fitness:
                bestSol=sol
        return bestSol
    
    def callAlg(self, n, noEpoch, noAnts,alpha = 1.9,beta = 0.9,rho = 0.05,q0 = 0.5):
        bestSol = Ant(n)
        # create a trace matrix for each element (elements from 1 to n) at each position (n positions)
        # of every permutation (2 * n permutations)
        trace=[[[1 for i in range(n + 1)] for j in range (n)] for k in range(2 * n)] 
        #print("Programul ruleaza! Dureaza ceva timp pana va termina!")
        for i in range(noEpoch):
            #print("iteration:", i)
            sol=self.iteration(noAnts, n, trace, alpha, beta, q0, rho)
            if sol.fitness < bestSol.fitness:
                bestSol=sol
            print("Iteration", i, "Best solution so far:")
            print(bestSol)
        return bestSol
    