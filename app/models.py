import config.factory as CF

class UserProfile(CF.db.Model):
    __tablename__ = 'user_profile'

    profile_name = CF.db.Column(CF.db.String, primary_key=True)
    rooms = CF.db.relationship("Room", back_populates="user_profile")

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields."""
        
        for key, value in new_dict.items():
            if key in self.__dict__.keys():
                setattr(self, key, value)
        return self

    def __repr__(self):
        return f"<profile_name: {self.profile_name}>"

    def json(self):
        return {"profile_name": self.profile_name}


class Room(CF.db.Model):
    __tablename__ = 'room'

    id = CF.db.Column(CF.db.Integer, primary_key=True)
    name = CF.db.Column(CF.db.String(100), default="Room #")
    profile_name = CF.db.Column(CF.db.Integer, CF.db.ForeignKey('user_profile.profile_name'))
    user_profile = CF.db.relationship("UserProfile", back_populates="rooms")
    lights = CF.db.relationship("Light", back_populates="room")

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields."""
        
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
                "lights": self.lights}

class Light(CF.db.Model):
    __tablename__ = 'light'

    id = CF.db.Column(CF.db.Integer, primary_key=True)
    name = CF.db.Column(CF.db.String(100), default="Light #")
    intensity = CF.db.Column(CF.db.Float, default=0.0)
    room_id = CF.db.Column(CF.db.Integer, CF.db.ForeignKey('room.id'))
    room = CF.db.relationship("Room", back_populates="lights")

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields."""
        
        for key, value in new_dict.items():
            if key in self.__dict__.keys():
                setattr(self, key, value)
        return self

    def __repr__(self):
        return f"<id: {self.id}> \
                <name: {self.name}> \
                <intensity: {self.intensity}>"

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "intensity": self.intensity}

