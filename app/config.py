#only uppercase keys are added to the config. This makes it possible to use lowercase values in the config file for temporary values

DEBUG = True #remove when deploying
SECRET_KEY = 'development key' #replace with random string when deploying
DATABASE = 'database/database.sqlite' #name of the sqlite file (is used as route too so be careful about replacing or moving the file location)


