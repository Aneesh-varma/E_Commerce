import sqlite3 as sql


def cart_insertion(cust_id,cust_name,cat_name,sub_cat_name,products):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    while True:
        for i in products:
            print(i)
        cart_choice = int(input("ENTER THE PRODUCT ID TO ADD TO THE CART:"))
        cnt = 0
        for i in products:
            if i[0] == cart_choice:
                break
            cnt += 1
        prod_name = str(products[cnt][1])
        price = str(products[cnt][2])
        prod_price = float(price)
        prod_desc = str(products[cnt][3])
        qnt = input("PLEASE ENTER THE QUANTITY: ")
        c.execute('''INSERT INTO cust_cart(cust_id,cust_name,cat_name,subcategory_name,product_name,product_price,product_description,qnt) VALUES(?,?,?,?,?,?,?,?)''',(cust_id,cust_name,cat_name,sub_cat_name,prod_name,prod_price,prod_desc,qnt))
        print(f'{products[cnt][1]} ADDED TO THE CART SUCCESSFULLY')
        g_choice = input("WANT TO ADD MORE PRODUCTS ?(YES/NO): ")
        if g_choice == 'YES':
            pass
        elif g_choice == 'NO':
            break

    conn.commit()
    conn.close()


def cart_removal(cus_details):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    cart_details=cart_view(cus_details)
    for i in cart_details:
        print(i)
    while True:
        c_remove = input("PLEASE ENTER THE PRODUCT NAME TO REMOVE FROM THE CART: ")
        for i in cart_details:
            if i[4] == c_remove:
                c.execute('''DELETE FROM cust_cart WHERE product_name = ?''', (c_remove,))
                print("ITEM REMOVED SUCCESSFULLY")


        r_choice = input("DO YOU WANT TO REMOVE MORE PRODUCTS:(YES/NO): )")
        if r_choice == 'YES':
            pass
        elif r_choice == 'NO':
            break
        else:
            print("INVALID INPUT")
    conn.commit()
    conn.close()



def cart_view(cus_details):
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    cus_id = int(cus_details[0])
    c.execute("""SELECT * FROM cust_cart WHERE cust_id=?""", (cus_id,))
    c_details=c.fetchall()
    if len(c_details) == 0:
        print("NO ITEMS IN THE CART")

    conn.commit()
    conn.close()
    return c_details


