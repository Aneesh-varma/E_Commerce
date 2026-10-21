import sqlite3 as sql

conn = sql.connect("./DATABASE/ecommerce.db")
c = conn.cursor()

def find_emp(emp_id,emp_pass):
    c.execute("SELECT * FROM employees WHERE employee_id = ? AND employee_password = ?", (emp_id,emp_pass))
    a = c.fetchone()
    return a