import sqlite3 as sql


def electronics():

    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    print('SHOP FOR ELECTRONICS')
    print('BELOW ARE THE ITEMS WE HAVE FOR ELECTRONICS')
    c.execute('''SELECT subcategory_id, subcategory_name FROM product_subcategory WHERE category_id = ?''',(1,))
    elec = c.fetchall()
    for i in elec:
        print(i)
    while True:
        print(f"TYPE '1' TO SHOP {elec[0]}")
        print(f"TYPE '2' TO SHOP {elec[1]}")
        print(f"TYPE '3' TO SHOP {elec[2]}")
        print(f"TYPE '4' TO SHOP {elec[3]}")
        print(f"TYPE '5' TO SHOP {elec[4]}")
        print(f"TYPE '6' TO GO BACK")
        s_choice = int(input("ENTER YOUR CHOICE: "))
        if s_choice == 1:
            print('BELOW ARE THE ITEMS WE HAVE IN SMARTPHONE SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,(1,))
            sphones = c.fetchall()
            for i in sphones:
                print(i)
        elif s_choice == 2:
            print('BELOW ARE THE ITEMS WE HAVE IN LAPTOP SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,(2,))
            ltops = c.fetchall()
            for i in ltops:
                print(i)
        elif s_choice == 3:
            print('BELOW ARE THE ITEMS WE HAVE IN HEADPHONE/EARPHONE SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (3,))
            h_ephones = c.fetchall()
            for i in h_ephones:
                print(i)
        elif s_choice == 4:
            print('BELOW ARE THE ITEMS WE HAVE IN TELEVISION SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (4,))
            tvs = c.fetchall()
            for i in tvs:
                print(i)
        elif s_choice == 5:
            print('BELOW ARE THE ITEMS WE HAVE IN CAMERA SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (5,))
            cams = c.fetchall()
            for i in cams:
                print(i)
        elif s_choice == 6:
            break
    conn.commit()
    conn.close()

def fashion():
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    print('SHOP FOR FASHION')
    print('BELOW ARE THE ITEMS WE HAVE FOR FASHION')
    c.execute('''SELECT subcategory_id, subcategory_name FROM product_subcategory WHERE category_id = ?''', (2,))
    fash = c.fetchall()
    for i in fash:
        print(i)


    while True:
        print(f"TYPE '1' TO SHOP {fash[0]}")
        print(f"TYPE '2' TO SHOP {fash[1]}")
        print(f"TYPE '3' TO SHOP {fash[2]}")
        print(f"TYPE '4' TO GO BACK")
        s_choice = int(input("ENTER YOUR CHOICE: "))
        if s_choice == 1:
            print('BELOW ARE THE ITEMS WE HAVE IN MEN CLOTHING SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,(6,))
            mencloths = c.fetchall()
            for i in mencloths:
                print(i)
        elif s_choice == 2:
            print('BELOW ARE THE ITEMS WE HAVE IN WOMEN CLOTHING SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,(7,))
            womencloths = c.fetchall()
            for i in womencloths:
                print(i)
        elif s_choice == 3:
            print('BELOW ARE THE ITEMS WE HAVE IN KIDS SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (8,))
            kidscloths = c.fetchall()
            for i in kidscloths:
                print(i)

        elif s_choice == 4:
            break


    conn.commit()
    conn.close()

def kitchen_home():
    conn = sql.connect("./DATABASE/ecommerce.db")
    c = conn.cursor()
    print('SHOP FOR KITCHEN/HOME')
    print('BELOW ARE THE ITEMS WE HAVE FOR KITCHEN/HOME')
    c.execute('''SELECT subcategory_id, subcategory_name FROM product_subcategory WHERE category_id = ?''', (3,))
    k_h = c.fetchall()
    for i in k_h:
        print(i)



    while True:
        print(f"TYPE '1' TO SHOP {k_h[0]}")
        print(f"TYPE '2' TO SHOP {k_h[1]}")
        print(f"TYPE '3' TO SHOP {k_h[2]}")
        print(f"TYPE '4' TO SHOP {k_h[3]}")
        print(f"TYPE '5' TO SHOP {k_h[4]}")
        print(f"TYPE '6' TO GO BACK")
        s_choice = int(input("ENTER YOUR CHOICE: "))
        if s_choice == 1:
            print('BELOW ARE THE ITEMS WE HAVE IN KITCHEN APPLIANCE SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,(9,))
            kitchens = c.fetchall()
            for i in kitchens:
                print(i)
        elif s_choice == 2:
            print('BELOW ARE THE ITEMS WE HAVE IN COOKWARE SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (10,))
            cooks = c.fetchall()
            for i in cooks:
                print(i)
        elif s_choice == 3:
            print('BELOW ARE THE ITEMS WE HAVE IN FURNITURE SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (11,))
            furs = c.fetchall()
            for i in furs:
                print(i)
        elif s_choice == 4:
            print('BELOW ARE THE ITEMS WE HAVE IN HOME DECOR SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (12,))
            decor = c.fetchall()
            for i in decor:
                print(i)
        elif s_choice == 5:
            print('BELOW ARE THE ITEMS WE HAVE IN BEDDING & BATH SECTION')
            c.execute("""SELECT product_id, product_name, price, description FROM products WHERE subcategory_id = ? """,
                      (13,))
            B_B = c.fetchall()
            for i in B_B:
                print(i)

        elif s_choice == 6:
            break



    conn.commit()
    conn.close()





