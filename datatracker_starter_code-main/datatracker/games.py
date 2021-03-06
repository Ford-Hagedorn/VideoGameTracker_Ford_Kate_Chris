import json
from types import SimpleNamespace

import requests
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint, app
#https://api.dccresource.com/
import datatracker

bp = Blueprint('games', __name__)

@bp.route('/Get')
def index():
    response = requests.get('https://api.dccresource.com/api/games')
    games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
    return games

@bp.route('/Search')
def search_by_name(input):
    games = index()
    for game in games:
        if game.name == input:
            return game

@bp.route('/Console')
def view_consoles():
    games = index()
    platform = []
    for game in games:
        platform += game.platform.distinct
    return platform

@bp.route('/chart')
def chart():
    games = index()
    after2013s = []
    platforms = []
    for game in games:
        if game.year >= 2013:
            after2013s.add(game)

    for after2013 in after2013s:
        if not platforms.contains(after2013.platform):
            platforms.add(after2013.platform)
    sales = []
    for after2013 in after2013s:
        if not sales.contains(after2013.globalSales):
            sales.add(after2013.globalSales)

        # if game.platform is not in platforms
        # what is the easiest way to see if item is in a python list?
        # add it to platforms
        # platforms += game.platform.distinct

    # create dictionary using all unique console from that list
    # best way to create a dictionary with keys from a list?

    dct = dict(zip(platforms, sales))
    # if game.console is in that dictionary, add its total sales to that value

    return render_template('chart.html', dct=dct)
