from core import app
from os import environ as env

if __name__ == "__main__":
    app.run(debug=bool(env.get("FLASK_DEBUG")))
