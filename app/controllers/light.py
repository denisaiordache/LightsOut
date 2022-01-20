from flask import request
import models
import config.factory as CF

def create_light(light_id):
    data = request.get_json()
    data["id"] = light_id
    if data:
        try:
            if models.Light.query.filter_by(id=light_id).first():
                raise Exception("That id already exists")

            light = models.Light(id=data["id"],
                                intensity=data["intensity"], 
                                name=data["name"],
                                room_id=data["room_id"])

            if "room_id" in data: #link the light with the related room
                if not models.Room.query.filter_by(id=data["room_id"]).first():
                    raise Exception("That room id does not exist")
                related_room = models.Room.query.filter_by(id=data["room_id"]).first()
                related_room.lights.append(light)
                CF.db.session.add(related_room)
            else:
                CF.db.session.add(light)
            CF.db.session.commit()
            result = models.Light.query.filter_by(id=light_id).first()
            return {"created light" : result.json()}, 201
        except Exception as e:
            return {"error": str(e)}, 400

def delete_light(light_id):
    data = request.get_json()
    if data:
        try:
            light = models.Light.query.get(light_id)
            CF.db.session.delete(light)
            CF.db.session.commit()
            return {}, 204
        except Exception as e:
            return {"error": str(e)}, 400

def get_light(light_id):
    data = light_id
    if data:
        try:
            light = models.Light.query.get(data)
            return {"light": light.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400

def get_lights():
    try:
        lights = models.Light.query.all()
        result = []
        for light in lights:
            result.append(light.json())
        return {"lights": result}, 200
    except Exception as e:
        return {"error": str(e)}, 400

def update_light(id_to_update):
    data = request.get_json()
    if data:
        try:
            light = models.Light.query.get(id_to_update).update(data)
            CF.db.session.commit()
            return {"light": light.json()}, 200
        except Exception as e:
            return {"error": str(e)}, 400