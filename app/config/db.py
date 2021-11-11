import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    click.echo("Initialized the database.")


def init_app(app):
    """Initialize the Flask app for database usage."""
    db.init_app(app)
    app.cli.add_command(init_db_command)