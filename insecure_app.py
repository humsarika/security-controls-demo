import sqlite3

def get_user_data(user_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Insecure SQL Query (Tainted User Input)
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    return cursor.fetchall()

user_input = "' OR '1'='1"
get_user_data(
user_input)
