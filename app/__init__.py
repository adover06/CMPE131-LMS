#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#import os
#
#myapp_obj = Flask(__name__)
#
#basedir = os.path.abspath(os.path.dirname(__file__))
#
#myapp_obj.config.from_mapping(
#    SECRET_KEY = 'you-will-never-guess',
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
#)
#
#db = SQLAlchemy(myapp_obj)
#
#from app import routes
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

myapp_obj = Flask(__name__)
myapp_obj.config.from_object("app.config.Config")

# Initialize database
db = SQLAlchemy(myapp_obj)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(myapp_obj)
login_manager.login_view = 'auth.login'

# Register blueprints 
from .auth import bp as auth_bp
myapp_obj.register_blueprint(auth_bp)

from .main import bp as main_bp
myapp_obj.register_blueprint(main_bp)

from app import models

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))



