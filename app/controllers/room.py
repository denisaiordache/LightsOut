from flask import request
import models
import config.factory as CF

def create_room():
    data = request.get_json()
    if data:
        try:
            #if models.Room.query.filter_by(id=room_id).first():
             #   raise Exception("That id already exists")

            room = models.Room(id=data["id"],
                                name=data["name"],
                                profile_name=data["profile_name"])

            if "profile_name" in data: #link the room with the related profile
                if not models.UserProfile.query.filter_by(profile_name=data["profile_name"]).first():
                    raise Exception("That profile name does not exist")
                related_profile = models.UserProfile.query.filter_by(profile_name=data["profile_name"]).first()
                related_profile.rooms.append(room)
                CF.db.session.add(related_profile)
            else:
                CF.db.session.add(room)

            CF.db.session.commit()
            #result = models.Room.query.filter_by(id=room_id).first()
            return {"message" : "successfully created room"}, 201
        except Exception as e:
            return {"error": str(e)}, 400

def delete_room(room_id):
    data = request.get_json()
    if data:
        try:
            room = models.Room.query.get(room_id)
            CF.db.session.delete(room)
            CF.db.session.commit()
            return {}, 204
        except Exception as e:
            return {"error": str(e)}, 400

def get_room(room_id):
    data = room_id
    if data:
        try:
            room = models.Room.query.get(data)
            return {"room": room.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400

def get_rooms():
    try:
        rooms = models.Room.query.all()
        result = []
        for room in rooms:
            result.append(room.json())
        return {"rooms": result}, 200
    except Exception as e:
        return {"error": str(e)}, 400

def update_room(id_to_update):
    data = request.get_json()
    if data:
        try:
            if "profile_name" in data and not models.UserProfile.query.get(data["profile_name"]):
                raise Exception("Can't assign room to an inexistent profile")
            room = models.Room.query.get(id_to_update)
            lights = room.lights
            room.update(data)
            for light in lights:
                light.room_id = room.id
            CF.db.session.commit()
            return {"room": room.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400