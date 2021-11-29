from config.factory import db

# TODO: figure out why 'id' is not a field in the "context" 
# #https://docs.sqlalchemy.org/en/14/core/defaults.html#context-sensitive-default-functions
# def light_name_default(context):
#     id = str(context.get_current_parameters())#['id']
#     return id

class Light(db.Model):
    __tablename__ = 'lights'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default="Light #")
    intensity = db.Column(db.Float, default=0.0)

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields. 
        New fields must follow this naming convention: new_example_field"""
        
        for key, value in new_dict.items():
            if key[4:] in self.__dict__.keys():
                setattr(self, key[4:], value)
        return self

    def __repr__(self):
        return f"<id: {self.id}> \
                <name: {self.name}> \
                <intensity: {self.intensity}>"

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "intensity": self.intensity}