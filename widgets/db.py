import sqlite3

def get_db():
    conn = sqlite3.connect("mydb.db")
    return conn
