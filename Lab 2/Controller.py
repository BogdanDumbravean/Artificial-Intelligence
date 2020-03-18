# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:03:36 2020

@author: Bogdan
"""


class Controller:
    def __init__(self, problem):
        self.problem = problem
        
    def orderStates(listOfStates):
        pass
    
    def dfs(self, problem): 
        # Generate all possibilities and add the new ones to the stack
        sol = []
        q = [self.problem.initialState]
        while(q != []):
            crt = q.pop()
            
            for s in self.problem.expand(crt):
                q.append(s)
            
            if (self.problem.isFinal(crt) and sol.count(crt) == 0):
                sol.append(crt)
                
        return sol
    
    '''def gbfs(self, problem):
        # Generate all possibilities that are sure to not repeat later (using heuristic)
        sol = []
        q = [self.problem.initialState]
        while(q != []):
            crt = q.pop()
            
            for s in self.problem.expand(crt):
                if(self.problem.heuristic(crt, s) == 0):
                    q.append(s)
            
            if (self.problem.isFinal(crt)):
                sol.append(crt)
                
        return sol
        '''
    def gbfs(self, problem):
        sol = []
        q = [self.problem.initialState]
        while(q != []):
            crt = q.pop()
            
            aux = []
            for s in self.problem.expand(crt):
                aux.append(s)
            
            if (self.problem.isFinal(crt)):
                return [crt]
                
            aux = [ [x, self.problem.heuristic(x)] for x in aux]
            aux.sort(key=lambda x:x[1])
            aux = [x[0] for x in aux]
            q = aux[:] + q 
        
        return sol