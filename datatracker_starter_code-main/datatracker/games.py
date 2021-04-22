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
    for game in games:
        platform += game.platform.distinct
    return platform