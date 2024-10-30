# import_json.py

import csv
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Rersevation')

# Create the Reservation table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reservation (
    ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
    GuestID INTEGER NULL,
    RoomID INTEGER NULL,
    CheckInDate DATE, 
    CheckOutDate DATE,
    Status TEXT NOT NULL
)
''')

#FOREIGN KEY (GuestID) REFERENCES Guest (GuestID)

with open('reservations.csv', 'r', encoding='utf-8') as files:
    csv_reader = csv.DictReader(files)

    # Insert the data
    for reservations in csv_reader:
        print(reservations)
        cursor.execute('''
        INSERT INTO Reservation (GuestID, RoomID, CheckInDate, CheckOutDate, Status)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            reservations["GuestID"], 
            reservations["RoomID"], 
            reservations["CheckInDate"], 
            reservations["CheckOutDate"], 
            reservations["Status"]
            ))

conn.commit()
conn.close()
print("Data imported successfully.")
