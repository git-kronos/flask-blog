from core import app
from core.forms import RegistrationForm, LoginForm
from core.models import User, Post
from flask import render_template, url_for, flash, redirect


data = [
    {"author": "Cory Schafer", "title": "Blog Post 1", "content": "First post content", "created": "April 20, 2018"},
    {"author": "John Doe", "title": "Blog Post 2", "content": "Second post content", "created": "April 21, 2018"},
    {"author": "Jane Doe", "title": "Blog Post 3", "content": "Third post content", "created": "April 22, 2018"}
]


@app.route('/')
def home():
    return render_template('home.html', posts=data)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"Login successful", 'success')
            return redirect(url_for('home'))
        flash(f"Login Failed", "danger")
    return render_template('login.html', title="Login", form=form)
