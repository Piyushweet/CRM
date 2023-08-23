import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='yourusernam',  # Use the new username here
    password='yourpassword',  # Use the new password here
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
