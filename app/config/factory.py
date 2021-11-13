from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize and configure the app and db variables 
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

