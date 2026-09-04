import numpy as np
from scipy.integrate import quad
from scipy.misc import derivative

# Function
def f(x):
    return x ** 2 + 3 * x + 2

x = 2

# Numerical differentiation
differentiation = derivative(f, x, dx=1e-6)

# Numerical integration
integration, error = quad(f, 0, 2)

print("Function: f(x) = x^2 + 3x + 2")

print("\nDerivative at x =", x, ":", differentiation)

print("\nIntegration from 0 to 2:", integration)
print("Estimated error:", error)