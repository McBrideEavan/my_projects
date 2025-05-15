from data_collection import collect_data
import pandas as pd

# Constants
TEAM_CODE = "MIN"       # Minnesota Wild
SEASON = "20242025"

def main():
    print("Starting data collection test...")

    # Collect data
    schedule_df, rosters, consistency_df = collect_data(TEAM_CODE, SEASON)

    # --- TEST 1: SCHEDULE DATAFRAME ---
    print("\n--- Validating Game Schedule DataFrame ---")
    assert isinstance(schedule_df, pd.DataFrame), "schedule_df is not a DataFrame"
    assert not schedule_df.empty, "schedule_df is empty"
    expected_columns = {'gamePk', 'date', 'homeTeam', 'awayTeam', 'homeScore', 'awayScore'}
    assert set(schedule_df.columns) == expected_columns, f"schedule_df columns do not match. Found: {schedule_df.columns}"

    print("✅ Game Schedule DataFrame is valid.")

    # --- TEST 2: ROSTERS DICTIONARY ---
    print("\n--- Validating Rosters Dictionary ---")
    assert isinstance(rosters, dict), "Rosters is not a dictionary"
    assert len(rosters) > 0, "Rosters dictionary is empty"
    sample_game_id = list(rosters.keys())[0]
    assert isinstance(rosters[sample_game_id], pd.DataFrame), f"Roster for game {sample_game_id} is not a DataFrame"

    print("✅ Rosters Dictionary is valid.")

    # --- TEST 3: CONSISTENCY DATAFRAME ---
    print("\n--- Validating Roster Consistency DataFrame ---")
    assert isinstance(consistency_df, pd.DataFrame), "consistency_df is not a DataFrame"
    assert not consistency_df.empty, "consistency_df is empty"
    expected_columns_consistency = {'gamePk', 'date', 'consistency', 'result'}
    assert set(consistency_df.columns) == expected_columns_consistency, f"consistency_df columns do not match. Found: {consistency_df.columns}"
    
    # Check the consistency values are between 0 and 1
    assert consistency_df['consistency'].between(0, 1).all(), "Consistency values are out of bounds"
    
    # Check for valid 'Win' or 'Loss' strings in 'result'
    assert consistency_df['result'].isin(['Win', 'Loss']).all(), "Result column contains invalid values"

    print("✅ Roster Consistency DataFrame is valid.")
    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    main()
