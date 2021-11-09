from flask import Flask

def create_app():
    """Factory for the Flask application."""
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    from db import init_app
    init_app(app)

    return app