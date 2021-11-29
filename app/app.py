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

@app.route('/user_profile/', defaults={'profile_name': "-1"})
@app.route("/user_profile/<string:profile_name>", methods=["GET", "PUT", "POST", "DELETE"])
def user_profile_route(profile_name):
    if request.method == "GET":
        if profile_name == "-1":
            return get_user_profiles.get_user_profiles()
        else:
            return get_user_profile.get_user_profile(profile_name)
    elif request.method == "PUT":
        return update_user_profile.update_user_profile(profile_name)
    elif request.method == "DELETE":
        return delete_user_profile.delete_user_profile(profile_name)
    elif request.method == "POST":
        return create_user_profile.create_user_profile(profile_name)

if __name__ == "__main__":
    app.run() 
# or use "$flask run" command (but you'll have to "set FLASK_ENV=development" in CMD for debug)
