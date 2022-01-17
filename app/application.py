from flask import request

import config.factory as CF
import config.database as DB_OPS
import controllers.user_profile as CUP

app, db = CF.app, CF.db

if app.config["RESET_DATABASE_ON_STARTUP"]:
    DB_OPS.create_db(app, db)
DB_OPS.populate_db(app, db)

#routing
@app.route("/")
def hello_world_route():
    return "<p>Hello, World!!!!</p>"

@app.route('/user_profile/', defaults={'profile_name': "-1"})
@app.route("/user_profile/<string:profile_name>", methods=["GET", "PUT", "POST", "DELETE"])
def user_profile_route(profile_name):
    if request.method == "GET":
        if profile_name == "-1":
            return CUP.get_user_profiles()
        else:
            return CUP.get_user_profile(profile_name)
    elif request.method == "PUT":
        return CUP.update_user_profile(profile_name)
    elif request.method == "DELETE":
        return CUP.delete_user_profile(profile_name)
    elif request.method == "POST":
        return CUP.create_user_profile(profile_name)

if __name__ == "__main__":
    app.run() 
# or use "$flask run" command (but you'll have to "set FLASK_ENV=development" in CMD for debug)
