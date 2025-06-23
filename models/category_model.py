import mysql.connector
from config.db_config import db_config

def get_all_category():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
