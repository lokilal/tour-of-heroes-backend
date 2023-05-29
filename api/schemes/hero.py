from marshmallow import Schema, fields


class HeroSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    ability = fields.String()
    class Meta:
        fields = ('id', 'name', 'ability')


class AbilitySchema(Schema):
    ability = fields.String()

    class Meta:
        fields = ('ability', )


hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)

ability_schema = AbilitySchema()
abilities_schema = AbilitySchema(many=True)
