# Copyright (c) 2021 Itz-fork

from functions.reddit import request


async def get_anime_wallpaper_route(q):
    imgs = []
    ft = await request("Animewallpaper", q)
    for i in ft:
        imgs.append(i["image"])
    return {"status": "Ok", "data": imgs}
