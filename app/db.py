import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    """The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request."""
    if 'db' not in g: #g is a special object that is unique for each request.
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row #tells the connection to return rows that behave like dicts. This allows accessing the columns by name.

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('database/schema.sql') as f: #example script
        db.executescript(f.read().decode('utf8'))
    close_db()

#Adds the "flask init-db" command which runs the init_db() function
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db) #tells Flask to call that function when cleaning up after returning the response.
    app.cli.add_command(init_db_command) #adds a new command that can be called with the flask command.