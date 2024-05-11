import numpy as np
import matplotlib.pyplot as plt

# XY coordinates for the circle
x = np.linspace(-np.pi,np.pi,100)
xy = np.vstack((np.cos(x),np.sin(x))).T
print(np.shape(xy))

# Circle itself
plt.plot(xy[:,0],xy[:,1],"o")

# 2x2 matrix
T = np.array([[1,2],[2,1]])

# MatMul by coordinates
newxy = xy@T # @ is basically shortcut for "np.matmul()"

# Plot new coords
plt.plot(newxy[:,0],newxy[:,1],"o")
plt.show()
