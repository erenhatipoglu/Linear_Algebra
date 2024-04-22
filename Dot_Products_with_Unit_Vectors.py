import numpy as np

v1 = np.round(20*np.random.randn(4))
v2 = np.round(20*np.random.randn(4))

# computing the lengths of the individual vectors
# and magnitude (length) of their dot product
v1_len = np.sqrt(np.dot(v1,v2))
v2_len = np.sqrt(np.dot(v1,v2))
dot_mag= np.abs(np.dot(v1,v2))

tobeprinted = [v1_len,v2_len,dot_mag]

for i in tobeprinted:
    print(f"{i:.4f}", end=" ")  # I was just trying to be cool =)

# Normalize the vectors (make their magnitude/length = 1)
v1mu = v1/v1_len
v2mu = v2/v2_len

print(v1mu,v2mu)

# Magnitude of the dot product:
dot_mag = np.abs(np.dot(v1mu,v2mu))
print(dot_mag)
