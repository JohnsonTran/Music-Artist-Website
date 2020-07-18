from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import environ

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # creates the database models
    from .models.user import User
    from .models.tour_model import Tour
    from .models.merch_model import Merch
    db.create_all(app=app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # registers blueprints
    from .views.home import home
    app.register_blueprint(home)
    
    from .views.music import music
    app.register_blueprint(music)

    from .views.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .views.profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from .views.tour import tour_blueprint
    app.register_blueprint(tour_blueprint)

    from .views.merch import merch_blueprint
    app.register_blueprint(merch_blueprint)

    from .views.product import product_blueprint
    app.register_blueprint(product_blueprint)
    
    from .views.admin import admin
    admin.init_app(app)

    return app
