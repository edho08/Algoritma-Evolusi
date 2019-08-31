# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:02:05 2019

@author: Edho
"""
from EvolutionAlgorithm.Random.__AbstractRandom import AbstractRandom
import random
import numpy
from numpy.random import choice as random_choice

class Choices(AbstractRandom):
    def __init__(self, choice=[[0,1], [0,1]], probability=[[0.5,0.5], [0.5,0.5]]):
        self._choice=choice
        self._probability=probability
    
    def __call__(self):
        return [ random_choice(param[0], p=param[1], size=1)[0] for param in zip(self._choice, self._probability)]  
    
    def prob(self, z):
        return numpy.prod([param[0][param[1].index(param[2])] if param[2] in param[1] else 0 for param in zip(self._probability, self._choice, z)]) #
    def update_param(self, choice, probability):
        self.__init__(choice, probability)
        
class Choice(Choices):
    def __init__(self, choice=[0,1], probability=[0.5,0.5]):
        super().__init__([choice], [probability])
    def __call__(self):
        return super().__call__()[0]
    def prob(self, z):
        return super().prob(z)
    
class Uniforms(AbstractRandom):
    def __init__(self, randrange=[[0,1]]):
        self._max= [max(i) for i in randrange]
        self._min= [min(i) for i in randrange]
    
    def __call__(self):
        return random.uniform(self._min, self._max)
    
    def prob(self, z):
        pass
class Uniform(Uniforms):
    def __init__(self, randrange=[0,1]):
        super().__init__(randrange, 1)        
    def __call__(self):
        return super().__call__()[0]

class UniformInts(Uniforms):
    def __init__(self, randrange=[0,10], size=10):
        super().__init__(randrange, size)
        
    def __call__(self):
        return random.randint(self._randrange[0], self._randrange[1], self._size)
    
class UniformInt(UniformInts):
    def __init__(self, randrange=[0,10]):
        super().__init__(randrange, 1)
    
    def __call__(self):
        return super().__call__()[0]
        
class Normals(AbstractRandom):
    def __init__(self, mean=0, std=1, size=10):
        self._mean = mean
        self._std = std
        self._size = size
        
    def __call__(self):
        return random.normal(self._mean, self._std, self._size)
    
class Normal(Normals):
    def __init__(self, mean=0, std=1):
        super().__init__(mean, std, 1)
    
    def __call__(self):
        return super().__call__()[0]
        