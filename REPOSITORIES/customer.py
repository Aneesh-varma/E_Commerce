import sqlite3 as sql



def find_cus(cus_phno,cus_pass):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE cust_phno = ? AND cust_password = ?", (cus_phno,cus_pass))
    a = c.fetchone()
    return a

def insert_cus(cus_name,cus_phno,cus_password):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    c.execute("INSERT INTO customers (cust_name,cust_phno,cust_password) VALUES(?,?,?)",(cus_name,cus_phno,cus_password))
    c.execute("SELECT * FROM customers WHERE cust_name = ?",(cus_name,))
    a = c.fetchone()
    conn.commit()
    conn.close()
    return a

def ch_cust_name(cust_id,new_username):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    c.execute("UPDATE customers SET cust_name = ? WHERE cust_id = ?",(new_username,cust_id))
    conn.commit()

    return

def ch_cust_phno(old_phno,new_phno):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    c.execute("UPDATE customers SET cust_phno = ? WHERE cust_phno = ?",(new_phno,old_phno))
    conn.commit()

    return

def ch_verify_password(cust_id,cust_password):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    c.execute("SELECT cust_password FROM customers WHERE cust_id = ?",(cust_id,))
    a = c.fetchone()
    if a[0] != cust_password:
        return False
    elif a[0] == cust_password:
        return True

def ch_cust_password(cust_id, new_password):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    c.execute("UPDATE customers SET cust_password = ? WHERE cust_id = ?", (new_password, cust_id))
    conn.commit()

    return




