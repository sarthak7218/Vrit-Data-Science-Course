import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate x values for the standard normal distribution
x = np.linspace(-4, 4, 1000)

# Calculate the probability dencity function (PDF) for each x value
pdf = stats.norm.pdf(x)

