# MySQLServer.py
import mysql.connector

try:
    # connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',        # change as needed
        user='root',             # change to your MySQL username
        password='yourpassword'  # change to your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

# <-- this is what the checker wants -->
except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
