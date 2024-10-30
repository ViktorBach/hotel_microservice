import json
import sqlite3

############   Database connection function   ##########

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

############   Fetch the guest data   ##########

def fetch_guests():
    # load json data from local file 
    with open('guest_data.json', 'r') as f:
        full_data = json.load(f)


        guests = full_data if isinstance(full_data, list) else full_data.get('guests', [])

        # filtering and transforming the guest data
        filstered_guests = [
            {
                "guestID": guest["GuestID"],
                "fiestname": guest["Firstname"],
                "lastname": guest["Lastname"],
                "email": guest["Email"],
                "phone": guest["Phone"],
                "review": guest["Review"]
            }
            for guest in guests
        ]

        return filstered_guests
    return []

#fetch and print the filtered guest data
guests_data = fetch_guests()
print(guests_data)
