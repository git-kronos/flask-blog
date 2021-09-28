from core import app
from flask import render_template
from flask_login import login_required


@app.route('/about')
@login_required
def about():
    return render_template('about.html', title="About")
