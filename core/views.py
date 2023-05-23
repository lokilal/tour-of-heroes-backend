from flask import jsonify, abort, request

from core import app, db
from core.models import Hero
from core.utils import get_or_create


@app.route('/api/heroes/', methods=['GET'])
def heroes_list():
    heroes = Hero.query.all()
    return jsonify([hero.to_json() for hero in heroes])


@app.route('/api/hero/<int:hero_id>/', methods=['GET'])
def hero_detail(hero_id: int):
    hero = Hero.query.get(hero_id)
    if hero:
        return jsonify(hero.to_json())
    abort(404)


@app.route('/api/hero/search/', methods=['POST'])
def search_hero():
    name = request.json.get('name')
    hero = Hero.query\
        .filter(Hero.name.contains(name))\
        .first()
    if hero:
        return jsonify(hero.to_json())
    abort(404)


@app.route('/api/hero/create/', methods=['POST'])
def create_hero():
    if 'name' not in request.json:
        abort(400)

    hero = get_or_create(db.session, Hero, name=request.json.get('name'))
    return jsonify(hero.to_json()), 201


@app.route('/api/hero/<int:hero_id>/', methods=['DELETE'])
def delete_hero(hero_id: int):
    hero = Hero.query.get(hero_id)
    if hero is None:
        abort(404)
    db.session.delete(hero)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/api/hero/<int:hero_id>/', methods=['PUT'])
def update_hero(hero_id: int):
    if not request.json:
        abort(400)
    hero = Hero.query.get(hero_id)
    if hero_id is None:
        abort(404)

    hero.name = request.json.get('name', hero.name)
    db.session.commit()
    return jsonify(hero.to_json())
