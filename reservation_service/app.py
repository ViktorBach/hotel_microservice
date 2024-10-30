# app.py

from flask import Flask, jsonify, request
from Services.reservations import fetch_reservations, create_reservation, update_reservation, delete_reservation

app = Flask(__name__)

# CRUD routes for reservations
@app.route('/reservations', methods=['GET'])
def get_all_reservations():
    reservations = fetch_reservations()
    return jsonify(reservations)

@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservations = fetch_reservations()
    reservation = next((reservation for reservation in reservations if reservation['ReservationID'] == id), None)
    if reservation:
        return jsonify(reservation)
    else:
        return jsonify({"error": "Reservation not found"}), 404

@app.route('/reservations', methods=['POST'])
def add_reservation():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    # Ensure all required fields are present
    required_fields = ["GuestID", "RoomID", "CheckInDate", "CheckOutDate", "Status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    result, status_code = create_reservation(data)
    return jsonify(result), status_code

@app.route('/reservations/<int:reservation_id>', methods=['PUT'])
def modify_reservation(reservation_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    # Ensure all required fields are present
    required_fields = ["GuestID", "RoomID", "CheckInDate", "CheckOutDate", "Status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    result, status_code = update_reservation(reservation_id, data)
    return jsonify(result), status_code

@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def remove_reservation(reservation_id):
    result, status_code = delete_reservation(reservation_id)
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
