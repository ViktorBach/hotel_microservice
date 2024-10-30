import json
import sqlite3

############   Database connection function   ##########

def get_db_connection():
    conn = sqlite3.connect('database2.db')
    conn.row_factory = sqlite3.Row  # Possible fetching rows 
    return conn

############   Fetch the guest data   ##########

def fetch_guests():
    # Connect to the database and fetch guest data
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute a query to fetch all records from the Guest table
    cursor.execute("SELECT * FROM Guest")
    rows = cursor.fetchall()
    conn.close()

    # Convert data to a list of dictionaries with required fields
    filtered_guests = [
        { 
            "guestID": row["GuestID"],
            "firstname": row["Firstname"],
            "lastname": row["Lastname"],
            "country": row["Country"],
            "email": row["Email"],
            "phone": row["Phone"],
            "loyaltyPoints": _calculate_loyaltyPoints(row["LoyaltyPoints"]),
            "review": row["Review"]
        }
        for row in rows
    ]

    return filtered_guests

def _calculate_loyaltyPoints(points):
    # Adds 10% to loyalty points if valid, otherwise returns 0
    try:
        return points * 1.1 if points else 0
    except TypeError:
        return 0  # In case points are not numeric or None

# Fetch and print the filtered guest data
guests_data = fetch_guests()
#print(guests_data)


############   Create new guest data   ##########

def create_guest(data):
    # Extract data fields from the request
    firstname = data.get("Firstname")
    lastname = data.get("Lastname")
    country = data.get("Country")
    email = data.get("Email")
    phone = data.get("Phone")
    loyalty_points = data.get("LoyaltyPoints", 0)  # Default to 0 if not provided

    # Verify that mandatory fields are present
    if not firstname or not lastname or not email:
        return {"error": "Firstname, Lastname, and Email are required fields"}, 400

    # Insert data into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO Guest (Firstname, Lastname, Country, Email, Phone, LoyaltyPoints) 
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (firstname, lastname, country, email, phone, loyalty_points)
    )
    conn.commit()
    guest_id = cursor.lastrowid
    conn.close()

    # Return confirmation with the new guest's ID
    return {"message": "Guest created successfully", "guestID": guest_id}, 201


############   Update guest data   ##########

def update_guest(guest_id, data):
    firstname = data.get("Firstname")
    lastname = data.get("Lastname")
    country = data.get("Country")
    email = data.get("Email")
    phone = data.get("Phone")
    loyalty_points = data.get("LoyaltyPoints")

    if not firstname or not lastname or not email:
        return {"error": "Fiestname, Lastname, and Email are required fields"}, 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Guest 
        SET Firstname = ?, Lastname = ?, Country = ?, Email = ?, Phone = ?, LoyaltyPoints = ?
        WHERE GuestID = ?
        ''', 
        (firstname, lastname, country, email, phone, loyalty_points, guest_id)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return {"error": "Guest not found"}, 404
    
    # return confirmation of successful update
    return {"message": "Guest updated successfully"}, 200

def create_review(guest_id, data):
    email = data.get("Email")
    phone = data.get("Phone")
    review = data.get("Review")

    if not email or not phone:
        return {"error": "Email and Phone are required fields"}, 400
    conn = get_db_connection
    cursor = conn.connect()
    cursor.execute('''
        UPDATE Guest 
        SET Review = ?
        WHERE GuestID = ?
        ''', 
        (review, guest_id)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return {"error": "Guest not found"}, 404
    
    # return confirmation of successful update
    return {"message": "Review created successfully"}, 200

############   Delete guest    ##########

def delete_guest(guest_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM Guest where GuestID = ?',
        (guest_id,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return {"error": "Guest not found"}, 404
    
    # return confirmation of successful removel
    return {"message": "Guest deleted successfully"}, 200
