import numpy as np

a = np.random.randn(5)
b = np.random.randn(5)

scalar1 = np.random.randn(1)
scalar2 = np.random.randn(1)

# Computing the dot product
aTb = np.dot(a,b)

# Dot product between scaled vectors

saTb = np.dot(a*scalar1,b*scalar2)

print(f"Original dot product:, {aTb:.4f}")
print(f"Scaled dot product:, {saTb:.4f}")
