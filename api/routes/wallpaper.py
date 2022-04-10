# Copyright (c) 2021 Itz-fork

from functions.reddit import request


subs = [
    "Animewallpaper",
    "wallpaper",
    "wallpapers",
    "wallpaperdump",
    "iWallpaper"
]


async def get_wallpaper(q):
    imgs = []
    for s in subs:
        ft = await request(s, q)
        for i in ft:
            imgs.append(i["image"])
    return {"status": "Ok", "data": imgs}
