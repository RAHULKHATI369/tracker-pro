from flask_pymongo import PyMongo
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/trackerdb")
mongo = PyMongo(app)

