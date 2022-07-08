import pandas as pd
from connection_settings import db_name

rooms = 'rooms.json'
students = 'students.json'

df_rooms = pd.read_json(rooms)
df_students = pd.read_json(students)


def rooms_writer():
    query = f'INSERT INTO rooms VALUES '
    for i in range(len(df_rooms)):
        idd = df_rooms.loc[i, :][0]
        name = str(df_rooms.loc[i, :][1])
        add_to_query = f"({idd}, '{name}'), "
        query += add_to_query
    return f'{query[:-2]};'


def students_writer():
    query = f'INSERT INTO students VALUES '
    for i in range(len(df_students)):
        birthday = df_students.loc[i, :][0]
        idd = df_students.loc[i, :][1]
        name = str(df_students.loc[i, :][2])
        room = df_students.loc[i, :][3]
        sex = df_students.loc[i, :][4]
        add_to_query = f"('{birthday}', {idd}, '{name}', {room}, '{sex}'), "
        query += add_to_query
    return f'{query[:-2]};'

