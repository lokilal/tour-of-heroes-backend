from flask import jsonify, abort, request

from api.models.hero import Hero
from api.schemes.hero import heroes_schema, hero_schema, abilities_schema
from api.utils import get_or_create


class HeroController:

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def heroes_list(self):
        if request.args:
            heroes = Hero.query
            for query_param, value in request.args.items():
                heroes = heroes.filter(getattr(Hero, query_param).contains(value))
            return {'data': heroes_schema.dump(heroes), 'totalItems':len(heroes.all())}
        heroes = Hero.query.all()
        return {'data': heroes_schema.dump(heroes), 'totalItems':len(heroes)}

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

    def abilities_list(self):
         abilities = Hero.query.distinct(Hero.ability)
         return abilities_schema.dump(abilities)
