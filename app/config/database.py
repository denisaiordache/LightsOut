from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import models

def create_db(app, db):
    with app.app_context():
        #Delete database file if it exists currently
        if os.path.exists("config/database.sqlite"):
            os.remove("config/database.sqlite")
        db.create_all()

def populate_db(app, db):
    profile1, profile2 = models.UserProfile(profile_name="profile1"), models.UserProfile(profile_name="profile2")
    room1, room2 = models.Room(name="bedroom"), models.Room(name="kitchen")
    light1, light2 = models.Light(), models.Light()
    room1.lights = [light1, light2]
    profile1.rooms = [room1, room2]
    with app.app_context():
        db.session.add(profile1)
        db.session.add(profile2)
        db.session.commit()

if __name__ == "__main__":
    #initialize and configure the app and db variables 
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db = SQLAlchemy(app)
    create_db(app, db)
    populate_db(app, db)