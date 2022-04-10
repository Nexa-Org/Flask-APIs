# Copyright (c) 2022 Itz-fork

from py_trans import Async_PyTranslator

async def translator_route(dest_lang, text):
    py_t = Async_PyTranslator()
    transed = await py_t.translate(text, dest_lang)
    tr = {}
    tr["status"] = "Ok"
    tr["data"] = transed
    return tr