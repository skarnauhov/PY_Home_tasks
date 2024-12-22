import sqlite3


PRODUCTS = ('пусто', 'Яблоко', 'Груша', 'Апельсин', 'Хурма')

def initiate_db():
    connection = sqlite3.connect('UrbanM13Bot.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute("SELECT * FROM Products")
    if len(cursor.fetchall()) == 0:
        for _ in range(1, len(PRODUCTS)):
            cursor.execute(f"INSERT INTO Products (title, description, price) VALUES ('{PRODUCTS[_]}', '{_*100} ккал', '{_*200}')")
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('UrbanM13Bot.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result