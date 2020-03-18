# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:05:39 2020

@author: Bogdan
"""
from State import State

class Problem:
    def __init__(self, initialState):
        self.initialState = initialState
        
    def checkCorrect(self, state):
        # Queens on board problem, basically
        for i in range(state.n):
            sl = 0
            sc = 0
            sd1 = 0
            sd2 = 0
            sd3 = 0
            sd4 = 0
            for j in range (state.n):
                #lines
                sl += state.A[i][j]
                if (sl > 1):
                    return False
                #columns
                sc += state.A[j][i]
                if (sc > 1):
                    return False
                #diagonals parallel to main diagonal
                if (i + j < state.n):
                    sd1 += state.A[i+j][j]      # below main diagonal
                    if(sd1 > 1):
                        return False
                    sd2 += state.A[j][i+j]      # above main diagonal
                    if(sd2 > 1):
                        return False
                #diagonals parallel to anti diagonal
                if (i + j < state.n):
                    sd3 += state.A[state.n-j-1 - i][j]      # above anti diagonal (because of "-i")
                    if(sd3 > 1):
                        return False
                    sd4 += state.A[state.n-j-1][j + i]      # below anti diagonal 
                    if(sd4 > 1):
                        return False
        
        return True
                    
        
    def expand(self, state):
        # add a 1 in all possible positions, starting from given state
        if(state.sum == len(state.A)):
            return []
        
        l = []
        n = state.n
            
        for i in range(n):
            for j in range(n):
                if(state.A[i][j] == 0):
                    B = []
                    for line in state.A:
                        B.append(line.copy())
                    B[i][j] = 1
                    
                    B = State(B, state.sum + 1)
                    if(self.checkCorrect(B)):
                        l.append(B)
        return l
    
    
    def isFinal(self, state):
        # final state if there are n 1's placed correctly
        return state.sum == len(state.A)
    
    
    '''def heuristic(self, state1, state2):
        # state2 has to be a descendant of state1
        # return 0 if state2 should be taken into consideration (it won't generate a state that was already generated)
        # (0 and 1, because it should return a float, not a bool)
        newQ = False
        for i in range(state1.n):
            for j in range(state1.n):
                if(state1.A[i][j] == 0 and state2.A[i][j] == 1):
                    newQ = True
                if(state1.A[i][j] == 1 and newQ):
                    return 1
        return 0
    '''
    
    def heuristic(self, state):
        # count nr of 0's on matrix
        c = 0
        for i in range(state.n):
            for j in range(state.n):
                if(state.A[i][j] == 0):
                    c += 1
        return c