from functions.reddit import reddit


async def search_reddit_route(query, subr=None):
    return await reddit(subr, query)
