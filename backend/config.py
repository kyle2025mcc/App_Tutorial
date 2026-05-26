from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# All of this sets up the ability to preform python class and translate it so SQL

# Intilizes flask application
app = Flask(__name__)
# Send cross orgin requests and wrap app in CORS
CORS(app)

app.config["SWLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
