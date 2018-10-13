
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import pylab

def next_turn(mean, drift, zscores, zscore_drifts, intraturn_variance):
    mean += drift # no intraturn variance for overall mean (yet) for sake of simplicity
    for i in range(0, len(zscores)):
        zscores[i] += np.random.normal(zscore_drifts[i], intraturn_variance)
    return mean, zscores

def draw_number_based_on_zscore(mean, std_dev, zscore):
    return mean + zscore * std_dev

def plot_paths(intraturn_variance, num_turns, mean, drift, std_dev, zscores, zscore_drifts):
    # Initializing list / starting position
    all_incomes = []
    all_zscores = []
    for i in range(0, len(zscores)):
        all_incomes.append([])
        all_zscores.append([])
        all_incomes[i].append(draw_number_based_on_zscore(mean, std_dev, zscores[i]))
        all_zscores[i].append(zscores[i])

    # run simulations
    for i in range(0, num_turns):
        mean, zscores = next_turn(mean, drift, zscores, zscore_drifts, intraturn_variance)
        for i in range(0, len(zscores)):
            all_incomes[i].append(draw_number_based_on_zscore(mean, std_dev, zscores[i]))
            all_zscores[i].append(zscores[i])
    
    # Plotting simulations
    turns = list(range(0, num_turns+1))
    plt.figure(1, figsize=(15, 8))
    
    plt.subplot(221)
    for i in range(0, len(zscores)):
        plt.plot(turns, all_incomes[i], label='Player ' + str(i+1))
    plt.legend(loc='best')
    plt.xlabel('Turn')
    plt.ylabel('Income')
    
    plt.subplot(222)
    for i in range(0, len(zscores)):
        plt.plot(turns, all_zscores[i], label='Player ' + str(i+1))
    plt.legend(loc='best')
    plt.xlabel('Turn')
    plt.ylabel('Zscore / relative ranking')
    
    plt.show()

# Command line arguments
# Read Command line input
num_turns = input('How many turns? (enter integer)\n')
mean = input('Mean? (enter decimal)\n')
drift = input('Drift? (enter decimal)\n')
std_dev = input('Standard deviation? (enter decimal)\n')
intraturn_variance = input('intraturn variance? (enter decimal)\n')

num_players = input('How many players? (enter integer)\n')
zscores = []
zscore_drifts = []
for i in range(0, int(num_players)):
	zscore = input('Starting zscore for player ' + str(i+1) + '? (enter decimal)\n')
	zscores.append(float(zscore))
	zscore_drift = input('Starting drift for player ' + str(i+1) + '? (enter decimal)\n')
	zscore_drifts.append(float(zscore_drift))

print('Running simulations...')

plot_paths(float(intraturn_variance), int(num_turns), float(mean), float(drift), float(std_dev), zscores, zscore_drifts)