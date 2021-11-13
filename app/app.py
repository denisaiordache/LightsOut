from flask import request

from config.factory import app, db
from config.db import create_db, populate_db

from controllers.user_profile import create_user_profile, get_user_profiles, get_user_profile, update_user_profile, delete_user_profile

if app.config["RESET_DATABASE_ON_STARTUP"]:
    create_db(app, db)
populate_db(app, db)

#routing
@app.route("/")
def hello_world_route():
    return "<p>Hello, World!!!!</p>"

@app.route("/user_profile/create", methods=["POST"])
def create_user_profile_route():
    return create_user_profile.create_user_profile()

@app.route("/user_profiles", methods=["GET"])
def read_user_profiles_route():
    return get_user_profiles.get_user_profiles()

@app.route("/user_profile", methods=["GET"])
def read_user_profile_route():
    return get_user_profile.get_user_profile()

@app.route("/user_profile/update", methods=["POST"])
def update_user_profile_route():
    return update_user_profile.update_user_profile()

@app.route("/user_profile/delete", methods=["POST"])
def delete_user_profile_route():
    return delete_user_profile.delete_user_profile()

if __name__ == "__main__":
    app.run() 
# or use "$flask run" command (but you'll have to "set FLASK_ENV=development" in CMD for debug)
