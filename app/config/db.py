from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from models.user_profile import UserProfile
from models.light import Light

def create_db(app, db):
    with app.app_context():
        #Delete database file if it exists currently
        if os.path.exists("config/database.sqlite"):
            os.remove("config/database.sqlite")
        db.create_all()

def populate_db(app, db):
    with app.app_context():
        db.session.add(UserProfile(profile_name="test1"))
        db.session.add(UserProfile(profile_name="test2"))
        db.session.add(UserProfile(profile_name="test3"))
        db.session.add(Light())
        db.session.add(Light())
        db.session.add(Light())
        db.session.commit()

if __name__ == "__main__":
    #initialize and configure the app and db variables 
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db = SQLAlchemy(app)
    create_db(app, db)
    populate_db(app, db)