from controller import Controller
from model import FuzzyDescriptions
from view import View

if __name__ == '__main__':
    temperature = FuzzyDescriptions()
    humidity = FuzzyDescriptions()
    time = FuzzyDescriptions()
    rules = []

    ctrl = Controller()
    view = View(ctrl)

    view.readProblemData([temperature, humidity, time], rules)
    ctrl.setData(temperature, humidity, time, rules)

    
    inputFile = open('input.in', 'r') 
    outputFile = open('output.out', 'w')

    x = int(inputFile.readline())
    for _ in range(x):
        values = inputFile.readline().split()
        res = str(view.compute({'humidity': int(values[0]), 'temperature': int(values[1])}))
        print("Humidity: " + values[0] + "\nTemperature: " + values[1] + "\nOperating time: " + res + "\n")
        outputFile.write(res + '\n')

    inputFile.close()
    outputFile.close()