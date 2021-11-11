from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    """Factory for the Flask application."""
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    from config.db import init_app
    init_app(app)

    return app