# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html',name="sohel")
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='secret-key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "db.sqlite")}'

    db.init_app(app)

    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app