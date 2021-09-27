from dotenv import load_dotenv
from os import environ as env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv(".env.local")
app = Flask(__name__)
app.config['SECRET_KEY'] = env.get("FlASK_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = env.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = int(env.get("SQLALCHEMY_TRACK_MODIFICATIONS")) == 1

db = SQLAlchemy(app)
from core import routes
