from flask import request
from models.user_profile import UserProfile

def get_user_profile(profile_name):
    data = profile_name
    if data:
        try:
            up = UserProfile.query.get(data)
            return {"user_profile": up.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400