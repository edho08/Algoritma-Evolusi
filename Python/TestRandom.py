import EvolutionAlgorithm.Random as Random

choices = Random.Choices()
a = choices()
prob = choices.prob(a)
print(a)
print(prob)

choice = Random.Choice()
a = choice()
prob = choice.prob(a)
print(a)
print(prob)

uniforms = Random.Uniforms([[0,10], [0,10]])
a = uniforms()
prob = uniforms.prob(a)
print(a)
print(prob)

uniform = Random.Uniform([0, 10])
a = uniform()
prob = uniform.prob(a)
print(a)
print(prob)

uniformints = Random.UniformInts()
a = uniformints()
prob = uniformints.prob(a)
print(a)
print(prob)

CovarianceMultivariateNormals = Random.CovarianceMultivariateNormals()
a = CovarianceMultivariateNormals()
prob = CovarianceMultivariateNormals.prob(a)
print(a)
print(prob)

UnivariateNormals = Random.UnivariateNormals()
a = UnivariateNormals()
prob = UnivariateNormals.prob(a)
print(a)
print(prob)


UniqueUniformsInt = Random.UniqueUniformsInt(randrange=[0, 100])
a = UniqueUniformsInt()
prob = UniqueUniformsInt.prob(a)
print(a)
print(prob)
