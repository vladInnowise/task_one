import psycopg2
from connection_settings import *

from pandas_reader import rooms_writer, students_writer

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            rooms_writer()
        )
        cursor.execute(
            students_writer()
        )
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
