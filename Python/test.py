import numpy as np
from scipy import optimize

# Define a function to minimize
def objective_func(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2

# Initial guess
initial_guess = [0, 0]

# Minimize the function using the Nelder-Mead method
result = optimize.minimize(objective_func, initial_guess, method='Nelder-Mead')

# Print the optimization result
print("Optimization Result:")
print(result)
print("Optimized Solution:")
print(result.x)
