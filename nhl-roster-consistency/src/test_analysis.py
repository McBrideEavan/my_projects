import unittest
import pandas as pd
from data_processing import process_data
from analysis import analyze_correlation, plot_consistency_vs_wins, plot_rolling_consistency
import matplotlib.pyplot as plt

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample DataFrames for testing
        schedule_df = pd.DataFrame({
            'gamePk': [1, 2, 3, 4, 5],
            'homeTeam': ['MIN', 'MIN', 'MIN', 'MIN', 'MIN'],
            'awayTeam': ['CHI', 'STL', 'DAL', 'WPG', 'NSH'],
            'homeScore': [4, 2, 3, 5, 1],
            'awayScore': [3, 3, 2, 2, 3],
         'date': pd.date_range(start='2025-10-01', periods=5)
     })

        consistency_df = pd.DataFrame({
            'gamePk': [1, 2, 3, 4, 5],
            'consistency': [0.8, 0.7, 0.9, 0.85, 0.6]
        })
    
        # Use the real processing function to generate rolling_consistency
        self.df = process_data(schedule_df, consistency_df)


    def test_analyze_correlation(self):
        """Test the Pearson correlation calculation."""
        correlation = analyze_correlation(self.df)
        self.assertIsInstance(correlation, float)
        self.assertGreaterEqual(correlation, -1)
        self.assertLessEqual(correlation, 1)

    def test_plot_consistency_vs_wins(self):
        """Test that the plot is generated without errors."""
        try:
            plot_consistency_vs_wins(self.df)
            plt.close()  # Close plot after test
        except Exception as e:
            self.fail(f"plot_consistency_vs_wins raised an exception: {e}")

    def test_plot_rolling_consistency(self):
        """Test that the rolling consistency plot is generated correctly."""
        try:
            plot_rolling_consistency(self.df)
            plt.close()  # Close plot after test
        except Exception as e:
            self.fail(f"plot_rolling_consistency raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
