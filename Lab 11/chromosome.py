from random import randint
from numpy.random.mtrand import choice
from math import sin, cos
from copy import deepcopy

from node import Node

DEPTH_MAX = 7

C = {
    'Slight-Left-Turn':     0,
    'Move-Forward':         1,
    'Slight-Right-Turn':    2,
    'Sharp-Right-Turn':     3
}

class Chromosome():
    def __init__(self, d=DEPTH_MAX):
        self.maxDepth = d
        self.fitness = 0
        self.root = Node()
        self.root.init(d)

    def evaluate(self, inputTrain, outputTrain):
        self.fitness = 0
        exp = str(self.root)
        for (x, y) in zip(inputTrain, outputTrain):
            res = eval(exp)
            self.fitness += abs(res - C[y])
        self.fitness = self.fitness / len(inputTrain)
        return self.fitness

    @staticmethod
    def crossover(ch1, ch2, probability_crossover):
        node1 = choice(ch1.root.getNodes())
        node2 = choice(ch2.root.getNodes())
        c = Chromosome()
        if ch1.root == node1:  
            c.root = node2.deepcopy()
        else:
            c.root = Node()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)
