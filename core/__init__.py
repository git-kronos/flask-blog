from dotenv import load_dotenv
from os import environ as env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# READ .ENV FILE
load_dotenv(".env.local")

# Flask INIT
app = Flask(__name__)

# CONFIGURATIONS
app.config['SECRET_KEY'] = env.get("FlASK_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = env.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(env.get("SQLALCHEMY_TRACK_MODIFICATIONS"))

# DATABASE INIT
db = SQLAlchemy(app)

# BCRYPT INIT
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from core import views
