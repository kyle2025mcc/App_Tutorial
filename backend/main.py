from flask import request, jsonify
from config import app, db
from models import Contact

# Decarator: Goes above a function
#Sets what the root is and sets what request types are allowed
# Getter of contacts
@app.route("/contacts", methods = ["GET"])
def get_contacts():
    # Gives list of all current contacts as a python object
    contacts = Contact.query.all()
    # Takes all objects from contacts and converts it to json data
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


# Setting contacts
@app.route("/create_contact", methods = ["POST"])
def create_contact():
    # Put a request to the frontend
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    # If all of these are NULL return an error message
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name, and email"}),
            400, # This is the error code
        )

    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    try: 
        # Adding it to database (like git controls)
        db.session.add(new_contact)
        db.session.commit()
    # Catch any exception
    except Exception as e:
        return jsonify({"message", str(e)}), 400

    return jsonify({"message": "User created!"}), 201


# Updating contact
@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    # If no user with contact exhists return an error
    if not contact:
        return jsonify({"message":"User not found"}), 404
    
    data = request.json
    # If new name is inputed takes first value of get otherwise second value
    contact.last_name = data.get("firstName", contact.first_name)
    contact.first_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated"}), 200


# Delete contact
@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    # If no user with contact exhists return an error
    if not contact:
        return jsonify({"message":"User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "User deleted!"}), 200
    


# Is called when program is called
if __name__ == "__main__":
    with app.app_context():
        # Create all the models defined in database
        db.create_all()

    app.run(debug=True)

