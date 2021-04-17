from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

from fapl.users.views import users  # blueprint-based architecture

moment = Moment()

def create_app(from_config):
    app = Flask(__name__)
    app.config.from_object(config[from_config])
    config[from_config].init_app(app)

    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #from fapl import views

    return app


#app.register_blueprint(users, url_prefix='/users')
#app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

#import fapl.models
#import fapl.views
