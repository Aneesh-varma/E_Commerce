import sqlite3 as sql

conn = sql.connect("./DATABASE/ecommerce.db")
c = conn.cursor()

def find_cus(cus_phno,cus_pass):
    c.execute("SELECT * FROM customers WHERE cust_phno = ? AND cust_password = ?", (cus_phno,cus_pass))
    a = c.fetchone()
    return a

def insert_cus(cus_name,cus_phno,cus_password):
    c.execute("INSERT INTO customers (cust_name,cust_phno,cust_password) VALUES(?,?,?)",(cus_name,cus_phno,cus_password))
    c.execute("SELECT * FROM customers WHERE cust_name = ?",(cus_name,))
    a = c.fetchone()
    conn.commit()
    conn.close()
    return a


