import re
from aiohttp import ClientSession


WALLPAPER_SUBREDDITS = ["wallpapers", "iWallpaper"]

async def get_wallpaper(query):
    async with ClientSession() as red_s:
        wallpapers = {}
        wall_list = []
        for wall_sbr in WALLPAPER_SUBREDDITS:
            if query:
                req = await red_s.get(f"https://www.reddit.com/r/{wall_sbr}/search.json?q={query}&restrict_sr=1&sr_nsfw=true")
            else:
                req = await red_s.get("https://www.reddit.com/r/{wall_sbr}.json")
            json_req = await req.json()
            req_data = json_req["data"]
            # Storing image urls in a list
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