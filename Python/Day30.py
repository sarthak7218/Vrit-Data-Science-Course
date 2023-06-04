import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(42)

# Generate samples fom an eponential distribution
population = np.random.exponential(scale=1, size=100000)

# Plot the population distribution
plt.figure(figsize=(8, 6))
plt.hist(population, bins=50, density=True, color='blue', alpha=0.6)
plt.title('Population Distribution (Exponential)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()


# Sample sie to consider
sample_sizes = [5, 10, 30, 50, 100, 1000]

# Generate samples of different sizes and calculate sample means
sample_means = []
for n in sample_sizes:
    samples = np.random.choice(population, size=(1000, n), replace=True)
    means = np.mean(samples, axis=1)
    sample_means.append(means)
    
# Plot the distribution of sampe means for each sample size
plt.figure(figsize=(12, 8))
for i, means in enumerate(sample_means):
    plt.subplot(2, 3, i+1)
    plt.hist(means, bins=30, density=True, color='green', alpha=0.6)
    plt.title(f'Sample Size: {sample_sizes[i]}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
plt.tight_layout()
plt.show()


## Hypotheis Testing

# Generate x values for the standard normal distribution
x = np.linspace(-4, 4, 1000)

# Calculate the critical z-scores
# ppf = percent point function
z_critical = stats.norm.ppf(1-0.05/2)

# Plot the standard normal distribution
plt.figure(figsize=(8, 6))
plt.plot(x, stats.norm.pdf(x), 'black', lw=2, label = 'Standard Normal Distribution')

# Shade the rejection region
plt.fill_between(x, stats.norm.pdf(x), where= (x <= -z_critical) | (x >= z_critical), color='red', alpha=1, label='Rejection Region')

# Add labels and title
plt.title('Standard Normal Distribution with Rejection Region')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.show()


## Perform Test Statistic and Calculate P-value

# Sample data (weights)
sample = [150, 155, 160, 170, 175, 180]

# Sample statistics
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
sample_size = len(sample)

# Hypothesized mean
mu_0 = 165

# Calculate the z-score
z_score = (sample_mean - mu_0) / (sample_std / np.sqrt(sample_size))

# Calculate the p-value
p_value = 2 * (1 - stats.norm.cdf(np.abs(z_score)))

p_value








