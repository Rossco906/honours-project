from .parameters import params
import random 

class Individual:
    def __init__(self):
        self.chromosome = list(range(1, params["numGenes"]+1)) #ordered permutations (shuffled in initialise)
        self.fitness = None
        self.hardConstraintFitness = None
        self.drones = None
        self.phenotype = None
    def initialise(self):
        #random.seed(1001)
        random.shuffle(self.chromosome)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.chromosome)