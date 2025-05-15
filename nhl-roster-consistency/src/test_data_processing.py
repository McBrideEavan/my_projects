import unittest
import pandas as pd
from data_processing import merge_dataframes, feature_engineering, process_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        """Set up sample data for testing."""
        self.schedule_df = pd.DataFrame({
            'gamePk': [1, 2, 3],
            'date': ['2024-10-10', '2024-10-12', '2024-10-14'],
            'homeTeam': ['MIN', 'MIN', 'CHI'],
            'awayTeam': ['CHI', 'WPG', 'MIN'],
            'homeScore': [3, 2, 1],
            'awayScore': [1, 4, 3]
        })

        self.consistency_df = pd.DataFrame({
            'gamePk': [1, 2, 3],
            'consistency': [0.9, 0.85, 0.8]
        })
        print("Sample data created for testing.")

    def test_merge_dataframes(self):
        """Test merging of schedule and consistency dataframes."""
        merged_df = merge_dataframes(self.schedule_df, self.consistency_df)
        self.assertEqual(len(merged_df), 3)
        self.assertIn('consistency', merged_df.columns)
        self.assertIn('homeTeam', merged_df.columns)
        print("Dataframes merged successfully.")

    def test_feature_engineering(self):
        """Test the feature engineering logic."""
        merged_df = merge_dataframes(self.schedule_df, self.consistency_df)
        engineered_df = feature_engineering(merged_df)
        print("Feature engineering applied successfully.")
        
        # Check if new columns are created
        self.assertIn('isHome', engineered_df.columns)
        self.assertIn('isWin', engineered_df.columns)
        self.assertIn('rolling_consistency', engineered_df.columns)
        print("New features added to dataframe.")

        # Validate home/away and win/loss logic
        self.assertEqual(engineered_df.loc[0, 'isHome'], 1)
        self.assertEqual(engineered_df.loc[2, 'isHome'], 0)
        self.assertEqual(engineered_df.loc[0, 'isWin'], 1)
        self.assertEqual(engineered_df.loc[1, 'isWin'], 0)
        print("Home/Away and Win/Loss logic validated.")

    def test_process_data(self):
        """Test the complete data processing pipeline."""
        final_df = process_data(self.schedule_df, self.consistency_df)
        self.assertIn('isHome', final_df.columns)
        self.assertIn('isWin', final_df.columns)
        self.assertIn('rolling_consistency', final_df.columns)
        self.assertEqual(len(final_df), 3)
        print("Data processing pipeline tested successfully.")

if __name__ == '__main__':
    unittest.main()
