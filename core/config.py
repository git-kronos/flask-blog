from os import getenv


class Config:
    SECRET_KEY = getenv("FlASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(
        getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    )
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = getenv("MAIL_USER")
    MAIL_PASSWORD = getenv("MAIL_PASS")
