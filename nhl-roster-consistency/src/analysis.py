import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

def analyze_correlation(processed_df: pd.DataFrame) -> float:
    """
    Analyze the correlation between roster consistency and game outcomes.

    Parameters:
    - processed_df (pd.DataFrame): The processed DataFrame containing features and game results.

    Returns:
    - float: The Pearson correlation coefficient between consistency and wins.
    """
    print("Analyzing correlation between consistency and win percentage...")
    correlation, _ = pearsonr(processed_df['consistency'], processed_df['isWin'])
    print(f"Correlation coefficient: {correlation}")
    return correlation


def plot_consistency_vs_wins(processed_df: pd.DataFrame):
    """
    Generate a scatter plot to visualize consistency against win percentage.

    Parameters:
    - processed_df (pd.DataFrame): The processed DataFrame containing features and game results.
    """
    print("Plotting consistency vs. wins...")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='consistency', y='isWin', data=processed_df)
    plt.title('Roster Consistency vs. Win Percentage')
    plt.xlabel('Roster Consistency')
    plt.ylabel('Win (1) / Loss (0)')
    plt.show()


def plot_rolling_consistency(processed_df: pd.DataFrame):
    """
    Generate a line plot for rolling consistency over the season.

    Parameters:
    - processed_df (pd.DataFrame): The processed DataFrame containing features and game results.
    """
    print("Plotting rolling consistency over the season...")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='rolling_consistency', data=processed_df, marker='o')
    plt.title('Rolling Consistency Over Season')
    plt.xlabel('Game Date')
    plt.ylabel('5-Game Rolling Consistency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
