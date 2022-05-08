"""A simple flask web app"""
from datetime import datetime
import os
from flask import Flask, render_template, Blueprint, session, request, redirect, url_for
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
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Create all app
    with app.app_context():
        db.create_all()
    # add command function to cli commands
    app.cli.add_command(create_database)

    @app.route('/')
    def index():
        if session.get('logged_in'):
            return render_template('home.html')
        else:
            return render_template('index.html', message="Hello!")


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if session.get('logged_in'):
            return render_template('home.html')
            
        if request.method == 'GET':
            return render_template('login.html')
        else:
            email = request.form['email']
            password = request.form['password']
            data = User.query.filter_by(email=email, password=password).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('index'))
            return render_template('index.html', message="Incorrect Details")


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            try:
                db.session.add(User(
                    email=request.form['email'], 
                    password=request.form['password'], 
                    # authenticated=True,
                    # registered_on=datetime.now(),
                    # active=True,
                    # is_admin=True
                ))
                db.session.commit()
                return redirect(url_for('login'))
            except:
                return render_template('index.html', message="User Already Exists")
        else:
            return render_template('register.html')

    
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        session['logged_in'] = False
        return redirect(url_for('index'))

    return app