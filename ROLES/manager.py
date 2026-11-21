from REPOSITORIES.managers import *

def manager_portal(man_details):
    print("WELCOME MANAGER,", man_details[1])

    while True:
        print("TYPE '1' TO VIEW YOUR PROFILE")
        print("TYPE '2' TO MANAGE THE PRODUCTS")
        print("TYPE '3' TO MANAGE THE DELIVERY")
        print("TYPE '4' TO LOG OUT")

        m_choice = input("ENTER YOUR CHOICE: ")
        if m_choice == "1":
            man_profile(man_details)
        elif m_choice == "2":
            pass
        elif m_choice == "3":
            pass
        elif m_choice == "4":
            return



def man_profile(man_details):
    print("YOUR DETAILS")
    print("YOUR ID:", man_details[0])
    print("YOUR NAME:", man_details[1])
    print("YOUR PHONE NUMBER:", man_details[2])
    print("YOUR PASSWORD:", '*' * len(man_details[3]))

    while True:
        print("1.TO CHANGE YOUR USER NAME\n2.TO CHANGE YOUR PHONE NUMBER\n3.TO CHANGE YOUR PASSWORD\n4.TO GO BACK")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("YOUR CURRENT USERNAME:", man_details[1])
            new_username = input("ENTER YOUR NEW USERNAME: ")
            ch_man_name(man_details[0], new_username)
            print("USERNAME CHANGED SUCCESSFULLY")
        elif choice == 2:
            print("YOUR CURRENT PHONE NUMBER:", man_details[2])
            new_phonenumber = input("ENTER YOUR NEW PHONE NUMBER: ")
            ch_man_phno(man_details[2], new_phonenumber)
            print("PHONE NUMBER CHANGED SUCCESSFULLY")
        elif choice == 3:
            while True:
                current_pass = input("ENTER YOUR CURRENT PASSWORD: ")
                ver = man_verify_password(man_details[0], current_pass)
                if ver:
                    new_password = input("ENTER YOUR NEW PASSWORD: ")
                    ch_man_password(man_details[0], new_password)
                    print("PASSWORD CHANGED SUCCESSFULLY")
                    break
                else:
                    print("PASSWORD INCORRECT TRY AGAIN")
                    break
        elif choice == 4:
            return
        else:
            print("Invalid choice")