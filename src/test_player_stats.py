# src/test_player_stats.py

import asyncio
from fetch_data import get_player_stats_by_name
from player_stats import flatten_player_data

async def main():
    raw_json = await get_player_stats_by_name("Gignac")
    df = flatten_player_data(raw_json)
    print(df.head())

    # 🔽 ADD THIS LINE TO SAVE THE FILE:
    df.to_csv("data/gignac_cleaned.csv", index=False)

asyncio.run(main())
