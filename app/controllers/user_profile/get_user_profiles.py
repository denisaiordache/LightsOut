from models.user_profile import UserProfile

def get_user_profiles():
    try:
        ups = UserProfile.query.all()
        result = []
        for up in ups:
            result.append(up.json())
        return {"user_profiles": result}, 200
    except Exception as e:
        return {"error": str(e)}, 400

