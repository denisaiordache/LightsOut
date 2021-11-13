from flask import request
from models.user_profile import UserProfile
from config.factory import db

def delete_user_profile():
    data = request.get_json()
    if data:
        try:
            up = UserProfile.query.get(data["profile_name"])
            db.session.delete(up)
            db.session.commit()
            return {}, 204
        except Exception as e:
            return {"error": str(e)}, 400