import EvolutionAlgorithm.Random as Random
import random
import numpy

class AbstractOperator:
    def __init__(self, chance=0):
        self._chance = chance
        
    def __call__(self):
        pass
    
class AbstractMutator(AbstractOperator):
    def __init__(self, chance=0.1):
        super().__init__(chance)
        self.__mutation_randomizer = Random.Choice([0,1], [1-chance, chance])
    
    def _mutate(self, number):
        pass
                
    def __call__(self, Locus):
        mutate_point = self.__mutation_randomizer(len(Locus.genes)).T.toList()[0]
        Locus._genes = numpy.array([self._mutate(gene) if mutate else gene for gene, mutate in zip(Locus._genes, mutate_point)])
        return Locus
            
class BinaryMutator(AbstractMutator):
    def __init__(self, chance=0.1):
        super().__init__(chance)

    def _mutate(self, number):
         return 0 if number else 1
     
class RealNumberMutator(AbstractMutator):
    def __init__(self, chance=0.1, random_generator=Random.UnivariateNormal()):
        super().__init__(chance)
        self._random_generator= random_generator
        
    def _mutate(self, number):
        return number + self._random_generator(1).toList()[0][0]
        
class AbstractCrossover(AbstractOperator):
    def __init__(self, chance=0.2):
        super().__init__(chance)
        self.__mutation_randomizer = Random.Choice([0,1], [1-chance, chance])
        
    def _crossover(self, Locus1, Locus2):
        pass
    
    def __call__(self, Locus1, Locus2):
        if random.random()<self._chance:
            return self._crossover(Locus1, Locus2)
        return Locus1, Locus2
    
class MultiPointCrossover(AbstractCrossover):
    pass
    