#!/usr/bin/python3
import sqlite3
import populate

def connectDB():
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
