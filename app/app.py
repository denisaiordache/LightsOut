from flask import request
from config.factory import create_app
from CRUD.user_profile.create_user_profile import create_user_profile
from CRUD.user_profile.get_user_profiles import get_user_profiles
from CRUD.user_profile.get_user_profile import get_user_profile
from CRUD.user_profile.update_user_profile import update_user_profile
from CRUD.user_profile.delete_user_profile import delete_user_profile

app = create_app()

@app.route("/")
def hello_world_route():
    return "<p>Hello, World!!!!</p>"

@app.route("/user_profile/create", methods=["POST"])
def create_user_profile_route():
    return #create_user_profile()

@app.route("/user_profiles", methods=["GET"])
def read_user_profiles_route():
    return #get_user_profiles()

@app.route("/user_profile/<int:id>", methods=["GET"])
def read_user_profile_route(id):
    return #get_user_profile(id)

@app.route("/user_profile/<int:id>/update", methods=["POST"])
def update_user_profile_route(id):
    return #update_user_profile(id)

@app.route("/user_profile/<int:id>/delete", methods=["POST"])
def delete_user_profile_route(id):
    return delete_user_profile(id)

if __name__ == "__main__":
    app.run() 
# or use "$flask run" command (but you'll have to "set FLASK_ENV=development" in CMD for debug)
