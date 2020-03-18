# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import Sudoku 
import Cryptarithmetic
import Geometric

        
def main():
    while(True):
        print("Commands: ")
        print("0 - Exit")
        print("1 - Sudoku")
        print("2 - Cryptarithmetic")
        print("3 - Geometric forms")
        
        cmd = int(input("Enter command: "))
        #try:
        if(cmd == 0):
            break
        elif(cmd == 1):
            Sudoku.main()
        elif(cmd == 2):
            Cryptarithmetic.main()
        elif(cmd == 3):
            Geometric.main()
        else:
            print("Invalid command")
        #except:
        #    print("Something went wrong. Try again")

main()




