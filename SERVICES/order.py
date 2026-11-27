import sqlite3 as sql
from SERVICES.cart import *

def order_management(cus_details):
    print("#                        YOUR CART                          #")
    c_details=cart_view(cus_details)
    print(c_details)
    while True:

        print("1. TYPE '1' TO GO FOR ADDRESS/PAYMENT DETAILS\n2. TYPE '2' TO GO BACK")
        choice = input("ENTER YOUR CHOICE: ")
        if choice == '1':
            payment_management(c_details,cus_details)
        elif choice == '2':
            break
        else:
            print("INVALID CHOICE")



def payment_management(c_details,cus_details):
    conn = sql.connect("DATABASE/ecommerce.db")
    c = conn.cursor()
    while True:
        bill = 0
        for i in c_details:
            bill = i[5]*i[7]
        c.execute('''SELECT cust_addresses FROM cust_addresses WHERE cust_id = ?''',(cus_details[0],))
        c_address = c.fetchone()
        if c_address:
            pass
        else:

            print("YOUR TOTAL BILL: ", bill)
            print("ENTER YOU ADDRESS DETAILS: ")
            c_state = input("ENTER YOUR STATE: ")
            c_city = input("ENTER YOUR CITY: ")
            c_area_name = input("ENTER YOUR AREA NAME: ")
            c_street_name = input("ENTER YOUR STREET NAME: ")
            c_building_name = input("ENTER YOUR BUILDING NAME: ")
            c_flat_no = input("ENTER YOUR FLAT NO: ")
            c_postal_code = input("ENTER YOUR POSTAL CODE: ")
            address = c_state + "," + c_city + "," + c_area_name + "," + c_street_name + "," + c_building_name + "," + c_flat_no + "," + c_postal_code
            print(" ")
            print("YOUR ADDRESS: ", address)
            c.execute('''INSERT INTO cust_addresses(cust_id,cust_name,cust_addresses) VALUES(?,?,?)''',(cus_details[0],cus_details[1],address))


        c.execute('''SELECT cust_addresses FROM cust_addresses WHERE cust_id = ?''',(cus_details[0],))
        f_address = str(c.fetchone())


        print("1.TYPE '1' TO MAKE PAYMENT AND ORDER ITEMS.\n2.TYPE '2' TO GO BACK")
        c_choice = int(input("ENTER YOUR CHOICE: "))
        if c_choice == 1:
            P_choice = input("TYPE 'PAY' TO MAKE PAYMENT: ")
            if P_choice == 'PAY':
                for i in c_details:
                    p_name = i[4]
                    p_price = i[5]
                    p_desc = i[6]
                    p_qnt = i[7]

                    c.execute(
                        '''INSERT INTO orders(cust_id,cust_name,cust_phno,cust_address,product_name,product_price,product_description,product_qnt,status) VALUES(?,?,?,?,?,?,?,?,?)''',
                        (cus_details[0], cus_details[1], cus_details[2], f_address,p_name,p_price,p_desc,p_qnt,"ORDER PLACED"))
                    c.execute('''DELETE FROM cust_cart WHERE cust_id = ?''',(cus_details[0],))
                    print("PAYMENT SUCCESSFUL")
                    print("ORDER DELIVERING TO: ",f_address)

                break
            else:
                print("PAYMENT UNSUCCESSFUL")
        elif c_choice == 2:
            break
        else:
            print("INVALID CHOICE")


    conn.commit()
    conn.close()


def order_view(cus_details):
    print("#                   YOUR ORDERS                          #")
    conn = sql.connect("DATABASE/ecommerce.db")
    c = conn.cursor()

    c.execute('''SELECT * FROM orders WHERE cust_id = ?''',(cus_details[0],))
    orders = c.fetchall()
    if orders:
        for i in orders:
            print(" ")
            print("YOUR CUSTOMER-ID: ", i[0])
            print("YOUR NAME: ", i[1])
            print("YOUR PH-NO: ", i[2])
            print("YOUR ADDRESS: ", i[3])
            print("PRODUCT NAME: ", i[4])
            print("PRODUCT PRICE: ", i[5])
            print("PRODUCT DESCRIPTION: ", i[6])
            print("PRODUCT QNT: ", i[7])
            print("ORDER STATUS: ", i[8])
    else:
        print("NO ORDERS FOUND")



