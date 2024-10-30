import csv
import sqlite3

# Connect to SQLite (creates the database file if it doesn't exist)
conn = sqlite3.connect('database2.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Guest')

# Create the Guest table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Guest (
    GuestID INTEGER PRIMARY KEY AUTOINCREMENT,
    Firstname TEXT NOT NULL,
    Lastname TEXT NOT NULL,
    Country TEXT,
    Email TEXT NOT NULL,
    Phone INTEGER,
    LoyaltyPoints INTEGER,
    Review TEXT
)
''')

# Read the CSV file and insert data into the table
with open('guest_info.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=',')  # Change to comma
    print("CSV Headers:", csv_reader.fieldnames)  # Confirm headers are as expected

    # Insert data from CSV into the Guest table
    for guest in csv_reader:
        cursor.execute('''
        INSERT INTO Guest (Firstname, Lastname, Country, Email, Phone, LoyaltyPoints)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            guest["First Name"].strip(),
            guest["Last Name"].strip(),
            guest["Country"].strip(),
            guest["Email"].strip(),
            int(guest["Phone"].strip()) if guest["Phone"].strip().isdigit() else None,
            int(guest["LoyaltyPoints"].strip()) if guest["LoyaltyPoints"].strip().isdigit() else 0
        ))

# Commit and close the connection
conn.commit()
conn.close()

print("Data successfully imported to SQLite database :)")
