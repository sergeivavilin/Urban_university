import sqlite3


def drop_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Products")
    cursor.execute("DROP TABLE IF EXISTS Users")
    connection.commit()
    connection.close()


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Создаем таблицу продуктов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title Text NOT NULL,  
        description TEXT,
        price INTEGER NOT NULL
        );
        '''
        )

    # Создаем таблицу пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username Text NOT NULL,  
        email Text NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        '''
        )

    connection.commit()
    connection.close()


def add_product(number):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    check_product = cursor.execute(f"SELECT id FROM Products WHERE id = {number}").fetchone()

    if check_product is None:
        cursor.execute(
            f'''
            INSERT INTO Products(title, description, price) 
            VALUES (?, ?, ?)
            ''',
            (f"Product {number}", f"Описание {number}", f"Цена {number * 100}")
        )
    connection.commit()
    connection.close()


# Проверяем есть-ли такой пользователь в базе данных
def is_included(name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    check_user = cursor.execute(f"SELECT id FROM Users WHERE username = '{name}'").fetchone()
    connection.close()

    if check_user is None:
        return False
    return True


# Добавляем пользователя если такого нет
def add_user(username, email, age):
    user_exist = is_included(username)

    if not user_exist:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(
            f'''
            INSERT INTO Users(username, email, age, balance)
            VALUES (?, ?, ?, ?)
            ''',
            (username, email, age, "1000")
        )
        connection.commit()
        connection.close()
        return True
    return False


# Получаем список всех продуктов
def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products

if __name__ == '__main__':
    drop_db()
    # initiate_db()
    # add_user(username="test", email="test@test.com", age="20")
    # add_product(1)
