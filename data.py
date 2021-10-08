import json
from pathlib import Path

from core import db, bcrypt
from core.models import Post, User

BASE_DIR = Path(__file__).resolve().parent


class Data:
    posts_file = BASE_DIR / "fixture" / "posts.json"
    users_file = BASE_DIR / "fixture" / "users.json"

    def __init__(self) -> None:
        db.create_all()

    @classmethod
    def create_db(cls):
        db.create_all()

    @classmethod
    def drop_db(cls):
        db.drop_all()

    @staticmethod
    def commit_user(username, email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

    def get_user(self):
        with open(self.users_file, "r") as file:
            data = json.load(file)
            for i in range(len(data)):
                self.commit_user(
                    data[i]["username"], data[i]["email"], data[i]["password"]
                )
        return

    @staticmethod
    def commit_post(title, content, user):
        post = Post(title=title, content=content, author=user)
        db.session.add(post)
        db.session.commit()

    def get_post(self):
        with open(self.posts_file, "r") as file:
            data = json.load(file)
            for i in range(len(data)):
                self.commit_post(
                    data[i]["title"],
                    data[i]["content"],
                    User.query.get(data[i]["user_id"]),
                )
        return


if __name__ == "__main__":
    print(BASE_DIR)
    print(Data.posts_file)
    print(Data.users_file)
    Data.drop_db()
    print("Table Droped...")
    Data.create_db()
    print("Table Created...")
    d = Data()
    d.get_user()
    print("Users Generated...")
    d.get_post()
    print("Posts Generated...")
