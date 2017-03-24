from flask import Flask
from config import config
from flask import Blueprint
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_login import LoginManager
from flask_cors import CORS

from app.api import ns1

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

moment = Moment()
db = SQLAlchemy()
api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_v1, version='1.0', title='VRUUM API', description='A development API')

def create_app(config_name):
    app = Flask(__name__)
    # api.init_app(app)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # Add namespaces
    ns = api.add_namespace(ns1)
    
    # Register routes
    app.register_blueprint(api_v1)

    return app
