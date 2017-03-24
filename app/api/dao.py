from models import *


class UserDAO(object):
    def __init__(self):
        self.counter = User.query.count()
        self.users = User.query.all()

    def get(self, id):
        for user in self.users:
            if user['id'] == id:
                return user
            print("Not found")
    
    def create(self, data):
        user = data
        pass

    def update(self, id, data):
        user = self.get(id)
        pass

    def delete(self, id):
        user = self.get(id)
        pass
            
        
        