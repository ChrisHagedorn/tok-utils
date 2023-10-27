import random
import matplotlib.pyplot as plt

# Parameters
initial_investment = 10000  # Initial investment
years = 5  # Number of years to simulate
num_simulations = 10000  # Number of simulations
mean_rois = [0.12, 0.15, 0.10]  # List of mean annual ROIs for different advertising opportunities
volatility = 0.2  # Annual ROI volatility (standard deviation)

# Lists to store simulation results for each opportunity
investment_values = [[] for _ in mean_rois]

# Perform Monte Carlo simulations for each advertising opportunity
for i, mean_roi in enumerate(mean_rois):
    for _ in range(num_simulations):
        investment = initial_investment
        for year in range(years):
            # Generate a random ROI based on a normal distribution
            roi = random.gauss(mean_roi, volatility)
            investment *= (1 + roi)
        investment_values[i].append(investment)

# Plot the results as histograms for each opportunity
plt.figure(figsize=(10, 6))
for i, mean_roi in enumerate(mean_rois):
    plt.hist(investment_values[i], bins=50, alpha=0.7, label=f'Opportunity {i + 1}: ROI {mean_roi}', edgecolor='black')

plt.xlabel('Investment Value')
plt.ylabel('Frequency')
plt.title('Monte Carlo Simulation of Investment ROI for Advertising Opportunities')
plt.legend()
plt.grid(True)

plt.show()