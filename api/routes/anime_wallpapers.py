from functions.reddit import reddit


async def get_anime_wallpaper_route(q):
    imgs = []
    ft = await reddit("Animewallpaper", q)
    for i in ft:
        imgs.append(i["image"])
    return {"status": "Ok", "data": imgs}
