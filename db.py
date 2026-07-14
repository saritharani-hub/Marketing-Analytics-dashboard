import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="guvi",      # Replace if your password is different
        database="marketing"
    )