# Copyright (c) 2021 Itz-fork

from functions.reddit import request


async def search_reddit_route(query, subr=None):
    return await request(subr, query)
