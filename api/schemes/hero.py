from marshmallow import Schema, fields


class AbilitySchema(Schema):
    id = fields.Integer()
    title = fields.String()

    class Meta:
        fields = ('title', 'id')

class HeroSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    ability = fields.Nested(AbilitySchema, only=['title'], many=True)

    class Meta:
        fields = ('id', 'name', 'ability')
        include_fk = True
        strict = True


hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)

ability_schema = AbilitySchema()
abilities_schema = AbilitySchema(many=True)
