from REPOSITORIES.customer import *
from SERVICES.products import *

def customer_portal(cus_details):
    print("HELLO,",cus_details[1])
    while True:
        print("1.TO VIEW YOUR PROFILE\n2.TO GO FOR SHOPPING\n3.TO VIEW YOUR ORDER HISTORY\n4.TO LOG OUT")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            cust_profile(cus_details)
        elif choice == 2:
            cust_shopping()
        elif choice == 3:
            cust_o_history()
        elif choice == 4:
            return
        else:
            print("Invalid choice")


def cust_profile(cus_details):
    print("YOUR DETAILS")
    print("YOUR ID:", cus_details[0])
    print("YOUR NAME:", cus_details[1])
    print("YOUR PHONE NUMBER:", cus_details[2])
    print("YOUR PASSWORD:", '*'*len(cus_details[3]))

    while True:
        print("1.TO CHANGE YOUR USER NAME\n2.TO CHANGE YOUR PHONE NUMBER\n3.TO CHANGE YOUR PASSWORD\n4.TO GO BACK")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("YOUR CURRENT USERNAME:", cus_details[1])
            new_username = input("ENTER YOUR NEW USERNAME: ")
            ch_cust_name(cus_details[0], new_username)
            print("USERNAME CHANGED SUCCESSFULLY")
        elif choice == 2:
            print("YOUR CURRENT PHONE NUMBER:", cus_details[2])
            new_phonenumber = input("ENTER YOUR NEW PHONE NUMBER: ")
            ch_cust_phno(cus_details[2], new_phonenumber)
            print("PHONE NUMBER CHANGED SUCCESSFULLY")
        elif choice == 3:
            while True:
                current_pass = input("ENTER YOUR CURRENT PASSWORD: ")
                ver=ch_verify_password(cus_details[0], current_pass)
                if ver:
                    new_password = input("ENTER YOUR NEW PASSWORD: ")
                    ch_cust_password(cus_details[0], new_password)
                    print("PASSWORD CHANGED SUCCESSFULLY")
                    break
                else:
                    print("PASSWORD INCORRECT TRY AGAIN")
                    break
        elif choice == 4:
            return
        else:
            print("Invalid choice")



def cust_shopping():
    while True:
        print("1.TO VIEW PRODUCTS\n2.TO VIEW YOUR CART\n3.TO VIEW YOUR ORDERS\n4.TO GO BACK")
        cust_choice = int(input("ENTER YOUR CHOICE: "))
        if cust_choice == 1:
            while True:
                print("1.TO SHOP ELECTRONICS\n2.TO SHOP FASHION\n3.TO SHOP KITCHEN/HOME APPLIANCES\n4.TO GO BACK")
                cat_choice = int(input("ENTER YOUR CHOICE: "))
                if cat_choice == 1:
                    electronics()
                elif cat_choice == 2:
                    fashion()
                elif cat_choice == 3:
                    kitchen_home()
                elif cat_choice == 4:
                    break
                else:
                    print("INVALID CHOICE")


        elif cust_choice == 2:
            pass
        elif cust_choice == 3:
            pass
        elif cust_choice == 4:
            return
        else:
            print("INVALID CHOICE")



def cust_o_history():
    pass