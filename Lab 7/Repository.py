
from Domain import Element
import random 

class Repo:
    def __init__(self, filePath):
        self.trainData = []
        self.testData = []
        self.filePath = filePath
        
        
    def loadFromFile(self, trainDataRatio):
        '''
        Reads the data file and splits the information according to a ratio
        trainDataRatio - between 0 and 1
        testDataRatio = 1 - trainDataRatio
        '''
        
        file = open(self.filePath, 'r')
        lines = file.readlines()
        file.close()
        
        elem = []
        
        for l in lines:
            x = l.strip().split(' ')
            # Baza de date contine pe fiecare linie 5 atribute si valoarea corespondenta lor
            e = Element(float(x[5]), [float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])])
            
            elem.append(e)
            
        
        random.shuffle(elem)
        trainDataCount = int(trainDataRatio*len(elem))
        self.trainData = elem[:trainDataCount]
        self.testData = elem[trainDataCount:]
        
        
        