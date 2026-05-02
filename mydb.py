
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mike1234',
    )

# Prepare a cursor object
cursor = database.cursor()

# Create a database
cursor.execute("CREATE DATABASE dcrm")
print("Database Created!")
