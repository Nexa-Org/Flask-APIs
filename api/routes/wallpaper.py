from functions.reddit import reddit


WALLPAPER_SUBREDDITS = ["wallpapers", "iWallpaper"]


async def get_wallpaper(q):
    imgs = []
    for s in WALLPAPER_SUBREDDITS:
        ft = await reddit(s, q)
        for i in ft:
            imgs.append(i["image"])
    return {"status": "Ok", "data": imgs}
