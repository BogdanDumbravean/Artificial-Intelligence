# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:01:57 2020

@author: Bogdan
"""


class UI:
    def __init__(self, controller):
        self.controller = controller
        
    def printStatesList(self, states):
        for s in states:
            print(s)
        print(len(states))
        
        if(len(states) == 0):
            print("No solution found")
            
        
    def mainMenu(self):
        while (True):
            print("Commands: ")
            print("0 - Exit")
            print("1 - DFS")
            print("2 - Greedy")
            
            cmd = input("Enter command: ")
            
            if (cmd == "0"):
                return
            elif (cmd == "1"):
                l = self.controller.dfs(self.controller.problem)
                self.printStatesList(l)
                
            elif (cmd == "2"):
                self.printStatesList(self.controller.gbfs(self.controller.problem))
            else:
                print("Invalid Command")