from core import app
from core.models import Post
from flask import render_template, request
from flask_login import login_required


@app.route("/")
@login_required
def home():
    page = request.args.get("page", 1, type=int)
    obj_list = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=5
    )
    return render_template("home.html", posts=obj_list)
