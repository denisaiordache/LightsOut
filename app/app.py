from flask import Flask
from factory import create_app

app = create_app()

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"

if __name__ == "__main__":
    app.run() 
# or use "$flask run" command (but you'll have to "set FLASK_ENV=development" in CMD for debug)
