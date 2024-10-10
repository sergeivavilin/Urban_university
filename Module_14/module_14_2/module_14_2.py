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

# Подсчет количества всех пользователей
count_users = "SELECT COUNT(*) FROM Users"

# Подсчет суммы всех балансов
sum_balance = "SELECT SUM(balance) FROM Users"

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

# Удаляем пользователя с id==6
cursor.execute(delete_user, (6,))

# Подсчет количества всех пользователей
cursor.execute(count_users)
total_users= cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute(sum_balance)
total_balance = cursor.fetchone()[0]

# Сохраняем изменения в базу данных
connection.commit()
# Закрываем соединение с базой данных
connection.close()

print(total_balance / total_users)