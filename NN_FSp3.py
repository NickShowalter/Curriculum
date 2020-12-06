import numpy as np 

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

output = np.dot(weights, inputs) + biases
print(output)

#understanding shape (dimensions) list of list, arrays and matrixes, 
#homologous is same size for each dimension 
#lolol = 3d array 
#tensor can be represeneted as an array 
#dot_product of two vector = a scalar single value 
#first element in dot product is indexed (why we use weights first)
#each vector from 0ith weights multiplied by vecotr of weights
#effects of activation functions, weights and biases.
