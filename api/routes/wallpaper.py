import re
from aiohttp import ClientSession


async def get_wallpaper(query):
    async with ClientSession() as red_s:
        if query:
            req = await red_s.get(f"https://www.reddit.com/r/wallpapers/search.json?q={query}&restrict_sr=1&sr_nsfw=true")
        else:
            req = await red_s.get("https://www.reddit.com/r/wallpapers.json")
        json_req = await req.json()
        req_data = json_req["data"]
        # Storing image urls in a list
        wallpapers = {}
        wall_list = []
        for child in req_data["children"]:
            try:
                pic = child["data"]["url"]
                if re.search(r'\bredd.it\b', pic):
                    wall_list.append(pic)
            except Exception as e:
                pass
        wallpapers["status"] = "Ok"
        wallpapers["data"] = wall_list
        return wallpapers