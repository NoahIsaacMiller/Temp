from app import db as database

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    gender = database.Column(database.Integer, nullable=False)
    age = database.Column(database.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
    
    def __init__(self, username, gender, age):
        self.username = username
        self.gender = gender
        self.age = age

    def save(self):
        database.session.add(self)
        database.session.commit()
    
    def update(self, username, gender, age):
        self.username = username
        self.gender = gender
        self.age = age
        database.session.commit()

    def delete(self):
        database.session.delete(self)
        database.session.commit()
        return self
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "gender": self.gender,
            "age": self.age
        }


    def from_dict(self, data):
        for field in ["username", "gender", "age"]:
            if field in data:
                setattr(self, field, data[field])

    @staticmethod
    def findUsersByName(name):
        return User.query.filter_by(username=name)
    @staticmethod
    def findUserById(cls, id):
        return User.query.filter_by(id=id)
    

    @staticmethod
    def findUsersByGender(cls, gender):
        return User.query.filter_by(gender=gender)