# Copyright (c) 2021 Itz-fork

from re import search
from httpx import AsyncClient


async def request(query, subr=None):
    async with AsyncClient() as red_s:
        if subr:
            req = await red_s.get(f"https://www.reddit.com/r/{subr}/search.json?q={query}&restrict_sr=1&sr_nsfw=true")
        else:
            req = await red_s.get(f"https://www.reddit.com/search.json?q={query}")
        req_data = req.json()["data"]
        posts_data = []
        result = 1
        for child in req_data["children"]:
            try:
                pst_data = {}
                pst_data["result_no"] = result
                pst_data["subreddit"] = child["data"]["subreddit_name_prefixed"]
                pst_data["title"] = child["data"]["title"]
                pst_data["author"] = child["data"]["author"]
                pst_data["post_link"] = child["data"]["permalink"]
                if search(r'\bredd.it\b', child["data"]["url"]):
                    pst_data["image"] = child["data"]["url"]
                else:
                    pst_data["image"] = ""
                pst_data["post_content"] = child["data"]["selftext"]
                posts_data.append(pst_data)
                result += 1
            except:
                pass
        main_posts_data = {}
        main_posts_data["status"] = "Ok"
        main_posts_data["data"] = posts_data
        return main_posts_data
