from app.models.user_model import User

class UserService:
    def get_all(self):
        users = User.query.all()

        users_list = []
        for user in users:
            users_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email
            })

        return users_list
    
    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, data):
        pass
    
    def get_by_id(self, id):
        pass

user_service = UserService()