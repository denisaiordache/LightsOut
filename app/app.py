from factory import create_app
from get_user_profiles import get_user_profiles
app = create_app()

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"

@app.route("/user_profile", methods=["GET"])
def get_user():
    return get_user_profiles()

if __name__ == "__main__":
    app.run() 
# or use "$flask run" command (but you'll have to "set FLASK_ENV=development" in CMD for debug)
