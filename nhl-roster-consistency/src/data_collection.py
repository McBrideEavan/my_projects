import requests

def collect_data():
    # Replace with actual code to fetch game schedule and rosters
    schedule_url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId=30&season=20252026"
    response = requests.get(schedule_url)
    data = response.json()
    
    schedule = []  # Extract schedule info
    rosters = []   # Extract roster info
    
    # You can extend this function to parse the schedule and rosters and return them as lists
    return schedule, rosters
