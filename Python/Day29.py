import numpy as np
import matplotlib.pyplot as plt

## Uniform Distribution

# Set the seed for reproductivity
np.random.seed(42)

# Generate samples from a uniform distribution (0, 1)
population = np.random.uniform(0, 1, size=100000)

# Plot the population distribution
plt.figure(figsize=(8, 6))
plt.hist(population, bins=50, density=True, color='blue', alpha=1)
plt.title('Population Distribution (Uniform)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()


# Sample sizes to consider
sample_sizes = [5, 10, 30, 100, 1000]

# Generate samples of different sizes and calculate sample means
sample_means = []
for n in sample_sizes:
    samples = np.random.choice(population, size=(1000, n), replace=True)
    means = np.mean(samples, axis = 1)
    sample_means.append(means)
    
# Plot the distribution of sample means for each sample size
plt.figure(figsize=(12, 8))
for i, means in enumerate (sample_means):
    plt.subplot(2, 3, i+1)
    plt.hist(means, bins=30, density=True, color='green', alpha=0.6)
    plt.title(f'Sample Size: {sample_sizes[i]}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
plt.tight_layout()
plt.show()


