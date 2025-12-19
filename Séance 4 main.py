#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats

#https://docs.scipy.org/doc/scipy/reference/stats.html

def plot_discrete_distributions():
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Discrete Statistical Distributions', fontsize=16)
    axes = axes.flatten()

    # 1. Dirac Distribution [cite: 21]
    # Modeled as probability 1 at a single value (e.g., k=5)
    x_dirac = [4, 5, 6]
    y_dirac = [0, 1, 0]
    axes[0].stem(x_dirac, y_dirac, basefmt=" ")
    axes[0].set_title('Dirac Distribution (at 5)')

    # 2. Discrete Uniform Distribution [cite: 23]
    # Example: Rolling a die (1 to 6)
    low, high = 1, 6
    x_uni = np.arange(low, high + 1)
    y_uni = stats.randint.pmf(x_uni, low, high + 1)
    axes[1].stem(x_uni, y_uni, basefmt=" ")
    axes[1].set_title('Discrete Uniform (1 to 6)')

    # 3. Binomial Distribution [cite: 24]
    # Example: 10 trials, probability 0.5
    n, p = 10, 0.5
    x_bin = np.arange(0, n + 1)
    y_bin = stats.binom.pmf(x_bin, n, p)
    axes[2].stem(x_bin, y_bin, basefmt=" ")
    axes[2].set_title(f'Binomial (n={n}, p={p})')

    # 4. Poisson Distribution [cite: 25]
    # Example: lambda = 3
    mu = 3
    x_pois = np.arange(0, 15)
    y_pois = stats.poisson.pmf(x_pois, mu)
    axes[3].stem(x_pois, y_pois, basefmt=" ")
    axes[3].set_title(f'Poisson (mu={mu})')

    # 5. Zipf (Zeta) Distribution [cite: 26]
    # Example: a = 2 (Shape parameter)
    a = 2
    x_zipf = np.arange(1, 15)
    y_zipf = stats.zipf.pmf(x_zipf, a)
    axes[4].stem(x_zipf, y_zipf, basefmt=" ")
    axes[4].set_title(f'Zipf (a={a})')

    # Hide empty 6th subplot
    axes[5].axis('off')

    plt.tight_layout()
    plt.show()

# Run the function
plot_discrete_distributions()


def plot_continuous_distributions():
    # Set up the figure for continuous variables
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Continuous Statistical Distributions', fontsize=16)
    axes = axes.flatten()
    
    # Generate X axis values (continuous range)
    x = np.linspace(0, 10, 1000)

    # 1. Normal Distribution 
    mu, sigma = 5, 1.5
    y_norm = stats.norm.pdf(x, loc=mu, scale=sigma)
    axes[0].plot(x, y_norm, 'r-', lw=2)
    axes[0].set_title(f'Normal Distribution ($\mu$={mu}, $\sigma$={sigma})')

    # 2. Log-normal Distribution 
    s = 0.8
    y_lognorm = stats.lognorm.pdf(x, s)
    axes[1].plot(x, y_lognorm, 'b-', lw=2)
    axes[1].set_title(f'Log-normal Distribution (s={s})')

    # 3. Continuous Uniform Distribution
    loc, scale = 2, 5  
    y_uniform = stats.uniform.pdf(x, loc=loc, scale=scale)
    axes[2].plot(x, y_uniform, 'g-', lw=2)
    axes[2].set_title('Continuous Uniform (2 to 7)')

    # 4. Chi-squared Distribution 

    df = 4
    y_chi2 = stats.chi2.pdf(x, df)
    axes[3].plot(x, y_chi2, 'm-', lw=2)
    axes[3].set_title(f'Chi-squared ($\chi^2$) (k={df})')

    # 5. Pareto Distribution
    b = 3
    y_pareto = stats.pareto.pdf(x, b)
    axes[4].plot(x, y_pareto, 'k-', lw=2)
    axes[4].set_title(f'Pareto (b={b})')
    
    axes[5].axis('off')

    plt.tight_layout()
    plt.show()

# Run the function
plot_continuous_distributions()


def print_stats(name, dist_obj):
    mean = dist_obj.mean()
    std = dist_obj.std()
    print(f"--- {name} ---")
    print(f"Mean:      {mean:.4f}")
    print(f"Std Dev:   {std:.4f}\n")

print("STATISTICS \n")

# --- DISCRETE VARIABLES ---
# For Dirac, as a constant value
# Mean = 5, Std = 0
print("--- Dirac (at 5) ---")
print("Mean:      5.0000")
print("Std Dev:   0.0000\n")

print_stats("Discrete Uniform (1-6)", stats.randint(1, 7))
print_stats("Binomial (n=10, p=0.5)", stats.binom(10, 0.5))
print_stats("Poisson (mu=3)", stats.poisson(3))

print_stats("Zipf (a=3)", stats.zipf(3))

print_stats("Normal (mu=5, sigma=1.5)", stats.norm(5, 1.5))
print_stats("Log-normal (s=0.8)", stats.lognorm(0.8))
print_stats("Continuous Uniform (2-7)", stats.uniform(2, 5))
print_stats("Chi-squared (k=4)", stats.chi2(4))
print_stats("Pareto (b=3)", stats.pareto(3))