import os
from flask.config import Config


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        os.environ.get('DB_USER', 'postgres'),
        os.environ.get('DB_PASSWORD', 'pass'),
        os.environ.get('DB_HOST', 'localhost'),
        os.environ.get('DB_PORT', '5432'),
        os.environ.get('DB_NAME', 'postgres'),
    )
