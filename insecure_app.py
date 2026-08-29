import os
import sqlite3

def run_command(user_input):
    # Command Injection Vulnerability
    os.system("ping -c 1 " + user_input)

def get_user(user_id):
    # SQL Injection Vulnerability
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id)
    return cursor.fetchall()


# Tainted Inputs
command_input = "127.0.0.1; cat /etc/passwd"
user_id_input = "1' OR '1'='1"

run_command(command_input)
get_user(user_id_input)
