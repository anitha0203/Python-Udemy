from database import Database


class Store:
    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

    def save(self):
        Database.insert(self.to_dict())
