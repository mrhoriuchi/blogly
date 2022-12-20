"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'bloglysecret'

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    """Redirects to list of users"""

    return redirect()


@app.route('/users')
def users_index():
    """Shows a page with info on all users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)


@app.route('/users/new', methods=["GET"])
def users_new_form():
    """Shows a form to create a new user"""

    return render_template('users/new.html')
