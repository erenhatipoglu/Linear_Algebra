import numpy as np

# Three random vectors, one is dependent on another
a = np.random.randn(15)
b = np.random.randn(15)
c = np.random.randn(1) * a  # Random scalar

# Dot products (I will assign the 'aTb' etc. variables rather than 'a_dot' or something, as dot product's notation is this.)

aTb = np.dot(a,b)
aTc = np.dot(a,c)

# Demonstration of the (in)equalities

print(f"{np.abs(aTb):.5f}, {np.linalg.norm(a)*np.linalg.norm(b):.5f}") # Inequality Case
# For inequality, the left hand side of the equation, which is the DOT product of A and B is less
# than this number, is smaller than the product of the magnitudes (lengths) of A and B.

print(f"{np.abs(aTc):.10f}, {np.linalg.norm(a)*np.linalg.norm(c):.10f}") # Equality
# For equality, the numbers are the same because A and C form a linearly dependent set.

