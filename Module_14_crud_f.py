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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    cursor.execute("SELECT * FROM Products")
    if len(cursor.fetchall()) == 0:
        for _ in range(1, len(PRODUCTS)):
            cursor.execute(f"INSERT INTO Products (title, description, price) "
                           f"VALUES ('{PRODUCTS[_]}', '{_*100} ккал', '{_*200}')")
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

def add_user(username, email, age, balance=1000):
    connection = sqlite3.connect('UrbanM13Bot.db')
    cursor = connection.cursor()
    cursor.execute(f'''
    INSERT INTO Users(username, email, age, balance) VALUES
    ('{username}', '{email}', '{age}', '{balance}')
    ''')
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('UrbanM13Bot.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    if user is None:
        return False
    else:
        return True
