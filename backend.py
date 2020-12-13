import sqlite3 as sql

def CreateUser(FullName, Email, Password):
    conn = sql.connect('Clever_health.db')
    conn.execute('INSERT INTO Users (FullName, Email, Password) VALUES (?,?,?)',
                 (FullName, Email, Password))
    conn.commit()