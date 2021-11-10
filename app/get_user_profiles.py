from flask import jsonify 
import json
from db import get_db

def get_user_profiles():
    #get database object
    db = get_db()
    #make query
    if db.execute(
            'SELECT * FROM user_profile', 
        ).fetchone() is not None:
        return get_user_profiles()
    else:
        return jsonify({"error": "Something went wrong."})

