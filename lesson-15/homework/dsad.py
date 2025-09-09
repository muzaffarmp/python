Got it! Here's a Python script using sqlite3 to create the database, add the table, insert data, update the name, and query Bajoran entries:

import sqlite3

def main():
    # Connect (or create) to the database file
    conn = sqlite3.connect('star_trek_roster.db')
    cursor = conn.cursor()

    # Create the Roster table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    ''')

    # Insert initial data
    roster_data = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', roster_data)
    conn.commit()

    # Update the Name of Jadzia Dax to Ezri Dax
    cursor.execute('''
        UPDATE Roster
        SET Name = ?
        WHERE Name = ?
    ''', ('Ezri Dax', 'Jadzia Dax'))
    conn.commit()

    # Select Name and Age of everyone classified as Bajoran
    cursor.execute('''
        SELECT Name, Age FROM Roster WHERE Species = ?
    ''', ('Bajoran',))

    bajorans = cursor.fetchall()
    print("Bajorans in the roster:")
    for name, age in bajorans:
        print(f"Name: {name}, Age: {age}")

    # Clean up
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
