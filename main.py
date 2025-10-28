# 1. создать функцию для подключения к postgres и проверить подключение
# 2. создать функцию для сбора данных из таблицы и проверить
# 3. создать функцию для вставки данных в таблицу и проверить
import psycopg2

def con(name: str, usr: str, psswrd: str, hst: str, pst: str) -> None:
    connect = psycopg2.connect(
        dbname = name,
        user = usr,
        password = psswrd,
        host = hst,
        port = pst
    )
    return connect

def slct(connection, query: str):
    with connection.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

connection = con("postgres", "postgres", "1234", "localhost", "5432")

print(slct(connection, "SELECT * FROM people"))

def insrt(connection, query: str, params = None):
    with connection.cursor() as cur:
        cur.execute(query, params)
        connection.commit()
    return None