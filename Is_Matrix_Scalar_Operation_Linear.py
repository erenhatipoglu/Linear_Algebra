import numpy as np

# Creating the matrices
A = np.random.randn(5,7)
B = np.random.randn(5,7)

scalar = np.random.randn()

# Computing the both sides of the equation
Left = scalar * (A+B)
Right = scalar*A + scalar*B

print(Left)
print(Right)

print(Left-Right) # There are real zeros in this matrix

# So essentially this confirms that we get our zeros matrix,
# which tells us that these two quantities are the same.

# Therefore scalar matrix multiplication is a linear operation.
