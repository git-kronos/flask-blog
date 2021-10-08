from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from core.config import Config

# READ .ENV FILE
load_dotenv(".env.local")

# DATABASE INIT
db = SQLAlchemy()
# BCRYPT INIT
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


def create_app(confg_calss=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from core.main.routes import main
    from core.posts.routes import posts
    from core.users.routes import users

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
