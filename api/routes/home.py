# Copyright (c) 2021 Itz-fork

from flask import render_template

async def home_route():
    return render_template("home.html")