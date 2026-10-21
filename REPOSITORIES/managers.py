import sqlite3 as sql

conn = sql.connect("./DATABASE/ecommerce.db")
c = conn.cursor()

def find_man(man_id,man_pass):
    c.execute("SELECT * FROM managers WHERE manager_id = ? AND manager_password = ?", (man_id,man_pass))
    a = c.fetchone()
    return a