# src/player_stats.py

import pandas as pd

def flatten_player_data(raw_data: dict) -> pd.DataFrame:
    """
    Extracts player names, team, and ID from SofaScore JSON results.
    Returns a clean pandas DataFrame.
    """
    players = raw_data.get("players", [])
    cleaned_data = []

    for player in players:
        cleaned_data.append({
            "name": player.get("name"),
            "player_id": player.get("id"),
            "team": player.get("team", {}).get("name"),
            "position": player.get("position"),
            "slug": player.get("slug")
        })

    df = pd.DataFrame(cleaned_data)
    return df
