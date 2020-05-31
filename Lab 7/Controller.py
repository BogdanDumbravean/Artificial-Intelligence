from random import random
import numpy

class Controller:
    def __init__(self, repo):
        self.repo = repo
        self.beta = []
        self.computed = []
        
    def iteration(self, learnRate, scale):
        for i in range(len(self.repo.trainData)):
            # compute the outcome with beta*input
            # beta0 is after beta1..n, on position len(attr)
            computed = self.beta[len(self.repo.trainData[i].attr)]
            for j in range(len(self.repo.trainData[i].attr)):
                computed += self.beta[j] * self.repo.trainData[i].attr[j]

            # update beta
            # scale is for smaller values (at first iterations error is usually too large)
            val = scale * learnRate * (computed - self.repo.trainData[i].res) 

            self.beta[len(self.repo.trainData[i].attr)] -= val 
            for j in range(len(self.repo.trainData[i].attr)):
                self.beta[j] -= val * self.repo.trainData[i].attr[j]

    def scale(self):
        # purpose of scale is to get smaller values for greater accuracy
        nmax = 0
        for x in self.repo.trainData:
            nmax = max(x.res, nmax)
        return 1 / nmax

    def startTraining(self, nrIterations, learnRate = 0.1):
        self.beta = [0 for y in range(len(self.repo.trainData[0].attr) + 1)]
        scale = self.scale()
        
        for i in range(nrIterations):
            self.iteration(learnRate, scale)

    def test(self, input):
        res = self.beta[len(input.attr)]
        for i in range (len(input.attr)):
            res += self.beta[i] * input.attr[i]
        return res
