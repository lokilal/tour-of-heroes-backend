from core import db


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}
