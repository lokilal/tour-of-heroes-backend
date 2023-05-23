from core import app
from core.models import Hero
from flask import jsonify, abort, request


@app.route('/api/heroes/', methods=['GET'])
def heroes_list():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])


@app.route('/api/hero/<int:hero_id>/', methods=['GET'])
def hero_detail(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        return jsonify(hero.to_dict())
    abort(404)


@app.route('/api/hero/search/', methods=['POST'])
def search_hero():
    name = request.json.get('name')
    hero = Hero.query\
        .filter(Hero.name.contains(name))\
        .first()
    if hero:
        return jsonify(hero.to_dict())
    abort(404)
