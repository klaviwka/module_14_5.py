import sqlite3

def create_connection(db_file):
    """Создает соединение с базой данных SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def initiate_db():
    """Создает таблицы Products и Users, если они еще не созданы."""
    database = r"products.db"  # Укажите путь к вашей базе данных
    conn = create_connection(database)

    if conn is not None:
        try:
            cursor = conn.cursor()
            # Создаем таблицу Products
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL
                );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL
                );
            ''')
            conn.commit()  # Сохраняем изменения
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def add_user(username, email, age):
    """Добавляет нового пользователя в таблицу Users с начальным балансом 1000."""
    database = r"products.db"  # Укажите путь к вашей базе данных
    conn = create_connection(database)

    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Users (username, email, age, balance)
                VALUES (?, ?, ?, ?);
            ''', (username, email, age, 1000))
            conn.commit()  # Сохраняем изменения
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()


def is_included(username):
    """Возвращает True, если пользователь с данным именем существует в таблице Users, иначе False."""
    database = r"products.db"  # Укажите путь к вашей базе данных
    conn = create_connection(database)

    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT COUNT(*) FROM Users WHERE username = ?;
            ''', (username,))
            count = cursor.fetchone()[0]
            return count > 0  # Возвращаем True, если пользователь найден
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    return False  # Если соединение не удалось, возвращаем False


def get_all_products():
    """Возвращает все продукты из таблицы Products."""
    database = r"products.db"  # Укажите путь к вашей базе данных
    conn = create_connection(database)
    products = []

    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products;")
            products = cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    return products