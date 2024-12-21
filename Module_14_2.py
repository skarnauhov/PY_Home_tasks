import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("SELECT * FROM Users")
if len(cursor.fetchall()) == 0:
    for _ in range(1,11):
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (f'User{_}', f'example{_}@gmail.com', f'{_*10}', f'{1000}'))

    # cursor.execute("SELECT * FROM Users")
    # users = cursor.fetchall()
    # for user in users:
    #     print(user)

    cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 != 0")

    # cursor.execute("SELECT * FROM Users")
    # users = cursor.fetchall()
    # for user in users:
    #     print(user)

    cursor.execute("SELECT id FROM Users")
    id_s = cursor.fetchall()
    for id_ in id_s[::3]:
        cursor.execute("DELETE FROM Users WHERE id = ?", (id_[0],))

    # cursor.execute("SELECT * FROM Users")
    # users = cursor.fetchall()
    # for user in users:
    #     print(user)

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(id) FROM Users")
users_quantity = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

print(total_balance/users_quantity)

connection.commit()
connection.close()