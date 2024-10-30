"""
Guest Service:
Styrer listen over gæster, inklusive detaljer såsom navn, kontak info og loyalitets point.
Tilbyder funktionalitet til at søge, filtrere, updatere og slette gæster.
"""
from flask import Flask, jsonify, request
from services.guests import fetch_guests
from services.guests import create_guest
from services.guests import update_guest
from services.guests import delete_guest

app = Flask(__name__)


########### CRUD method GET ############

@app.route('/guests', methods=['GET'])
def get_all_guests():
    guests = fetch_guests()
    return jsonify(guests)

@app.route('/guests/<int:id>', methods=['GET'])
def get_guests(id):
    guests = fetch_guests()
    
    return jsonify([guest for guest in guests if guest['guestID'] == id])

# Søg efter gæster på efternavn
@app.route('/guests/search', methods=['GET'])
def search_guest():
    query = request.args.get('lastname', '').lower()
    guests = fetch_guests()
    
    filtered_guests = [guest for guest in guests if query in guest['lastname'].lower()]
    return jsonify(filtered_guests)

@app.route('/guests/loyalty/<int:points>', methods=['GET'])
def get_guest_by_loyalty(points):
    guests = fetch_guests()
    
    filtered_guests = [guest for guest in guests if guest['loyaltyPoints'] == points]
    return jsonify(filtered_guests)


########### CRUD method POST ############

@app.route('/guests', methods=['POST'])
def add_guest():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid json data"}), 400
    
    result, status_code = create_guest(data)
    return jsonify(result), status_code


########### CRUD method POST ############

@app.route('/guests/<int:guest_id>', methods=['PUT'])
def modify_guest(guest_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid json data"}), 400
    
    result, status_code = update_guest(guest_id, data)
    return jsonify(result), status_code


########### CRUD method DELETE ############

@app.route('/guests/<int:guest_id>', methods=['DELETE'])
def remove_guest(guest_id):
    result, status_code = delete_guest(guest_id)
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0', port=4000)