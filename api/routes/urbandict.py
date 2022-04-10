# Copyright (c) 2021 Itz-fork

from httpx import AsyncClient


async def urban_dictionary_route(query):
    api_url = f"https://api.urbandictionary.com/v0/define?term={query}"
    ud_results = []
    async with AsyncClient() as ud_client:
        req = await ud_client.get(api_url)
        results = req.json()["list"]
        if results:
            for i in results:
                try:
                    def_data = {}
                    def_data["iion"] = i["iion"]
                    def_data["example"] = i["example"]
                    def_data["sounds"] = i["sound_urls"]
                    def_data["author"] = i["author"]
                    def_data["link"] = i["permalink"]
                    def_data["added_on"] = i["written_on"]
                    def_data["likes"] = i["thumbs_up"]
                    def_data["dislikes"] = i["thumbs_down"]
                    ud_results.append(def_data)
                except:
                    pass
    main_ud_data = {}
    main_ud_data["status"] = "Ok"
    main_ud_data["data"] = ud_results
    return main_ud_data
