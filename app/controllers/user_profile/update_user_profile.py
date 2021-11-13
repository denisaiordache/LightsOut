from flask import request
from models.user_profile import UserProfile
from config.factory import db

def update_user_profile():
    data = request.get_json()
    if data:
        try:
            up = UserProfile.query.get(data["profile_name"]).update(data)
            db.session.commit()
            return {"user_profile": up.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400