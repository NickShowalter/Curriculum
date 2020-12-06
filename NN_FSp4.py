import numpy as np 

np.random.seed(0)

X = [[1.0, 2.0, 3.0, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases 


Layer1 = Layer_Dense(4,5)
Layer2 = Layer_Dense(5,3)

Layer1.forward(X)
#print(Layer1.output)
Layer2.forward(Layer1.output)
print(Layer2.output)




         





#bigger batches mean more paralell operations we can run.
#batching helps with generalization 
#too many batches will cause over generalization (32 is commmon batch size)
#matrix product 
#dimensions are not alligned (shape error) we are trying to do inputs * weights using matrix *
#resolve shape problem by using transpose which will switch rows and columns 
#adding layer consists of intitalization of weights and biases (W: -1 to 1 for exploding outputs)
#Normalization 
#randn is a gaussian distribution surrounded around 
#pass paremeters in randn are the shape rather then tuples of the shape 
#shape weights by # of inputs and neurons so we do not have to do a transpose 
#pass in input data to obtain whatever shape you want for pass through 