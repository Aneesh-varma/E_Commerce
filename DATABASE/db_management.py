import sqlite3 as sql

conn = sql.connect("ecommerce.db")
c = conn.cursor()

""" 
# CUSTOMERS TABLE
c.execute('''CREATE TABLE IF NOT EXISTS customers(
          cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
          cust_name TEXT,
          cust_phno TEXT,
          cust_password VARCHAR
          )''')

#c.execute("INSERT INTO customers VALUES (1,'Aneesh','134234324','ndjendjen23')")

#MANAGERS TABLE
c.execute('''CREATE TABLE IF NOT EXISTS managers(
          manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
          manager_name TEXT,
          manager_phno TEXT,
          manager_password VARCHAR
          )''')

#c.execute("INSERT INTO managers VALUES (1001,'SURESHH','134234324','ndjendjen24')")


#EMPLOYEE TABLE
c.execute('''CREATE TABLE IF NOT EXISTS employees(
          employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
          employee_name TEXT,
          employee_phno TEXT,
          employee_password VARCHAR
          )''')

#c.execute("INSERT INTO employees VALUES (10001,'SURESH','134234323','ndjendjen23')")

#ADMIN TABLE
c.execute('''CREATE TABLE IF NOT EXISTS admins(
          admin_id INTEGER PRIMARY KEY,
          admin_name TEXT,
          admin_phno TEXT,
          admin_password VARCHAR
          )''')

#c.execute("INSERT INTO admins VALUES (101,'SURESH','134234323','ndjendjen23')")



#Product_Category_Table

c.execute('''CREATE TABLE IF NOT EXISTS product_category(
          category_id INTEGER PRIMARY KEY,
          category_name TEXT
          )''')

'''
c.execute("INSERT INTO product_category VALUES (1,'ELECTRONICS')")
c.execute("INSERT INTO product_category VALUES (2, 'FASHION')")
c.execute("INSERT INTO product_category VALUES (3, 'KITCHEN & HOME')")
'''


#Product_Sub-Category_Table

c.execute('''CREATE TABLE IF NOT EXISTS product_subcategory(
          subcategory_id INTEGER PRIMARY KEY,
          category_id INTEGER,
          subcategory_name TEXT
          )''')


'''
c.execute("INSERT INTO product_subcategory VALUES (1,1,'SMARTPHONES')")
c.execute("INSERT INTO product_subcategory VALUES (2,1,'LAPTOPS')")
c.execute("INSERT INTO product_subcategory VALUES (3,1,'HEADPHONES & EARPHONES')")
c.execute("INSERT INTO product_subcategory VALUES (4,1,'TELEVISIONS')")
c.execute("INSERT INTO product_subcategory VALUES (5,1,'CAMERAS')")
c.execute("INSERT INTO product_subcategory VALUES (6,2,'MENS CLOTHING')")
c.execute("INSERT INTO product_subcategory VALUES (7,2,'WOMEN CLOTHING')")
c.execute("INSERT INTO product_subcategory VALUES (8,2,'KIDS CLOTHING')")
c.execute("INSERT INTO product_subcategory VALUES (9,3,'KITCHEN APPLIANCES')")
c.execute("INSERT INTO product_subcategory VALUES (10,3,'COOKWARE')")
c.execute("INSERT INTO product_subcategory VALUES (11,3,'FURNITURE')")
c.execute("INSERT INTO product_subcategory VALUES (12,3,'HOME DECOR')")
c.execute("INSERT INTO product_subcategory VALUES (13,3,'BEDDING & BATH')")
'''



#Products_Table

c.execute('''CREATE TABLE IF NOT EXISTS products(
          product_id INTEGER PRIMARY KEY,
          subcategory_id INTEGER,
          product_name TEXT,
          qnt INTEGER,
          price REAL,
          description TEXT
          )''')

'''
#SMARTPHONES (subcategory_id = 1)

c.execute("INSERT INTO products VALUES (1,1,'iPhone 16',15,69900,'Apple smartphone with A18 chip and advanced camera system')")
c.execute("INSERT INTO products VALUES (2,1,'Samsung Galaxy S25',20,80999,'Samsung flagship smartphone with AMOLED display and AI features')")
c.execute("INSERT INTO products VALUES (3,1,'OnePlus 13',12,69999,'Premium Android smartphone with Snapdragon processor')")
c.execute("INSERT INTO products VALUES (4,1,'Google Pixel 9',10,79999,'Google smartphone with advanced AI photography features')")
c.execute("INSERT INTO products VALUES (5,1,'Redmi Note 14',25,17999,'Budget smartphone with AMOLED display and long battery life')")

#LAPTOPS (subcategory_id = 2)

c.execute("INSERT INTO products VALUES (6,2,'MacBook Air M4',10,99900,'Apple laptop powered by M4 chip with Retina display')")
c.execute("INSERT INTO products VALUES (7,2,'Dell Inspiron 15',15,54999,'Everyday laptop suitable for office work and productivity')")
c.execute("INSERT INTO products VALUES (8,2,'HP Pavilion 15',12,62999,'Versatile laptop for productivity and entertainment')")
c.execute("INSERT INTO products VALUES (9,2,'Lenovo IdeaPad Slim 5',18,57999,'Slim laptop designed for everyday computing and multitasking')")
c.execute("INSERT INTO products VALUES (10,2,'ASUS Vivobook 16',14,64999,'Large-screen laptop suitable for work and entertainment')")

#HEADPHONES & EARPHONES (subcategory_id = 3)

c.execute("INSERT INTO products VALUES (11,3,'Sony WH-1000XM5',20,29990,'Wireless over-ear headphones with active noise cancellation')")
c.execute("INSERT INTO products VALUES (12,3,'Apple AirPods Pro 2',15,24900,'Wireless earbuds with active noise cancellation and spatial audio')")
c.execute("INSERT INTO products VALUES (13,3,'Samsung Galaxy Buds 3',18,12999,'Wireless earbuds with immersive audio and comfortable fit')")
c.execute("INSERT INTO products VALUES (14,3,'JBL Tune 770NC',25,5999,'Wireless headphones with adaptive noise cancellation')")
c.execute("INSERT INTO products VALUES (15,3,'OnePlus Buds 3',22,5499,'Wireless earbuds with powerful bass and clear audio')")

#TELEVISIONS (subcategory_id = 4)

c.execute("INSERT INTO products VALUES (16,4,'Samsung 55-inch 4K Smart TV',10,54999,'4K smart television with vibrant colours and streaming apps')")
c.execute("INSERT INTO products VALUES (17,4,'LG 43-inch LED Smart TV',12,32999,'Full HD smart television with webOS operating system')")
c.execute("INSERT INTO products VALUES (18,4,'Sony Bravia 65-inch 4K TV',8,119999,'Large 4K television with advanced picture processing')")
c.execute("INSERT INTO products VALUES (19,4,'TCL 50-inch QLED TV',15,39999,'QLED television with vibrant colours and smart features')")
c.execute("INSERT INTO products VALUES (20,4,'Xiaomi 32-inch Smart TV',20,14999,'Compact smart television suitable for bedrooms and small spaces')")

#CAMERAS (subcategory_id = 5)

c.execute("INSERT INTO products VALUES (21,5,'Canon EOS R50',8,67995,'Mirrorless camera suitable for photography and content creation')")
c.execute("INSERT INTO products VALUES (22,5,'Sony Alpha A6400',10,72990,'Mirrorless camera with fast autofocus and 4K video recording')")
c.execute("INSERT INTO products VALUES (23,5,'Nikon Z50',7,69995,'Compact mirrorless camera for photography enthusiasts')")
c.execute("INSERT INTO products VALUES (24,5,'Fujifilm X-T5',6,169999,'High-resolution mirrorless camera with advanced image controls')")
c.execute("INSERT INTO products VALUES (25,5,'GoPro Hero 13',12,39990,'Action camera designed for adventure and outdoor recording')")

#MENS CLOTHING (subcategory_id = 6)

c.execute("INSERT INTO products VALUES (26,6,'Mens Cotton T-Shirt',50,499,'Comfortable everyday cotton T-shirt')")
c.execute("INSERT INTO products VALUES (27,6,'Mens Casual Shirt',30,999,'Casual full-sleeve shirt suitable for everyday wear')")
c.execute("INSERT INTO products VALUES (28,6,'Mens Denim Jeans',25,1499,'Regular-fit denim jeans for casual outfits')")
c.execute("INSERT INTO products VALUES (29,6,'Mens Cotton Kurta',35,899,'Traditional cotton kurta with a comfortable fit')")
c.execute("INSERT INTO products VALUES (30,6,'Mens Formal Trousers',20,1299,'Formal trousers suitable for office and professional occasions')")

#WOMEN CLOTHING (subcategory_id = 7)

c.execute("INSERT INTO products VALUES (31,7,'Womens Cotton Kurti',40,799,'Lightweight cotton kurti for everyday comfort')")
c.execute("INSERT INTO products VALUES (32,7,'Womens Saree',20,1999,'Traditional saree suitable for festive and family occasions')")
c.execute("INSERT INTO products VALUES (33,7,'Womens Palazzo Pants',30,699,'Comfortable wide-leg palazzo pants for casual outfits')")
c.execute("INSERT INTO products VALUES (34,7,'Womens Casual Dress',25,1299,'Stylish casual dress suitable for everyday outings')")
c.execute("INSERT INTO products VALUES (35,7,'Womens Leggings',45,399,'Stretchable leggings designed for everyday use')")

#KIDS CLOTHING (subcategory_id = 8)

c.execute("INSERT INTO products VALUES (36,8,'Kids Cotton T-Shirt',40,299,'Soft cotton T-shirt designed for children')")
c.execute("INSERT INTO products VALUES (37,8,'Kids Denim Jeans',25,699,'Comfortable denim jeans for everyday kids wear')")
c.execute("INSERT INTO products VALUES (38,8,'Kids Party Wear Dress',15,1199,'Decorative party wear dress for special occasions')")
c.execute("INSERT INTO products VALUES (39,8,'Kids Cotton Shorts',35,349,'Lightweight cotton shorts for daily activities')")
c.execute("INSERT INTO products VALUES (40,8,'Kids Traditional Wear',20,999,'Traditional ethnic outfit for children')")

#KITCHEN APPLIANCES (subcategory_id = 9)

c.execute("INSERT INTO products VALUES (41,9,'Philips Mixer Grinder',15,3499,'Powerful mixer grinder for blending and grinding ingredients')")
c.execute("INSERT INTO products VALUES (42,9,'Prestige Electric Kettle',20,1299,'Electric kettle for quickly boiling water')")
c.execute("INSERT INTO products VALUES (43,9,'LG Microwave Oven',10,8999,'Microwave oven for heating and cooking food')")
c.execute("INSERT INTO products VALUES (44,9,'Butterfly Wet Grinder',12,5999,'Wet grinder suitable for preparing batter and grinding ingredients')")
c.execute("INSERT INTO products VALUES (45,9,'Pigeon Induction Cooktop',18,2199,'Energy-efficient induction cooktop for everyday cooking')")

#COOKWARE (subcategory_id = 10)

c.execute("INSERT INTO products VALUES (46,10,'Non-Stick Frying Pan',30,799,'Non-stick frying pan for easy cooking and cleaning')")
c.execute("INSERT INTO products VALUES (47,10,'Stainless Steel Pressure Cooker',25,1799,'Durable stainless steel pressure cooker for everyday meals')")
c.execute("INSERT INTO products VALUES (48,10,'Cast Iron Dosa Tawa',20,999,'Heavy-duty cast iron tawa for preparing dosas and pancakes')")
c.execute("INSERT INTO products VALUES (49,10,'Stainless Steel Cooking Pot',35,1299,'Multipurpose stainless steel cooking pot')")
c.execute("INSERT INTO products VALUES (50,10,'Aluminium Kadai',28,699,'Lightweight aluminium kadai for frying and cooking')")

#FURNITURE (subcategory_id = 11)

c.execute("INSERT INTO products VALUES (51,11,'Wooden Study Table',10,4999,'Spacious wooden study table suitable for home and office')")
c.execute("INSERT INTO products VALUES (52,11,'Office Ergonomic Chair',15,5999,'Ergonomic office chair designed for comfortable seating')")
c.execute("INSERT INTO products VALUES (53,11,'Three-Seater Sofa',5,18999,'Comfortable three-seater sofa for living room spaces')")
c.execute("INSERT INTO products VALUES (54,11,'Wooden Bookshelf',12,3499,'Multi-level wooden bookshelf for organizing books')")
c.execute("INSERT INTO products VALUES (55,11,'Queen Size Bed',8,15999,'Queen-size wooden bed frame for bedroom use')")

#HOME DECOR (subcategory_id = 12)

c.execute("INSERT INTO products VALUES (56,12,'Decorative Wall Clock',25,799,'Stylish wall clock for home decoration')")
c.execute("INSERT INTO products VALUES (57,12,'LED Decorative Lights',40,499,'Decorative LED lights for indoor ambience')")
c.execute("INSERT INTO products VALUES (58,12,'Artificial Indoor Plant',30,599,'Low-maintenance artificial plant for interior decoration')")
c.execute("INSERT INTO products VALUES (59,12,'Decorative Wall Painting',15,1499,'Decorative wall painting for living room interiors')")
c.execute("INSERT INTO products VALUES (60,12,'Ceramic Flower Vase',20,699,'Decorative ceramic vase suitable for flowers and interiors')")

#BEDDING & BATH (subcategory_id = 13)

c.execute("INSERT INTO products VALUES (61,13,'Cotton Bedsheet Set',25,1299,'Soft cotton bedsheet set for comfortable sleeping')")
c.execute("INSERT INTO products VALUES (62,13,'Memory Foam Pillow',30,999,'Supportive memory foam pillow for comfortable sleep')")
c.execute("INSERT INTO products VALUES (63,13,'King Size Comforter',15,2499,'Soft king-size comforter for bedroom use')")
c.execute("INSERT INTO products VALUES (64,13,'Cotton Bath Towels',40,499,'Absorbent cotton bath towels for everyday use')")
c.execute("INSERT INTO products VALUES (65,13,'Microfiber Blanket',20,899,'Lightweight microfiber blanket for everyday comfort')")

'''





#CART_TABLE

c.execute('''CREATE TABLE IF NOT EXISTS cust_cart(
        cust_id INTEGER,
        cust_name TEXT,
        cat_name TEXT,
        subcategory_name TEXT,
        product_name INTEGER TEXT,
        product_price REAL,
        product_description TEXT,
        qnt INTEGER
        )''')






c.execute('''SELECT * FROM products''')
for row in c.fetchall():
    print(row)

c.execute('''SELECT * FROM product_subcategory''')
for row in c.fetchall():
    print(row)

c.execute('''SELECT * FROM product_category''')
for row in c.fetchall():
    print(row)






"""

"""
c.execute('''CREATE TABLE IF NOT EXISTS orders(
         cust_id INTEGER,
         cust_name TEXT,
         cust_phno TEXT,
         cust_address TEXT,
         product_name INTEGER,
         product_price REAL,
         product_description TEXT,
         product_qnt INTEGER,
         status TEXT
         )'''
        )
"""
"""
c.execute('''CREATE TABLE IF NOT EXISTS cust_addresses(
             cust_id INTEGER,
             cust_name TEXT,
             cust_addresses TEXT
             )'''
          )
"""


conn.commit()
conn.close()
