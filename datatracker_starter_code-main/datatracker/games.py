import json
from types import SimpleNamespace

import requests
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
#https://api.dccresource.com/
import datatracker

bp = Blueprint('games', __name__)

@bp.route('/Get')
def index():
    response = requests.get('https://api.dccresource.com/api/games')
    games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
    for game in games:
        print(game.name)
    return ('Hello World!')

