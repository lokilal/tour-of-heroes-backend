from flask import jsonify, abort, request

from api.models.hero import Hero
from api.schemes.hero import heroes_schema, hero_schema
from api.utils import get_or_create


class HeroController:

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def heroes_list(self):
        if request.args.get('name'):
            name = request.args.get('name')
            heroes = Hero.query \
                .filter(Hero.name.contains(name))
            if heroes:
                return heroes_schema.dump(heroes)
        heroes = Hero.query.all()
        return heroes_schema.dump(heroes)

    def hero_detail(self, hero_id: int):
        hero = Hero.query.get(hero_id)
        if hero:
            return hero_schema.dump(hero)
        abort(404)

    def create_hero(self):
        if 'name' not in request.json:
            abort(400)

        hero = get_or_create(self.db.session, Hero, name=request.json.get('name'))
        return hero_schema.dump(hero), 201

    def delete_hero(self, hero_id: int):
        hero = Hero.query.get(hero_id)
        if hero is None:
            abort(404)
        self.db.session.delete(hero)
        self.db.session.commit()
        return jsonify({'result': True})

    def update_hero(self, hero_id: int):
        if not request.json:
            abort(400)
        hero = Hero.query.get(hero_id)
        if hero_id is None:
            abort(404)

        hero.name = request.json.get('name', hero.name)
        self.db.session.commit()
        return hero_schema.dump(hero)
