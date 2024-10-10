import sqlite3


# Группа SQL запросов для задания
# Создание пустой таблицы
create_table = """
    CREATE TABLE IF NOT EXISTS 
    Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    """
# Обновление баланса пользователя
update_users = """
    UPDATE Users
    SET balance = 500
    WHERE id % 2 != 0
    """
# Выбор пользователей по возрасту
select_users_by_age = """
    SELECT username, email, age, balance FROM Users
    WHERE age != 60
    """
# Удаление таблицы
drop_table = """
    DROP TABLE IF EXISTS Users
    """
# Вставка данных в таблицу Users
insert_users = "INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)"
# Удаление данных из таблицы Users по id
delete_user = "DELETE FROM Users WHERE id = ?"

# Собираем список с данными для заполнения таблицы
users_data = [(f"User{i}", f"example{i}@gmail.com", i*10, 1000) for i in range(1, 11)]

# Создаем соединение с базой данных
connection = sqlite3.connect("not_telegram.db",)
cursor = connection.cursor()

# Удаляем таблицу если она есть и создаем новую
cursor.executescript(f"{drop_table} ; {create_table}")

# Заполняем таблицу
cursor.executemany(insert_users, users_data)

# Обновление баланса пользователя
cursor.execute(update_users)

# Удаление каждого 3-го пользователя
cursor.executemany(delete_user, [(id_,) for id_ in range(1, 11, 3)])

# Выборка пользователей с фильтром по возрасту (все кроме 60-ти летние)
cursor.execute(select_users_by_age)
data = cursor.fetchall()

# Сохраняем изменения в базу данных
connection.commit()
# Закрываем соединение с базой данных
connection.close()

# Выводим отфильтрованные данные пользователей на экран
for username, email, age, balance in data:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")
