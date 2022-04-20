import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

A = np.array([[1,2], [3,4]])
A.shape

B = np.array([[5, 6], [7, 8]])
print(B)
np.ndim(B)
B.shape

np.dot(A, B)
