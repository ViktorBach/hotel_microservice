from flask import Flask, jsonify, request
from services.guests import fetch_guests, create_review, delete_review

app = Flask(__name__)

# Dummy data representing reviews stored in the `reviews` repo
reviews_data = [
    {"review_id": 1, "guest_id": 101, "review": "Great experience!", "rating": 5},
    {"review_id": 2, "guest_id": 102, "review": "Average service.", "rating": 3},
    {"review_id": 3, "guest_id": 101, "review": "Loved the stay!", "rating": 5},
]

@app.route('/reviews/<int:guest_id>', methods=['GET'])
def get_reviews(guest_id):
    # Filter reviews by guest_id
    guest_reviews = [review for review in reviews_data if review["guest_id"] == guest_id]
    return jsonify(guest_reviews)

@app.route('/guests')
def get_guests():
    return jsonify(fetch_guests())

@app.route('/guests/<int:id>')
def get_guest(id):
    return jsonify([guest for guest in fetch_guests() if guest['guestID'] == id])


app.run(host='0.0.0.0', port=5005)