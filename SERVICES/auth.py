import string
from REPOSITORIES.customer import *
from REPOSITORIES.managers import *
from REPOSITORIES.employee import *
from REPOSITORIES.admin import *

# CUSTOMER AUTHENTICATION
"""
\\\\\\
\\\\\\
\\\\\\
"""
def customer_authentication():
    print(" ")
    print("WELCOME TO STAR MALL! EXPLORE OUR LATEST COLLECTIONS AND FIND EXACTLY WHAT YOU NEED TODAY")
    print("TYPE '1' TO SIGNUP\nTYPE '2' TO SIGNIN\nTYPE '3' TO GO BACK")
    while True:
        cust_choice = input("ENTER YOUR CHOICE: ")
        if cust_choice == "1":
            cust_details=customer_signup()
            return cust_details
        elif cust_choice == "2":
            cust_details = customer_signin()
            return cust_details
        elif cust_choice == "3":
            return None
        else:
            print("INVALID CHOICE")


def customer_signin():
    while True:
        cus_phno = input("PLEASE ENTER YOUR REGISTERED PH-NO: ")
        cus_pass = input("PLEASE ENTER YOUR REGISTERED PASSWORD: ")
        cus_details=find_cus(cus_phno,cus_pass)
        if cus_details is not None:
            print("LOGIN SUCCESS")
            return cus_details
        elif cus_details is None:
            print("INVALID REGISTERED PH-NO OR PASSWORD")
            o_change = input("DO YOU WISH TO GO FOR SIGNUP (YES/NO): ")
            if o_change.upper() == "YES":
                customer_signup()
                break
            elif o_change.upper() == "NO":
                pass
            else:
                print("INVALID CHOICE")



def customer_signup():
    cus_r_name = input("PLEASE ENTER YOUR NAME TO SIGN UP: ")
    cus_r_phno = input("PLEASE ENTER YOUR PH-NO TO REGISTER: ")
    print("PLEASE ENTER YOUR PASSWORD TO CONTINUE(your password must contain at least 8 characters,one uppercase letter,one lowercase letter,one number,one special character))")

    l_letters = "abcdefghijklmnopqrstuvwxyz"
    u_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = string.punctuation

    while True:
        cus_password = input("PLEASE ENTER YOUR PASSWORD: ")
        if len(cus_password) >=8:
            if not(set(cus_password).isdisjoint(l_letters) and set(cus_password).isdisjoint(u_letters) and set(cus_password).isdisjoint(digits) and set(cus_password).isdisjoint(specials)):
                print("VALID PASSWORD")
                while True:
                    pass_again = input("PLEASE ENTER YOUR PASSWORD AGAIN TO CONFIRM: ")
                    if pass_again == cus_password:
                        b=insert_cus(cus_r_name,cus_r_phno,cus_password)
                        print("YOUR DETAILS: ",b)
                        print("YOU HAVE SUCCESSFULLY SIGNED UP")
                        return b
                    elif pass_again != cus_password:
                        print("PLEASE RE-WRITE THE PASSWORD TO CONFIRM: ")

            else:
                print("INVALID PASSWORD")
                print("PLEASE ENTER YOUR PASSWORD RIGHT")
        else:
            print("INVALID ENTRY(please set the password according to the specified criteria)")







"""
\\\\\\
\\\\\\
\\\\\\
"""


# MANAGER AUTHENTICATION
"""
\\\\\\
\\\\\\
\\\\\\
"""

def manager_authentication():
    print(" ")
    print("TYPE '1' TO SIGNIN\nTYPE '2' TO GO BACK")
    while True:
        man_choice = input("ENTER YOUR CHOICE: ")
        if man_choice == "1":
            man_details = manager_signin()
            return man_details
        elif man_choice == "2":
            return None
        else:
            print("INVALID CHOICE")


def manager_signin():
    while True:
        man_ID = input("PLEASE ENTER YOUR MANAGER ID: ")
        man_pass = input("PLEASE ENTER YOUR PASSWORD: ")
        man_details=find_man(man_ID, man_pass)
        if man_details is not None:

            return man_details
        elif man_details is None:
            print("INVALID MANAGER ID OR PASSWORD")
            print("PLEASE ENTER YOUR VALID MANAGER ID AND PASSWORD")




"""
\\\\\\
\\\\\\
\\\\\\
"""


# EMPLOYEE AUTHENTICATION

"""
\\\\\\
\\\\\\
\\\\\\
"""

def employee_authentication():
    print(" ")
    print("TYPE '1' TO LOGIN\nTYPE '2' TO GO BACK")
    while True:
        emp_choice = input("ENTER YOUR CHOICE: ")
        if emp_choice == "1":
            emp_details = employee_signin()
            return emp_details
        elif emp_choice == "2":
            return None
        else:
            print("INVALID CHOICE")


def employee_signin():
    while True:
        emp_id = input("PLEASE ENTER YOUR EMPLOYEE ID: ")
        emp_pass = input("PLEASE ENTER YOUR PASSWORD: ")
        emp_details=find_emp(emp_id, emp_pass)
        if emp_details is not None:

            return emp_details
        else:
            print("INVALID EMPLOYEE ID OR PASSWORD")
            print("PLEASE ENTER YOUR VALID EMPLOYEE ID AND PASSWORD")

"""
\\\\\\
\\\\\\
\\\\\\
"""


#ADMIN AUTHENTICATION

"""
\\\\\\
\\\\\\
\\\\\\
"""

def admin_authentication():
    print(" ")
    print("TYPE '1' TO LOGIN\nTYPE '2' TO GO BACK")
    while True:
        admin_choice = input("ENTER YOUR CHOICE: ")
        if admin_choice == "1":
            admin_details=admin_signin()
            return admin_details
        elif admin_choice == "2":
            return None
        else:
            print("INVALID CHOICE")


def admin_signin():
    while True:
        admin_id = input("PLEASE ENTER YOUR ADMIN ID: ")
        admin_pass = input("PLEASE ENTER YOUR PASSWORD: ")
        admin_details=find_admin(admin_id, admin_pass)
        if admin_details is not None:

            return admin_details
        else:
            print("INVALID ADMIN ID OR PASSWORD")
            print("PLEASE ENTER YOUR VALID ADMIN ID AND PASSWORD")

"""
\\\\\\
\\\\\\
\\\\\\
"""




