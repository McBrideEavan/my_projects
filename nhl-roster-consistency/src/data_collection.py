import requests
import pandas as pd

def get_game_schedule(team_code: str, season: str) -> pd.DataFrame:
    """
    Fetches the game schedule for a specified team and season using the new NHL API format.

    Parameters:
    - team_code (str): The NHL team code (e.g., 'MIN' for Minnesota Wild).
    - season (str): The NHL season in YYYYYYYY format (e.g., '20252026').

    Returns:
    - pd.DataFrame: DataFrame containing game IDs, dates, home/away teams, and scores for completed games.
    """
    url = f"https://api-web.nhle.com/v1/club-schedule-season/{team_code}/{season}"
    response = requests.get(url)
    response.raise_for_status()
    schedule_data = response.json()

    games = []
    for game in schedule_data.get("games", []):
        if game.get("gameState") == "FINAL":  # Filter completed games
            games.append({
                "gamePk": game.get("id"),
                "date": game.get("gameDate"),
                "homeTeam": game.get("homeTeam", {}).get("commonName", {}).get("default"),
                "awayTeam": game.get("awayTeam", {}).get("commonName", {}).get("default"),
                "homeScore": game.get("homeTeam", {}).get("score"),
                "awayScore": game.get("awayTeam", {}).get("score"),
            })

    return pd.DataFrame(games)

def get_roster_for_game(game_id: int, team_code: str) -> pd.DataFrame:
    """
    Fetch the roster for a specified team in a given game using the NHL boxscore API.

    Parameters:
    - game_id (int): The NHL game ID.
    - team_code (str): The NHL team abbreviation (e.g., 'MIN' for Minnesota Wild).

    Returns:
    - pd.DataFrame: DataFrame with player info (playerId, name, jerseyNumber, position).
    """
    url = f"https://api-web.nhle.com/v1/gamecenter/{game_id}/boxscore"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Players are under playerByGameStats grouped by team: 'homeTeam' or 'awayTeam'
    # So first find which side is the requested team_code
    home_team = data.get("homeTeam", {}).get("abbrev", "")
    away_team = data.get("awayTeam", {}).get("abbrev", "")

    if team_code == home_team:
        team_key = "homeTeam"
    elif team_code == away_team:
        team_key = "awayTeam"
    else:
        raise ValueError(f"Team code '{team_code}' not found in game {game_id}")

    players = []
    # The players are grouped by position groups (forwards, defensemen, goalies) inside playerByGameStats
    player_groups = data.get("playerByGameStats", {}).get(team_key, {})

    for group in player_groups.values():  # e.g. forwards, defensemen, goalies
        for player in group:
            players.append({
                "playerId": player.get("playerId"),
                "name": player.get("name", {}).get("default"),
                "jerseyNumber": player.get("sweaterNumber"),
                "position": player.get("position")
            })

    return pd.DataFrame(players)

def calculate_roster_consistency(schedule_df: pd.DataFrame, rosters: dict) -> pd.DataFrame:
    """
    Calculates the roster consistency for each game compared to the previous game.

    Parameters:
    - schedule_df (pd.DataFrame): DataFrame with the game schedule.
    - rosters (dict): Dictionary of game rosters keyed by game ID.

    Returns:
    - pd.DataFrame: DataFrame with Game ID, Date, Consistency, Win/Loss status.
    """
    # Sort schedule by date to ensure correct game order
    schedule_df = schedule_df.sort_values(by='date')
    
    # Initialize list to store consistency data
    consistency_data = []

    previous_roster = set()
    
    for _, game in schedule_df.iterrows():
        game_id = game['gamePk']
        game_date = game['date']
        home_team = game['homeTeam']
        away_team = game['awayTeam']
        home_score = game['homeScore']
        away_score = game['awayScore']

        # Current roster for this game
        current_roster = set(rosters[game_id]['playerId']) if game_id in rosters else set()

        if previous_roster:
            # Calculate intersection and consistency rate
            common_players = current_roster.intersection(previous_roster)
            if len(previous_roster) > 0:
                consistency_rate = len(common_players) / len(previous_roster)
            else:
                consistency_rate = 0
        else:
            consistency_rate = 1  # First game has 100% consistency by default

        # Determine if this was a Win or Loss
        win_status = "Win" if (home_team == "MIN" and home_score > away_score) or \
                               (away_team == "MIN" and away_score > home_score) else "Loss"
        
        # Append to list
        consistency_data.append({
            "gamePk": game_id,
            "date": game_date,
            "consistency": consistency_rate,
            "result": win_status
        })

        # Update previous roster for next iteration
        previous_roster = current_roster

    # Convert to DataFrame
    return pd.DataFrame(consistency_data)

def collect_data(team_code: str, season: str) -> tuple:
    """
    Collects game schedule, rosters, and roster consistency for the specified team and season.

    Parameters:
    - team_code (str): NHL team abbreviation (e.g., 'MIN' for Minnesota Wild).
    - season (str): NHL season in YYYYYYYY format (e.g., '20252026').

    Returns:
    - tuple: (schedule_df, rosters, consistency_df)
    """
    print("Starting data collection...")

    # Step 1: Fetch the game schedule
    print(f"Fetching game schedule for Team Code: {team_code} for season {season}...")
    schedule_df = get_game_schedule(team_code, season)

    # Step 2: Fetch rosters for each game
    print("Collecting rosters for each game...")
    rosters = {}
    for game_id in schedule_df['gamePk']:
        try:
            rosters[game_id] = get_roster_for_game(game_id, team_code)
            print(f"Roster for game {game_id} collected successfully.")
        except Exception as e:
            print(f"Failed to collect roster for game {game_id}: {e}")

    # Step 3: Calculate roster consistency
    print("Calculating roster consistency between games...")
    consistency_df = calculate_roster_consistency(schedule_df, rosters)

    print("Data collection complete.")
    return schedule_df, rosters, consistency_df

