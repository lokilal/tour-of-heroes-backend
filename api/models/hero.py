from run import db

hero_abilities = db.Table('hero_abilities',
    db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id'))
)

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    ability = db.relationship('Ability', backref='hero',
                              secondary=hero_abilities)


class Ability(db.Model):
    __tablename__ = 'ability'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
