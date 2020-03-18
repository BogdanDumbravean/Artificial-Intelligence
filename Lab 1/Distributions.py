# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:10:33 2020

@author: Bogdan
"""



import matplotlib.pyplot as plt
import numpy as np



def geometric():
    p = float(input("Enter probability of success: "))
    A = np.random.geometric(p, size=1000)
    plt.plot(A, 'ro')
    plt.ylabel('Given interval')
    plt.show()

def exponential():
    scale = float(input("Enter scale: "))
    A = np.random.exponential(scale, size=1000)
    plt.plot(A, 'bo')
    plt.ylabel('Given interval')
    plt.show()

def binomial():
    n = int(input("Enter number of trials: "))
    p = float(input("Enter probability of success: "))
    A = np.random.binomial(n, p, size=1000)
    plt.plot(A, 'go')
    plt.ylabel('Given interval')
    plt.show()


def main():
    while(True):
        print("0 - Exit")
        print("1 - Geometric Distribution")
        print("2 - Exponential Distribution")
        print("3 - Binomial Distribution")
        
        cmd = int(input("Enter command: "))
        
        try:
            if(cmd == 0):
                break
            elif(cmd == 1):
                geometric()
            elif(cmd == 2):
                exponential()
            elif(cmd == 3):
                binomial()
            else:
                print("Incorrect command")
        except: 
            print("Something went wrong. Try again")
            
main()
            