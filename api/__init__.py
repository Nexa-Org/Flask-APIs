# Copyright (c) 2021 Itz-fork

from flask import Flask, request
from .routes import (
    home_route,
    translator_route,
    get_anime_wallpaper_route,
    get_wallpaper,
    search_reddit_route,
    urban_dictionary_route,
    unicode_detect_route
)


# Configs
nexa_apis = Flask(__name__)
nexa_apis.config['JSON_SORT_KEYS'] = False
nexa_apis.config["DEBUG"] = False

# Home route
@nexa_apis.route("/")
async def home():
    return await home_route()

# Translator Route
@nexa_apis.route("/tr")
async def translate():
    try:
        tr_text = request.args.get("text")
        dest_l = request.args.get("dest_lang")
        if tr_text and dest_l:
            return await translator_route(dest_l, tr_text)
        else:
            return {"status": "Rip!", "data": "Not enough arguments provided 😐!"}
    except:
        return {"status": "Rip!", "data": "Server got a trouble 😐!"}

# Anime Wallpaper Route
@nexa_apis.route("/anime_wall")
async def anime_wallpapers():
    try:
        w_query = request.args.get("query")
        anime_random_walls = await get_anime_wallpaper_route(w_query)
        return anime_random_walls
    except:
        return {"status": "Rip!", "data": "Server got a trouble 😐!"}

# Wallpaper Route
@nexa_apis.route("/wallpaper")
async def wallpapers():
    try:
        query = request.args.get("query")
        some_wallpapers = await get_wallpaper(query)
        return some_wallpapers
    except Exception as e:
        print(e)
        return {"status": "Rip!", "data": "Server got a trouble 😐!"}

# Reddit Search Route
@nexa_apis.route("/reddit")
async def reddit_search():
    try:
        s_query = request.args.get("query")
        sub_redd = request.args.get("subreddit")
        if not s_query:
            return {"status": "Rip!", "data": "Not enough arguments provided 😐!"}
        reddit_search_data = await search_reddit_route(s_query, sub_redd)
        return reddit_search_data
    except:
        return {"status": "Rip!", "data": "Server got a trouble 😐!"}

# Urban dictionary Search Route
@nexa_apis.route("/ud")
async def ud_search():
    try:
        ud_query = request.args.get("query")
        if not ud_query:
            return {"status": "Rip!", "data": "Not enough arguments provided 😐!"}
        urban_dict_search_data = await urban_dictionary_route(ud_query)
        return urban_dict_search_data
    except:
        return {"status": "Rip!", "data": "Server got a trouble 😐!"}

# Unicode detector
@nexa_apis.route("/unicode")
async def unicode_count():
    try:
        uni_text = request.args.get("text")
        if not uni_text:
            return {"status": "Rip!", "data": "Not enough arguments provided 😐!"}
        unicode_count = await unicode_detect_route(uni_text)
        return unicode_count
    except:
        return {"status": "Rip!", "data": "Server got a trouble 😐!"}

if __name__ == "__main__":
    nexa_apis.run(threaded=True, port=5000)