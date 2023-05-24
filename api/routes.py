import importlib

import connexion
from flask import Blueprint, Flask
from jinja2 import Environment, FileSystemLoader
from swagger_ui_bundle import swagger_ui_3_path


class HeroApiResolver(connexion.Resolver):

    def __init__(self, app, db):
        super().__init__()
        self.app = app
        self.db = db

    def resolve_function_from_operation_id(self, operation_id):
        module,  controller_name, operation = operation_id.rsplit('.', 2)
        controller_module = importlib.import_module(module)
        controller_cls = getattr(controller_module, controller_name)
        controller = controller_cls(self.app, self.db)
        return getattr(controller, operation)


def connexion_register(app: Flask, db, swagger_file):
    con = connexion.FlaskApp("hero_api", app.instance_path)
    api = con.add_api(swagger_file, resolver=HeroApiResolver(app, db))
    bp = Blueprint('heroes_swagger_ui', __name__)
    bp.add_url_rule('/api/heroes/ui/',
                    view_func=lambda: Environment(loader=FileSystemLoader(swagger_ui_3_path),
                                                  trim_blocks=True).get_template('index.j2').render(
                        openapi_spec_url="/api/heroes/openapi.json"
                    ), methods=['GET'])
    app.register_blueprint(bp)
    app.register_blueprint(api.blueprint)
    return api


def init_route(app: Flask, db):
    connexion_register(app, db,'api/swagger/swagger.yml')
