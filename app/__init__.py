"""A simple flask web app"""
import os
from flask import Flask, render_template
from app.cli import create_database
from app.db import db
from app.db.models import User
from flask_bootstrap import Bootstrap5

def page_not_found(e):
    # return render_template("404.html")
    return "page not found"

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'
    bootstrap = Bootstrap5(app)

    app.register_error_handler(404, page_not_found)
    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    # add command function to cli commands
    app.cli.add_command(create_database)

    @app.route('/')
    def hello():
        return 'Hello, World'

    @app.route('/login')
    def login_view():
        return "Login view"

    return app