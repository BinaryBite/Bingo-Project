import matplotlib.pyplot as plt
from scipy.stats import describe
import numpy as np
import pandas as pd

###############################################################################################################

def calculate_centrality(bingo_results, full_results):
    centrality_figures = []
    
    num_cols = bingo_results.shape[1]

    for num_called in range(0, num_cols + 1):
        # Assuming you want to calculate statistics for both bingo and full results at each call number
        bingo_data = bingo_results[:, num_called - 1]
        full_data = full_results[:, num_called - 1]

        # Calculate statistics for bingo data
        bingo_stats = describe(bingo_data)

        # Calculate statistics for full data
        full_stats = describe(full_data)

        centrality_figures.append({
            'Number Called': num_called,
            'Bingo_Mean': bingo_stats.mean,
            'Bingo_Variance': bingo_stats.variance,
            'Bingo_Skewness': bingo_stats.skewness,
            'Bingo_Kurtosis': bingo_stats.kurtosis,
            'Bingo_Min': bingo_stats.minmax[0],
            '25th Percentile': np.percentile(bingo_data, 25),
            'Bingo_Median': np.median(bingo_data),
            '75th Percentile': np.percentile(bingo_data, 75),
            'Bingo_Max': bingo_stats.minmax[1],

            'Full_Mean': full_stats.mean,
            'Full_Variance': full_stats.variance,
            'Full_Skewness': full_stats.skewness,
            'Full_Kurtosis': full_stats.kurtosis,
            'Full_Min': full_stats.minmax[0],
            '25th Percentile': np.percentile(full_data, 25),
            'Full_Median': np.median(full_data),
            '75th Percentile': np.percentile(full_data, 75),
            'Full_Max': full_stats.minmax[1],
        })

    return centrality_figures

def plot_combined_analysis(bingo_results, full_results):
        x_values = np.arange(1, bingo_results.shape[1] + 1)

        # Average counts
        avg_bingo = np.mean(bingo_results, axis=0)
        avg_fullhouse = np.mean(full_results, axis=0)

        # Standard deviations
        std_bingo = np.std(bingo_results, axis=0)
        std_fullhouse = np.std(full_results, axis=0)

        # Minimum and maximum counts
        min_bingo = np.min(bingo_results, axis=0)
        max_bingo = np.max(bingo_results, axis=0)
        min_fullhouse = np.min(full_results, axis=0)
        max_fullhouse = np.max(full_results, axis=0)

        # Line plot with shaded area for standard deviation
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, avg_bingo, label='Average BINGO', color='blue')
        plt.fill_between(x_values, avg_bingo - std_bingo, avg_bingo + std_bingo, color='blue', alpha=0.2)
        plt.plot(x_values, avg_fullhouse, label='Average Full-House', color='green')
        plt.fill_between(x_values, avg_fullhouse - std_fullhouse, avg_fullhouse + std_fullhouse, color='green', alpha=0.2)

        # Dotted lines for minimum and maximum counts
        plt.plot(x_values, min_bingo, '--', color='blue', alpha=0.5)
        plt.plot(x_values, max_bingo, '--', color='blue', alpha=0.5)
        plt.plot(x_values, min_fullhouse, '--', color='green', alpha=0.5)
        plt.plot(x_values, max_fullhouse, '--', color='green', alpha=0.5)

        plt.title('Bingo Simulation Analysis')
        plt.xlabel('Number of Called Numbers')
        plt.ylabel('Number of Winning Cards')
        plt.legend()
        plt.show()
        
         # Histogram of cards with bingo after x numbers called from all simulations

        bingo_frequencies = np.sum(bingo_results > 1, axis=0)
        bingo_percentages = (bingo_frequencies / len(bingo_results)) * 100

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(bingo_frequencies) + 1), bingo_percentages, color = 'blue', alpha=0.7, label='Bingo Frequencies')
        plt.title('Histogram of Number of Bingos After Numbers Called')
        plt.xlabel('Numbers Called')
        plt.ylabel('Percentage of Bingos')
        plt.ylim(0,100)
        plt.legend()
        plt.show()
        
        full_frequencies = np.sum(full_results > 1, axis=0)
        full_percentages = (full_frequencies / len(full_results)) * 100

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(full_frequencies) + 1), full_percentages, color = 'green', alpha=0.7, label='Full Frequencies')
        plt.title('Histogram of Number of Fullhouses After Numbers Called')
        plt.xlabel('Numbers Called')
        plt.ylabel('Percentage of Fullhouses')
        plt.ylim(0,100)
        plt.legend()
        plt.show()
    # Convert centrality figures to a DataFrame
        centrality_df = pd.DataFrame(calculate_centrality(bingo_results, full_results))
        return centrality_df