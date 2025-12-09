import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",     # replace with your MySQL username
        password="your_password"  # replace with your MySQL password
    )

    cursor = connection.cursor()
    # CREATE DATABASE with exact name
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
