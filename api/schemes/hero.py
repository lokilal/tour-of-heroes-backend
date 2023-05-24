from marshmallow import Schema, fields


class HeroSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    class Meta:
        fields = ('id', 'name')


hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)
