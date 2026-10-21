import sqlite3 as sql

conn = sql.connect("ecommerce.db")
c = conn.cursor()


# CUSTOMERS TABLE
c.execute('''CREATE TABLE IF NOT EXISTS customers(
          cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
          cust_name TEXT,
          cust_phno TEXT,
          cust_password VARCHAR
          )''')

#c.execute("INSERT INTO customers VALUES (1,'Aneesh','134234323','ndjendjen23')")

#MANAGERS TABLE
c.execute('''CREATE TABLE IF NOT EXISTS managers(
          manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
          manager_name TEXT,
          manager_phno TEXT,
          manager_password VARCHAR
          )''')

#c.execute("INSERT INTO managers VALUES (1001,'SURESH','134234323','ndjendjen23')")


#EMPLOYEE TABLE
c.execute('''CREATE TABLE IF NOT EXISTS employees(
          employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
          employee_name TEXT,
          employee_phno TEXT,
          employee_password VARCHAR
          )''')

c.execute("INSERT INTO employees VALUES (10001,'SURESH','134234323','ndjendjen23')")

#ADMIN TABLE
c.execute('''CREATE TABLE IF NOT EXISTS admins(
          admin_id INTEGER PRIMARY KEY,
          admin_name TEXT,
          admin_phno TEXT,
          admin_password VARCHAR
          )''')

c.execute("INSERT INTO admins VALUES (101,'SURESH','134234323','ndjendjen23')")








conn.commit()
conn.close()
