import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()

def add_products():
    products = [
        ("Сухари""  1", 10.99, 20),
        ("Сухари "" 2", 25.49, 15),
    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()

def print_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def print_filtered_products():
    cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
    products = cursor.fetchall()
    for product in products:
        print(product)

def search_products_by_title(keyword):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + keyword + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

add_products()
update_quantity(1, 30)
update_price(2, 19.99)
delete_product(3)
print_all_products()
print_filtered_products()
search_products_by_title("мыло")


conn.close()