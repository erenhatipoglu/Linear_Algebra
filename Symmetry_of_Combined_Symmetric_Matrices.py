import numpy as np

# Transposer
T = T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# creating 2 symmetric matrices
m = 3
A = np.random.randn(m,m)
AtA = A.T@A

B = np.random.randn(m,m)
BtB = B.T@B

# Sum, multiplication and Hadamard
s = AtA + BtB # sum
m = AtA @ BtB # matrix multiplication
h = AtA * BtB # Hadamard (Element-Wise) multiplication

print(s-s.T),
print(m-m.T),
print(h-h.T)
