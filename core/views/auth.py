from core import app, db, bcrypt, mail
from core.forms import (
    RegistrationForm,
    LoginForm,
    RequestResetForm,
    ResetPasswordForm,
)
from core.models import User, Post
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
            user.password, form.password.data
        ):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return (
                redirect(next_page) if next_page else redirect(url_for("home"))
            )
        flash(f"Login Failed", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/user/<string:username>")
@login_required
def posts_user(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    obj_list = (
        Post.query.filter_by(author=user)
        .order_by(Post.date_posted.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("posts_user.html", posts=obj_list, user=user)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request",
        sender="noreply@demo.com",
        recipients=[user.email],
    )
    msg.body = f"To reset your password, visit the following link:"
    msg.body += f"{url_for('reset_token', token=token, _external=True)}"
    msg.body += "If you did not make this request then "
    msg.body += "simply ignore this email and no changes will be made"
    mail.send(msg)


@app.route("/reset_password/", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instruction", "info")
        return redirect(url_for("login"))
    return render_template(
        "reset_request.html", title="Reset Password", form=form
    )


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticates:
        return redirect(url_for("home"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("Token is invalid or expired", "warning")
        return redirect(url_for("reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
        flash(
            f"Your Password for {form.username.data} has been updated!",
            "success",
        )
        return redirect(url_for("login"))
    return render_template(
        "reset_token.html", title="Reset Password", form=form
    )
