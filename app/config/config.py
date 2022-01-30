#only uppercase keys are added to the config. This makes it possible to use lowercase values in the config file for temporary values
from os.path import dirname, join

DEBUG = True #remove when deploying
SECRET_KEY = 'development key' #replace with random string when deploying
DATABASE = 'database/database.sqlite' #name of the sqlite file (is used as route too so be careful about replacing or moving the file)
SQLALCHEMY_DATABASE_URI="sqlite:///" + join(dirname(__file__), "database.sqlite") #location of database file for linking with sqlalchemy
RESET_DATABASE_ON_STARTUP = False #flag for determining whether or not to delete and recreate the database each time app.py is run
