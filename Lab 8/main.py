'''
An example of a simple ANN with 1+2 layers
The implementation uses 2 matrixes in order to memorise the weights.

'''

import numpy as np
import matplotlib.pyplot as plt
import random

class NeuralNetwork:
    
    def __init__(self, x, y, hiddenNodes):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1], hiddenNodes)
        self.weights2   = np.random.rand(hiddenNodes,1) 
        self.y          = y
        self.output     = np.zeros(self.y.shape)
        self.loss       = []

    def test(self, input):
        layer1 = np.dot(input, self.weights1)
        return np.dot(layer1, self.weights2)

    # the function that computs the output of the network for some input
    def feedforward(self):
        self.layer1 = np.dot(self.input, self.weights1)
        self.output = np.dot(self.layer1, self.weights2)
        

    # the backpropagation algorithm 
    def backprop(self, l_rate):
        error = 2*(self.y - self.output) * self.output

        d_weights2 = np.dot(self.layer1.T, error)
        d_weights1 = np.dot(self.input.T,  np.dot(error, self.weights2.T) * self.layer1)

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += l_rate * d_weights1 / len(self.input) 
        self.weights2 += l_rate * d_weights2 / len(self.input) 
        
        self.loss.append(sum((self.y - self.output)**2))



def readData(testx, filePath):
    file = open(filePath, 'r')
    lines = file.readlines()
    file.close()
    
    elem = []
    for l in lines:
        x = l.strip().split(' ')
        # Data file has on each line 5 attributes and their corresponding value
        e = (float(x[5]), [float(x[i]) for i in range(5)]) 
        elem.append(e)
        
    # split the Data
    trainDataRatio = 0.8
    random.shuffle(elem)
    trainDataCount = int(trainDataRatio*len(elem))
    
    # place data in arrays and in the corresponding slots
    testx['train']['input'] = [np.array(e[1]) for e in elem[:trainDataCount]]
    testx['train']['output'] = [[e[0]] for e in elem[:trainDataCount]]
    testx['test']['input'] = [np.array(e[1]) for e in elem[trainDataCount:]]
    testx['test']['output'] = [[e[0]] for e in elem[trainDataCount:]]



if __name__ == "__main__":
    nrTests = 30
    error = 0
    for x in range(nrTests):
        print("Test nr", x+1)

        testx = {'train':{}, 'test':{}}
        readData(testx, "data.txt")

        trainData = np.array(testx['train']['input'])
        trainDataSol = np.array(testx['train']['output'])
        
        nn = NeuralNetwork(trainData,trainDataSol,3)

        # train network
        nn.loss=[]
        iterations =[]
        for i in range(100):
            nn.feedforward()
            nn.backprop(1e-08)
            iterations.append(i)

        #test network
        output = nn.test(np.array(testx['test']['input']))
        actualResult = np.array(testx['test']['output'])

        localError = sum(abs(x) for x in (output-actualResult)) / len(output)
        print('\tLocal error (per item):', localError)

        error += localError

    print("Average error (per item):", error/nrTests)
    
