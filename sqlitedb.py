#!/usr/bin/python3
import sqlite3
import populate

connectDB = sqlite3.connect('JoyOfCoding.db')

cursor = connectDB.cursor()

try:
    cursor.execute(""" SELECT Title FROM episodes; """)
    print("Database loaded and ready to roll.")
except:
    print("Database not found.")
    print("Creating the database and populating...")
    populate.populateDB()
    print("Database created and ready to roll.")
    cursor.execute(""" SELECT Title FROM episodes; """)

episodes = cursor.execute(""" SELECT * FROM episodes WHERE Season = '1'; """)
for episode in episodes:
    print(episode)
