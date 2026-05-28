from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    # Like a python dictionary, allows API to communicate using json
    # json is like a python dictionary
    def to_json(self):
        return {
            # camelCase is convention for json while snakecase is covention for python
            "id" : self.id,
            "firstName": self.first_name,
            "lastName" : self.last_name,
            "email" : self.email
        }
