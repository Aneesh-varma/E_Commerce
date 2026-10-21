import sqlite3 as sql

conn = sql.connect("./DATABASE/ecommerce.db")
c = conn.cursor()

def find_admin(admin_id,admin_pass):
    c.execute("SELECT * FROM admins WHERE admin_id = ? AND admin_password = ?", (admin_id,admin_pass))
    a = c.fetchone()
    return a