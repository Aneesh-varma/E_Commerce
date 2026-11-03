import random
from SERVICES.auth import *
from ROLES.customer import *
from ROLES.manager import *
from ROLES.employee import *
from ROLES.admin import *

print(" ")
a = random.choice(["Welcome to the STAR MALL portal.Please select your role to sign in",
                   "Welcome to STAR MALL Commerce System.Please securely authenticate your account to continue.",
                   "Welcome to STAR MALL. Access your space",
                   "Welcome to STAR MALL. Please choose your destination to sign in"])

print(a)


def main():

    while True:
        print("TYPE '1' TO SIGN UP AS A CUSTOMER")
        print("TYPE '2' TO SIGN UP AS A MANAGER")
        print("TYPE '3' TO SIGN UP AS AN EMPLOYEE")
        print("TYPE '4' TO SIGN UP AS AN ADMIN")
        print("TYPE '5' TO EXIT")
        print(" ")
        init_choice = input("ENTER YOUR CHOICE: ")
        if init_choice == "1":
            cus_details=customer_authentication()
            if cus_details is not None:
                customer_portal(cus_details)
                return
            else:
                pass
        elif init_choice == "2":
            man_details=manager_authentication()
            if man_details is not None:
                manager_portal(man_details)
                return
            else:
                pass
        elif init_choice == "3":
            emp_details=employee_authentication()
            if emp_details is not None:
                employee_portal(emp_details)
                return
            else:
                pass
        elif init_choice == "4":
            admin_details=admin_authentication()
            if admin_details is not None:
                admin_portal(admin_details)
                return
            else:
                pass
        elif init_choice == "5":
            return
        else:
            print("INVALID CHOICE. PLEASE ENTER THE VALID CHOICE")

main()






