import sqlite3


def drop_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Products")
    connection.commit()
    connection.close()


def initiate_db():
    # create database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title Text NOT NULL,  
        description TEXT,
        price INTEGER NOT NULL
        );
        '''
    )

    connection.commit()
    connection.close()


def add_product(number):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    check_product = cursor.execute(f"SELECT id FROM Products WHERE id = {number}")

    if check_product.fetchone() is None:
        cursor.execute(
            f'''
            INSERT INTO Products(title, description, price) 
            VALUES (?, ?, ?)
            ''',
            (f"Product {number}", f"Описание {number}", f"Цена {number * 100}")
        )

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products
