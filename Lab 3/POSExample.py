# -*- coding: utf-8 -*-
"""
Determine the minimum for Schaffer's function of two variables
on [-10,10]x[-10,10] using a PSO (particle swarm optimisation) algorithm.

see for Schaffer's function:
    http://deap.gel.ulaval.ca/doc/0.8/api/benchmarks.html


The result for this problem should be: x=(0,0) with f(x)=0

"""

from random import randint, random
from operator import add
from math import sin, pow

class particle:
    """ The class that implements a particle """
    def __init__(self, l, vmin, vmax):
        """ constructor

        input--
          l: the number of components
          vmin: the minimum possible value 
          vmax: the maximum possible value
        """
        self._position = [ (random()*(vmax-vmin)+vmin) for x in range(l) ]
        self.evaluate()
        self.velocity = [ 0 for i in range(l)]
        
        #the memory of that particle
        self._bestPosition=self._position.copy()
        self._bestFitness=self._fitness
        
    def fit(self,position):
        """
        Determine the fitness of a particle. Lower is better.(min problem)
        For this problem we have the Schaffer's function

        input --
            position: the position of the particle we wish to evaluate
        """
        n=len(position)
        f=0
        for i in range(n-1):
            y=pow(position[i],2)+pow(position[i+1],2)
            f=f+pow(y,0.25)*(pow(sin(50*pow(y,0.1)),2)+1)
        return f

    def evaluate(self):
        """ evaluates the particle """
        self._fitness = self.fit(self._position)

    @property
    def position(self):
        """ getter for position """
        return self._position

    @property
    def fitness(self):
        """ getter for fitness """
        return self._fitness

    @property
    def bestPosition(self):
        """ getter for best position """
        return self._bestPosition

    @property
    def bestFitness(self):
        """getter for best fitness """
        return self._bestFitness
    
    @position.setter
    def position(self, newPosition):
        self._position=newPosition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self._fitness<self._bestFitness):
            self._bestPosition = self._position
            self._bestFitness  = self._fitness

def population(count, l, vmin, vmax):
    """
    Create a number of particles (i.e. a population).

    input --
       count: the number of individuals in the population
       l: the number of values in the position of a particle
       vmin: the minimum possible value 
       vmax: the maximum possible value

    output --
       the random created population of count particles
    """
    return [ particle(l, vmin, vmax) for x in range(count) ]


def selectNeighbors(pop, nSize):
    """  the selection of the neighbours for each particle
    
    input --
       pop: current population
       nSize: the number of neighbours of a particle

    output--
       ln: list of neighblours for each particle
    """

    if (nSize>len(pop)):
        nSize=len(pop)

    # Attention if nSize==len(pop) this selection is not a propper one
    # use a different approach (like surfle to form a permutation)
    neighbors=[]
    for i in range(len(pop)):
        localNeighbor=[]
        for j in range(nSize):
            x=randint(0, len(pop)-1)
            while (x in localNeighbor):
                x=randint(0, len(pop)-1)
            localNeighbor.append(x)
        neighbors.append(localNeighbor.copy())
    return neighbors
            
    
def iteration(pop, neighbors, c1, c2, w ):
    """
    an iteration

    pop: the current state of the population
    

    for each particle we update the velocity and the position
    according to the particle's memory and the best neighbor's position 
    """
    bestNeighbors=[]
    #determine the best neighbor for each particle
    for i in range(len(pop)):
        bestNeighbors.append(neighbors[i][0])
        for j in range(1,len(neighbors[i])):
            if (pop[bestNeighbors[i]].fitness>pop[neighbors[i][j]].fitness):
                bestNeighbors[i]=neighbors[i][j]
                
    #update the velocity for each particle
    for i in range(len(pop)):
        for j in range(len(pop[0].velocity)):
            newVelocity = w * pop[i].velocity[j]
            newVelocity = newVelocity + c1*random()*(pop[bestNeighbors[i]].position[j]-pop[i].position[j])    
            newVelocity = newVelocity + c2*random()*(pop[i].bestPosition[j]-pop[i].position[j])
            pop[i].velocity[j]=newVelocity
    
    #update the position for each particle
    for i in range(len(pop)):
        newPosition=[]
        for j in range(len(pop[0].velocity)):
            newPosition.append(pop[i].position[j]+pop[i].velocity[j])
        pop[i].position=newPosition
    return pop

def main(noIteratii=100):
    #PARAMETERS:
    
    #number of particles
    noParticles = 100
    #individual size
    dimParticle = 2
    #the boundries of the search interval
    vmin = -100
    vmax = -10
    #specific parameters for PSO
    w=1.0
    c1=1.
    c2=2.5
    sizeOfNeighborhood=20
    P = population(noParticles, dimParticle, vmin, vmax)

    # we establish the particles' neighbors 
    neighborhoods=selectNeighbors(P,sizeOfNeighborhood)
    
    for i in range(noIteratii):
        P = iteration(P, neighborhoods, c1,c2, w/(i+1))

        #print the best individual
        best = 0
        for i in range(1, len(P)):
            if (P[i].fitness<P[best].fitness):
                best = i
        
        fitnessOptim=P[best].fitness
        individualOptim=P[best].position
        print('Result: The detectet minimum point is (%3.2f %3.2f) \n with function\'s value %3.2f'% \
              (individualOptim[0],individualOptim[1], fitnessOptim) )
    
    
    
main()
    
    