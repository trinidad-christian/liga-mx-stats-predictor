import pandas as pd

def flatten_player_data(raw_data: dict) -> pd.DataFrame:
    results = raw_data.get("results", [])
    players = []

    for item in results:
        if item.get("type") == "player":
            entity = item.get("entity", {})
            players.append({
                "name": entity.get("name", ""),
                "player_id": entity.get("id", ""),
                "team": entity.get("team", {}).get("name", "") if entity.get("team") else "",
                "position": entity.get("position", ""),
                "slug": entity.get("slug", "")
            })

    df = pd.DataFrame(players)
    return df
