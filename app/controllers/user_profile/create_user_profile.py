from flask import request
from models.user_profile import UserProfile
from config.factory import db

def create_user_profile():
    data = request.get_json()
    if data:
        try:
            up = UserProfile(profile_name=data["profile_name"])
            db.session.add(up)
            db.session.commit()
            result = UserProfile.query.filter_by(profile_name=data["profile_name"]).first()
            return {"created user_profile with profile_name" : result.json()}
        except Exception as e:
            return {"error": str(e)}, 400

