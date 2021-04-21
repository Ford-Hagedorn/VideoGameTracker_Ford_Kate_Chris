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

def search_by_year(input):
    games = index()
    for game in games:
        if game.year == input:
            return game

def search_by_console(input):
    games = index()
    for game in games:
        if game.platform == input:
            return game

def search_by_genre(input):
    games = index()
    for game in games:
        if game.genre == input:
            return game

from flask.views import View

class ShowGames(View):

    def dispatch_request(self):

        pass


class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class GameView(ListView):

    def get_template_name(self):
        return

    def get_objects(self):
        pass
