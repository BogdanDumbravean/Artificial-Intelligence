# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:51:41 2020

@author: Bogdan
"""

from Domain import Node
from math import log

class Controller:
    def __init__(self, repo):
        self.repo = repo
        self.tree = None
        
    def train(self):
        attr = [x for x in self.repo.trainData[0].attr.keys()]
        self.tree = self.generate(self.repo.trainData[:], attr)
    
    def getMajorityClass(self, data):
        countL = 0
        countB = 0
        countR = 0
        for x in data:
            if x.name == 'L':
                countL += 1
            elif x.name == 'B':
                countB += 1
            elif x.name == 'R':
                countR += 1
    
        if countL == max(countL, countB, countR):
            return 'L'
        elif countB == max(countL, countB, countR):
            return 'B'
        else:
            return 'R'
        
    def attrSelection(self, data, attr):
        nameCount = {}
        attrCount = {x:{} for x in attr} 
        for x in data:
            if x.name in nameCount:
                nameCount[x.name] += 1
            else:
                nameCount[x.name] = 1
                
            for a in attr:
                val = x.attr[a]
                if val not in attrCount[a]:
                    attrCount[a][val] = {'L':0, 'B':0, 'R':0}
                attrCount[a][val][x.name] += 1
            
        S = 0
        for name in nameCount.keys():
            p = nameCount[name] / len(data)
            S -= p * log(p, 2)
            
        maxGain = 0
        sol = attr[0]
        for a in attr:
            gain = S
            for val in attrCount[a]:
                countVal = sum(attrCount[a][val].values())
                pL = attrCount[a][val]['L'] / countVal
                pB = attrCount[a][val]['B'] / countVal
                pR = attrCount[a][val]['R'] / countVal
                
                sVal = 0
                if pL != 0:
                    sVal += pL * log(pL, 2)
                if pB != 0:
                    sVal += pB * log(pB, 2)
                if pR != 0:
                    sVal +=pR * log(pR, 2)
                
                gain -= countVal / len(data) * sVal# + log(countVal / len(data), 2))
            
            if(gain > maxGain):
                maxGain = gain
                sol = a
        return sol
                
    
    def generate(self, data, attr):
        countL = 0
        countB = 0
        countR = 0
        for x in data:
            if x.name == 'L':
                countL += 1
            elif x.name == 'B':
                countB += 1
            elif x.name == 'R':
                countR += 1
                
        countAll = countL + countB + countR
        if countL == countAll:
            return Node('L')
        elif countB == countAll:
            return Node('B')
        elif countR == countAll:
            return Node('R')
        
        if len(attr) == 0:
            if countL == max(countL, countB, countR):
                return Node('L')
            elif countB == max(countL, countB, countR):
                return Node('B')
            elif countR == max(countL, countB, countR):
                return Node('R')
            
        sepAttr = self.attrSelection(data, attr)
        node = Node(sepAttr)
        
        sepAttrSplit = {x:[] for x in range(1,26)}
        for x in data:
            sepAttrSplit[x.attr[sepAttr]].append(x)
                
        for a in sepAttrSplit.keys():
            if len(sepAttrSplit[a]) == 0:
                node.children[a] = Node(self.getMajorityClass(data))
            else:
                newAttr = attr[:]
                newAttr.remove(sepAttr)
                node.children[a] = self.generate(sepAttrSplit[a], newAttr)
                
        return node
     
        
    
    def solve(self, element):
        solutions = ['L', 'B', 'R']
        
        n = self.tree
        while n != None:
            if(n.data in solutions):
                return n.data
            
            n = n.children[element.attr[n.data]]
    
    def test(self):
        '''
        Returns percent of good results
        '''
        c = 0
        for e in self.repo.testData:
            if self.solve(e) == e.name:
                c += 1
                
        return c * 100 / len(self.repo.testData)
    
    
    