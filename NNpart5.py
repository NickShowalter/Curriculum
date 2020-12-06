#step function is if input is 0 step will be 1
#Used as an activation function is each nueruon is hidden layer has the activation functon input times weight + bias 
#Output will be 0 or 1 

#sigmoid acitivation function great because granularity of output
#calculating loss and optimzation is next steps

#Relu activation function can be granular, solves vanishing gradient problem and it is fast. 

#Non-linear is best for NN because of aproximation issues with linear act functions
#Vital to know how to debug a NN and explain the blackbox


import numpy as np 
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X = [[1, 2.3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]


X, y = spiral_data(100, 3)


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLu()

layer1.forward(X)

#print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)

#https://cs231n.github.io/neural-networks-case-study/#data