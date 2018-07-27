# from flask_api import FlaskAPI

from instance.config import app_config
from app.api import app

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')
    app.secret_key = 'dvsquf8qte91te1'
    app.config['SESSION_TYPE'] = 'filesystem'
    return app