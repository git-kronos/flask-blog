from core import db
from core.models import Post
from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required

from .forms import PostForm

posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        flash("Post created", "success")
        obj_list = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
        )
        db.session.add(obj_list)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template(
        "create_post.html", title="New Post", legend="Create Post", form=form
    )


@posts.route("/post/<int:pk>")
def post_view(pk):
    obj = Post.query.get_or_404(pk)
    return render_template("post.html", title=obj.title, post=obj)


@posts.route("/post/<int:pk>/edit", methods=["GET", "POST"])
@login_required
def post_edit(pk):
    obj = Post.query.get_or_404(pk)
    if obj.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        obj.title = form.title.data
        obj.content = form.content.data
        db.session.commit()
        flash("Post has been updated!", "success")
        return redirect(url_for("posts.post_view", pk=obj.id))
    elif request.method == "GET":
        form.title.data = obj.title
        form.content.data = obj.content
    return render_template(
        "create_post.html", title="Update Post", legend="Update Post", form=form
    )


@posts.route("/post/<int:pk>/delete", methods=["POST"])
def post_delete(pk):
    obj = Post.query.get_or_404(pk)
    if obj.author != current_user:
        abort(403)
    db.session.delete(obj)
    db.session.commit()
    flash("Post has been deleted!", "success")
    return redirect(url_for("main.home"))
