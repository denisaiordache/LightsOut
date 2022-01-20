from flask import request
import models
import config.factory as CF

def create_user_profile(profile_name):
    data = request.get_json()
    data["profile_name"] = profile_name
    if data:
        try:
            if models.UserProfile.query.filter_by(profile_name=data["profile_name"]).first():
                raise Exception("That profile name already exists")
            up = models.UserProfile(profile_name=data["profile_name"])
            CF.db.session.add(up)
            CF.db.session.commit()
            result = models.UserProfile.query.filter_by(profile_name=data["profile_name"]).first()
            return {"created user_profile with profile_name" : result.json()}, 201
        except Exception as e:
            return {"error": str(e)}, 400

def delete_user_profile(profile_name):
    data = request.get_json()
    data["profile_name"] = profile_name
    if data:
        try:
            up = models.UserProfile.query.get(data["profile_name"])
            CF.db.session.delete(up)
            CF.db.session.commit()
            return {}, 204
        except Exception as e:
            return {"error": str(e)}, 400

def get_user_profile(profile_name):
    data = profile_name
    if data:
        try:
            up = models.UserProfile.query.get(data)
            return {"user_profile": up.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400

def get_user_profiles():
    try:
        ups = models.UserProfile.query.all()
        result = []
        for up in ups:
            result.append(up.json())
        return {"user_profiles": result}, 200
    except Exception as e:
        return {"error": str(e)}, 400

def update_user_profile(profile_name_to_update):
    data = request.get_json()
    if data:
        try:
            up = models.UserProfile.query.get(profile_name_to_update).update(data)
            CF.db.session.commit()
            return {"user_profile": up.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400