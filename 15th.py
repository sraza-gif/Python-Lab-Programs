from scipy.optimize import minimize


def function(x):
    return x[0]**2 + 4*x[0] + 5


initial_guess = [0]

result = minimize(function, initial_guess)

print("Minimum value:", result.fun)
print("Value of x at minimum:", result.x)