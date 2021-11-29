from config.factory import db

class UserProfile(db.Model):
    __tablename__ = 'user profiles'

    profile_name = db.Column(db.String, primary_key=True)

    def update(self, new_dict):
        """Method to update all fields, given a dict with values for said fields. 
        New fields must follow this naming convention: new_example_field"""
        
        for key, value in new_dict.items():
            if key[4:] in self.__dict__.keys():
                setattr(self, key[4:], value)
        return self

    def __repr__(self):
        return f"<profile_name: {self.profile_name}>"

    def json(self):
        return {"profile_name": self.profile_name}

