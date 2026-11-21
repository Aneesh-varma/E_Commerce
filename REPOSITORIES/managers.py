import sqlite3 as sql

conn = sql.connect("./DATABASE/ecommerce.db")
c = conn.cursor()

def find_man(man_id,man_pass):
    c.execute("SELECT * FROM managers WHERE manager_id = ? AND manager_password = ?", (man_id,man_pass))
    a = c.fetchone()
    return a

def ch_man_name(man_id,new_username):
    c.execute("UPDATE managers SET manager_name = ? WHERE manager_id = ?",(new_username,man_id))
    conn.commit()

    return

def ch_man_phno(old_phno,new_phno):
    c.execute("UPDATE managers SET manager_phno = ? WHERE manager_phno = ?",(new_phno,old_phno))
    conn.commit()

    return

def man_verify_password(man_id,man_password):
    c.execute("SELECT manager_password FROM managers WHERE manager_id = ?",(man_id,))
    a = c.fetchone()
    if a[0] != man_password:
        return False
    elif a[0] == man_password:
        return True

def ch_man_password(man_id, new_password):
    c.execute("UPDATE managers SET manager_password = ? WHERE manager_id = ?", (new_password, man_id))
    conn.commit()

    return