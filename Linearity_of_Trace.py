
import numpy as np

A = np.random.randn(4,4)
B = np.random.randn(4,4)

scalar_or_lambda = np.random.randn()

print("trace(A+B) = " + str(np.trace(A+B)))
print("trace(A) + trace(B) = " + str(np.trace(A) + np.trace(B)))

# trace of A plus B and the trace of A plus the trace of B is that these both match these numbers

print(" ")

print("tr(scalar_or_lambda*A) = " + str(np.trace(scalar_or_lambda*A)))
print("scalar_or_lambda*tr(A) = " + str(scalar_or_lambda*np.trace(A)))

# And here with the trace of Lambda Times A versus Lambda Times, the trace of A, we see again that these
