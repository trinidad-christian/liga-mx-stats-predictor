# src/fetch_data.py
import asyncio
import json
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.search import Search

async def get_player_stats_by_name(name: str):
    api = SofascoreAPI()
    search = Search(api, search_string=name)
    results = await search.search_all()
    await api.close()
    return results

if __name__ == "__main__":
    async def main():
        data = await get_player_stats_by_name("André-Pierre Gignac")
        print(json.dumps(data, indent=4))

    asyncio.run(main())
# To run this script, use the command: python src/fetch_data.py