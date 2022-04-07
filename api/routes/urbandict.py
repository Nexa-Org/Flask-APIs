from aiohttp import ClientSession


async def urban_dictionary_route(query):
    api_url = f"https://api.urbandictionary.com/v0/define?term={query}"
    ud_results = []
    async with ClientSession() as ud_client:
        req = await ud_client.get(api_url)
        jsned = await req.json()
        results = jsned["list"]
        if results:
            for definit in results:
                try:
                    definition_data = {}
                    definition_data["definition"] = definit["definition"]
                    definition_data["example"] = definit["example"]
                    definition_data["sounds"] = definit["sound_urls"]
                    definition_data["author"] = definit["author"]
                    definition_data["link"] = definit["permalink"]
                    definition_data["added_on"] = definit["written_on"]
                    definition_data["likes"] = definit["thumbs_up"]
                    definition_data["dislikes"] = definit["thumbs_down"]
                    # Appending the data to the main list
                    ud_results.append(definition_data)
                except:
                    pass
        # Parsing
    main_ud_data = {}
    main_ud_data["status"] = "Ok"
    main_ud_data["data"] = ud_results
    return main_ud_data
