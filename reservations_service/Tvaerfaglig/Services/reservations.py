# reservations.py

import sqlite3

DATABASE = 'database.db'

def fetch_reservations():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Reservation")
    reservations = cursor.fetchall()
    conn.close()
    return [{
        "ReservationID": row[0],
        "GuestID": row[1],
        "RoomID": row[2],
        "CheckInDate": row[3],
        "CheckOutDate": row[4],
        "Status": row[5]
    } for row in reservations]

def create_reservation(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Reservation (GuestID, RoomID, CheckInDate, CheckOutDate, Status) VALUES (?, ?, ?, ?, ?)", 
        (data["GuestID"], data["RoomID"], data["CheckInDate"], data["CheckOutDate"], data["Status"])
    )
    conn.commit()
    conn.close()
    return {"message": "Reservation created successfully"}, 201

def update_reservation(reservation_id, data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Reservation SET GuestID = ?, RoomID = ?, CheckInDate = ?, CheckOutDate = ?, Status = ? WHERE ReservationID = ?", 
        (data["GuestID"], data["RoomID"], data["CheckInDate"], data["CheckOutDate"], data["Status"], reservation_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Reservation updated successfully"}, 200

def delete_reservation(reservation_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Reservation WHERE ReservationID = ?", (reservation_id,))
    conn.commit()
    conn.close()
    return {"message": "Reservation deleted successfully"}, 200
