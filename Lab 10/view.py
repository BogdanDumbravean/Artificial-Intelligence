from model import FuzzyRule

class View:
    def __init__(self, controller):
        self.controller = controller

    def compute(self, inputs):
        return self.controller.compute(inputs)


    def trapezoidal(self, a, b, c, d):
        return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))

    def triangular(self, a, b, c):
        return lambda x: max(0, min((x - a) / (b - a), 1, (c - x) / (c - b)))

    def inverse_line(self, a, b):
        return lambda val: val * (b - a) + a

    def inverse_tri(self, a, b, c):
        return lambda val: (self.inverse_line(a, b)(val) + self.inverse_line(c, b)(val)) / 2


    def readProblemData(self, descriptions, rules):
        problemFile = open('problem.in', 'r') 
        
        for d in descriptions:
            self.readDescription(problemFile, d)
        self.readRules(problemFile, rules)

        problemFile.close()

    def readRules(self, problemFile, rules):
        x = int(problemFile.readline())
        for _ in range(x):
            a = problemFile.readline().split(';')
            rules.append(FuzzyRule(eval(a[0]), eval(a[1])))

    def readDescription(self, problemFile, description):
        x = int(problemFile.readline())
        for _ in range(x):
            name = problemFile.readline().rstrip()
            valueLine = problemFile.readline()
            values = [int(val) for val in valueLine.split()]
            if(len(values) == 3):
                description.add_region(name, self.triangular(*values))
            elif(len(values) == 4):
                description.add_region(name, self.trapezoidal(*values))
            elif(len(values) == 5):
                description.add_region(name, self.triangular(*values[:3]), self.inverse_line(*values[3:]))
            elif(len(values) == 6):
                description.add_region(name, self.triangular(*values[:3]), self.inverse_tri(*values[3:]))