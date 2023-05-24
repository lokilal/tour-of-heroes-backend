from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from api.routes import init_route
from config import DevConfig
from api.error_handlers import init_handlers

app = Flask('hero')

app.config.from_object(DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

init_route(app, db)
init_handlers(app)
