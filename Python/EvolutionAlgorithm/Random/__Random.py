# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:02:05 2019

@author: Edho
"""
from EvolutionAlgorithm.Random.__AbstractRandom import AbstractRandom
import numpy.random as random
import numpy
import math
import scipy.stats as stats

class Choices(AbstractRandom):
    def __init__(self, choice=[[0,1], [0,1]], probability=[[0.5,0.5], [0.5,0.5]]):
        self._choice=choice
        self._probability=probability
        self._rand = lambda _choice, _probability, size : random.choice(_choice, p=_probability, size=size)
        self._prob = lambda _choice, _probability, z : [param[0][param[1].index(param[2])] if param[2] in param[1] else 0 for param in zip(self._probability, self._choice, z)]

    def __call__(self, size=10):
        return numpy.array([self._rand(self._choice[i], self._probability[i], size) for i in range(len(self._choice))]).T
    
    def prob(self, z):
        return numpy.array([numpy.prod(self._prob(self._choice, self._probability, i)) for i in z])
        
    def update_param(self, choice, probability):
        self.__init__(choice, probability)
        
class Choice(Choices):
    def __init__(self, choice=[0,1], probability=[0.5,0.5]):
        super().__init__([choice], [probability])
    def __call__(self, size=10):
        return super().__call__(size)
    
class Uniforms(AbstractRandom):
    def __init__(self, randrange=[[0,1], [0,1]]):
        self._max= [max(i) for i in randrange]
        self._min= [min(i) for i in randrange]
        self._rand = lambda _min, _max, size : random.uniform(_min, _max, size) 
        self._prob = numpy.vectorize(lambda _min, _max, z : 1/(_max-_min) if z <_max and z>_min else 0)
    
    def __call__(self, size=10):
        return numpy.array([self._rand(_min, _max, size) for _min, _max in zip(self._min, self._max)]).T
    
    def prob(self, z):
        return numpy.prod(numpy.array([self._prob(_min, _max, _z) for _min, _max, _z in zip(self._min, self._max, z.T)]), axis=0)
        
    def update_param(self, randrange):
        self.__init__(randrange)

class Uniform(Uniforms):
    def __init__(self, randrange=[0,1]):
        super().__init__([randrange])        
    def __call__(self, size=10):
        return super().__call__(size)

class UniformInts(Uniforms):
    def __init__(self, randrange=[[0,10], [0,10]]):
        super().__init__(randrange)
        self._rand = lambda _min, _max, size : random.randint(_min, _max, size)
        self._prob = numpy.vectorize(lambda _min, _max, z : (math.floor(z) - _min + 1)/(_max - _min + 1))
        
    def __call__(self, size=10):
        return numpy.array([ self._rand(_min, _max, size) for _min, _max in zip(self._min, self._max)]).T
    
class UniformInt(UniformInts):
    def __init__(self, randrange=[0,10]):
        super().__init__([randrange])
    
    def __call__(self, size=10):
        return super().__call__(size)
        
class UnivariateNormals(AbstractRandom):
    def __init__(self, mean=[0,0], std=[1, 1]):
        self._mean = mean
        self._std = std
        self._rand = lambda _mean, _std, size : random.normal(_mean, _std, size)
        self._prob = lambda _mean, _std, z : stats.norm.pdf(z, _mean, _std)
        
    def __call__(self, size=10):
        return numpy.array([random.normal(_mean, _std, size) for _mean, _std in zip(self._mean, self._std)]).T
 
    def prob(self, z):
        return numpy.prod(numpy.array([self._prob(_mean, _std, _z) for _mean, _std, _z in zip(self._mean, self._std, z.T)]), axis=0)
    
class UnivariateNormal(UnivariateNormals):
    def __init__(self, mean=0, std=1):
        super().__init__([mean], [std])
    
    def __call__(self):
        return super().__call__(size=10)

class CovarianceMultivariateNormals(AbstractRandom):
    def __init__(self, mean=[0,0], covariance=[[1,0],[0,1]]):
        self._mean = mean
        self._cov = covariance

    def __call__(self, size=10):
        return random.multivariate_normal(self._mean, self._cov, 10)

    def prob(self,z):
        return stats.multivariate_normal.pdf(z, self._mean, self._cov)       
"""
class AMultivariateNormals(CovarianceMultivariateNormals):
    def __init__(self, mean=[0,0], A=[1, 15):
        A = numpy.array([A])
        print(numpy.multiply(A.T, A))
        super().__init__(mean, numpy.multiply(A.T, A))
        self._A = A
"""        
