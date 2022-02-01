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
            up = models.UserProfile(profile_name=data["profile_name"],
                                    is_active=data["is_active"],
                                    wake_up_hour = data["wake_up_hour"],
                                    sleep_hour = data["sleep_hour"],
                                    timer = data["timer"],
                                    same_as_outside_lights = data["same_as_outside_lights"])

            CF.db.session.add(up)
            CF.db.session.commit()
            result = models.UserProfile.query.filter_by(profile_name=data["profile_name"]).first()

            #Before returning, make all other profiles inactive (as this newly added one is the currently active one)
            if up.is_active:
                ups = aux_get_user_profiles()
                for profile in ups:
                    if not profile.profile_name == up.profile_name:
                        profile.is_active = False
                        CF.db.session.add(profile)
                CF.db.session.commit()

            return {"created user_profile with profile_name" : result.json()}, 201
        except Exception as e:
            print(e)
            return {"error": str(e)}, 400

def delete_user_profile(profile_name):
    data = request.get_json()
    data["profile_name"] = profile_name
    if data:
        try:
            up = CF.db.session.query(models.UserProfile).filter(models.UserProfile.profile_name==profile_name).first()
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
            up = models.UserProfile.query.get(profile_name_to_update)
            rooms = up.rooms
            up.update(data)
            for room in rooms:
                room.profile_name = up.profile_name
            CF.db.session.commit()
            return {"user_profile": up.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400

def aux_get_user_profiles():
    try:
        ups = models.UserProfile.query.all()
        result = []
        for up in ups:
            result.append(up)
        return result
    except Exception as e:
        return str(e)