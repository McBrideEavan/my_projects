import pandas as pd

def merge_dataframes(schedule_df: pd.DataFrame, consistency_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the game schedule DataFrame and the roster consistency DataFrame on gamePk and date.

    Parameters:
    - schedule_df (pd.DataFrame): DataFrame containing game schedule data.
    - consistency_df (pd.DataFrame): DataFrame containing roster consistency data.

    Returns:
    - pd.DataFrame: Merged DataFrame.
    """
    print("Merging schedule and consistency dataframes...")
    merged_df = pd.merge(schedule_df, consistency_df, on='gamePk', how='inner')
    return merged_df


def feature_engineering(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds additional features to the merged DataFrame for analysis.

    Parameters:
    - merged_df (pd.DataFrame): Merged DataFrame of schedule and consistency.

    Returns:
    - pd.DataFrame: DataFrame with new features.
    """
    print("Adding features to merged dataframe...")

    # Home/Away indicator
    merged_df['isHome'] = merged_df.apply(
        lambda row: 1 if row['homeTeam'] == 'MIN' else 0, axis=1
    )

    # Win/Loss indicator
    merged_df['isWin'] = merged_df.apply(
        lambda row: 1 if (
            (row['isHome'] == 1 and row['homeScore'] > row['awayScore']) or 
            (row['isHome'] == 0 and row['awayScore'] > row['homeScore'])
        ) else 0, axis=1
    )

    # Rolling average of consistency over the last 5 games
    merged_df['rolling_consistency'] = merged_df['consistency'].rolling(window=5).mean()

    return merged_df


def process_data(schedule_df: pd.DataFrame, consistency_df: pd.DataFrame) -> pd.DataFrame:
    """
    High-level function to process and prepare data for analysis.

    Parameters:
    - schedule_df (pd.DataFrame): DataFrame containing game schedule data.
    - consistency_df (pd.DataFrame): DataFrame containing roster consistency data.

    Returns:
    - pd.DataFrame: Final processed DataFrame.
    """
    print("Processing data for analysis...")
    merged_df = merge_dataframes(schedule_df, consistency_df)
    processed_df = feature_engineering(merged_df)
    print("Data processing complete.")
    return processed_df
