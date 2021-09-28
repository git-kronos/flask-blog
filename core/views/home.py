from core import app
from flask import render_template
from flask_login import login_required


data = [
    {"author": "Cory Schafer", "title": "Blog Post 1", "content": "First post content", "created": "April 20, 2018"},
    {"author": "John Doe", "title": "Blog Post 2", "content": "Second post content", "created": "April 21, 2018"},
    {"author": "Jane Doe", "title": "Blog Post 3", "content": "Third post content", "created": "April 22, 2018"}
]


@app.route('/')
@login_required
def home():
    return render_template('home.html', posts=data)
