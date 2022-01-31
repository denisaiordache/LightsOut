import config.factory as CF

class UserProfile(CF.db.Model):
    __tablename__ = 'user_profile'

    profile_name = CF.db.Column(CF.db.String, primary_key=True)
    wake_up_hour = CF.db.Column(CF.db.String)
    sleep_hour = CF.db.Column(CF.db.String)
    timer =  CF.db.Column(CF.db.Float)
    same_as_outside_lights = CF.db.Column(CF.db.Boolean)

    rooms = CF.db.relationship("Room", back_populates="user_profile", cascade="all, delete-orphan")

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields.
        Don't try to use with a newly created instance of this model. (self.__dict__ will be something else)"""
        
        for key, value in new_dict.items():
            if key in self.__dict__.keys():
                setattr(self, key, value)
        return self

    def __repr__(self):
        return f"<profile_name: {self.profile_name}> \
                <rooms: {self.rooms}>"

    def json(self):
        return {"profile_name": self.profile_name,
                "wake_up_hour":self.wake_up_hour,
                "sleep_hour":self.sleep_hour,
                "timer":self.timer,
                "same_as_outside_lights":self.same_as_outside_lights,
                "rooms": [x.json() for x in self.rooms]}


class Room(CF.db.Model):
    __tablename__ = 'room'

    id = CF.db.Column(CF.db.Integer, primary_key=True)
    name = CF.db.Column(CF.db.String(100), default="Room #")
    profile_name = CF.db.Column(CF.db.String, CF.db.ForeignKey('user_profile.profile_name'))
    user_profile = CF.db.relationship("UserProfile", back_populates="rooms")
    lights = CF.db.relationship("Light", back_populates="room", cascade="all, delete-orphan")

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields.
        Don't try to use with a newly created instance of this model. (self.__dict__ will be something else)"""
        
        for key, value in new_dict.items():
            if key in self.__dict__.keys():
                setattr(self, key, value)
        return self

    def __repr__(self):
        return f"<id: {self.id}> \
                <name: {self.name}> \
                <profile_name: {self.profile_name}> \
                <lights: {self.lights}"

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "profile_name": self.profile_name,
                "lights": [x.json() for x in self.lights]}

class Light(CF.db.Model):
    __tablename__ = 'light'

    id = CF.db.Column(CF.db.Integer, primary_key=True)
    name = CF.db.Column(CF.db.String(100), default="Light #")
    intensity = CF.db.Column(CF.db.Float, default=0.0)
    #color = CF.db.Column(CF.db.String(20))
    room_id = CF.db.Column(CF.db.Integer, CF.db.ForeignKey('room.id'))
    room = CF.db.relationship("Room", back_populates="lights")

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields.
        Don't try to use with a newly created instance of this model. (self.__dict__ will be something else)"""
        
        for key, value in new_dict.items():
            if key in self.__dict__.keys():
                setattr(self, key, value)
        return self

    def __repr__(self):
        return f"<id: {self.id}> \
                <name: {self.name}> \
                <intensity: {self.intensity}> \
                <room_id: {self.room_id}>"

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "intensity": self.intensity,
                "room_id": self.room_id}

