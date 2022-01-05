async def unicode_detect_route(text):
    listed = list(text)
    uni_count = 0
    for char in listed:
        if char.encode("ascii", "ignore"):
            pass
        else:
            uni_count += 1
    unicode_data = {"status": "Ok", "data": {"count": uni_count}}
    return unicode_data