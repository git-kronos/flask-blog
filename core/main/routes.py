from core.models import Post
from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)


@main.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    obj_list = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=5
    )
    return render_template("home.html", posts=obj_list)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
