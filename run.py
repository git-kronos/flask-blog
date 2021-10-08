from core import create_app
from os import getenv

app = create_app()


if __name__ == "__main__":
    app.run(debug=bool(getenv("FLASK_DEBUG")))
