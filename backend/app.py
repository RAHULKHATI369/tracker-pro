from flask import Flask, request, jsonify
from flask_cors import CORS
from database import mongo
import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from database import mongo
import datetime
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Flask backend running successfully 🚀"})

@app.route('/api/track_number', methods=['POST'])
def track_number():
    data = request.json
    number = data.get('number')

    # Check if number already exists in MongoDB
    record = mongo.db.tracked.find_one({"number": number})

    # Possible providers and locations
    providers = ["Jio", "Airtel", "Vodafone", "BSNL", "Idea"]
    locations = ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Hyderabad", "Pune"]

    if record:
        # Existing number → return stored info
        response = {
            "number": number,
            "location": record.get('location', 'Unknown'),
            "provider": record.get('provider', 'Unknown'),
            "coordinates": record.get('coordinates', [0, 0]),
            "last_updated": record.get('last_updated', 'N/A')
        }
    else:
        # New number → generate random provider, location, coordinates
        location = random.choice(locations)
        provider = random.choice(providers)
        coordinates = [
            round(random.uniform(20.0, 30.0), 4),  # latitude
            round(random.uniform(70.0, 80.0), 4)   # longitude
        ]
        last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = {
            "number": number,
            "location": location,
            "provider": provider,
            "coordinates": coordinates,
            "last_updated": last_updated
        }

        # Save to MongoDB
        mongo.db.tracked.insert_one(response)

    return jsonify(response)

if __name__ == '__main__':
    # Bind to all addresses for frontend access
    app.run(debug=True, host='0.0.0.0')

