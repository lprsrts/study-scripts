import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def central_limit_theorem_demo(n_samples=1000, sample_size=30, distribution='uniform'):
    """Demonstrates the Central Limit Theorem by summing random variables and standardizing the result."""
    sample_sums = []
    all_samples = []

    for _ in range(n_samples):
        if distribution == 'uniform':
            sample = np.random.uniform(0, 1, sample_size)
        elif distribution == 'exponential':
            sample = np.random.exponential(1, sample_size)
        elif distribution == 'poisson':
            sample = np.random.poisson(3, sample_size)
        else:
            raise ValueError("Unsupported distribution type")

        sample_sums.append(np.sum(sample))
        all_samples.extend(sample)  # Store all values in a flat list

    # Standardizing the sums
    mean = np.mean(sample_sums)
    std = np.std(sample_sums)
    standardized_sums = [(x - mean) / std for x in sample_sums]

    return standardized_sums, all_samples

# Parameters
n_samples = 1000
sample_size = 30

# Generate standardized sample sums and individual samples for different distributions
uniform_sums, uniform_samples = central_limit_theorem_demo(n_samples, sample_size, 'uniform')
exponential_sums, exponential_samples = central_limit_theorem_demo(n_samples, sample_size, 'exponential')
poisson_sums, poisson_samples = central_limit_theorem_demo(n_samples, sample_size, 'poisson')

# Plot histograms and individual distributions
plt.figure(figsize=(12, 6))

def plot_distribution(ax, samples, sums, title, color):
    ax.hist(samples, bins=30, density=True, alpha=0.3, color=color, edgecolor='black', label='Original Samples')
    ax.hist(sums, bins=30, density=True, alpha=0.7, color=color, edgecolor='black', label='Standardized Sum of Samples')

    # Overlay standard normal distribution
    x = np.linspace(-4, 4, 100)
    ax.plot(x, stats.norm.pdf(x, 0, 1), 'k--', label='Standard Normal')

    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    ax.legend()

plt.subplot(1, 3, 1)
plot_distribution(plt.gca(), uniform_samples, uniform_sums, "Uniform Distribution", 'b')

plt.subplot(1, 3, 2)
plot_distribution(plt.gca(), exponential_samples, exponential_sums, "Exponential Distribution", 'g')

plt.subplot(1, 3, 3)
plot_distribution(plt.gca(), poisson_samples, poisson_sums, "Poisson Distribution", 'r')

plt.tight_layout()
plt.show()
