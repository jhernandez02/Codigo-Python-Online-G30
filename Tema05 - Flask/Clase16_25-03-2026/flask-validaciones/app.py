from flask import Flask, request
from pydantic import BaseModel, ValidationError

app = Flask(__name__)

class LocationSchema(BaseModel):
    lat: float
    lon: float

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    age: int
    is_married: bool
    location: LocationSchema
    tags: list[str]

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        validated_user = UserSchema.model_validate(data)
        print(validated_user.name)
        print(validated_user.email)
        return validated_user.model_dump()
    except ValidationError as e:
        return {
            'error': e.errors()
        }, 400
    except Exception as e:
        return {
            'error': str(e)
        }, 400

if __name__ == '__main__':
    app.run(debug=True)