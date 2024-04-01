import mysql.connector

database = mysql.connector.connect(
    user='root',
    password='265512',
    host='localhost',
)

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE zeeldb")
print("ALL DONE!")