from connection_settings import connection  # file with connection settings
import psycopg2
import pandas as pd
import numpy
import json
import xml.etree.cElementTree as ET

'''functions connect() and disconnect() are provided for convenience so that i don't have to 
write code to connect and disconnect to db manually every time'''


def connect():
    connector = psycopg2.connect(  # attribute with all data needed to establish connection
        host=connection['host'],
        user=connection['user'],
        password=connection['password'],
        database=connection['database'],
        port=connection['port']
    )
    connector.autocommit = True
    return connector


def disconnect():
    connect().cursor().close()
    connect().close()


'''function write() helps us to reduce the amount of written code, accepts query as a string'''


def write(query):
    cursor = connect().cursor()
    cursor.execute(query)
    try:
        result = cursor.fetchall()
    except psycopg2.Error:
        pass
    try:
        cursor.execute(query)
        print(cursor.fetchall())
    except psycopg2.Error:
        pass
    disconnect()
    return result


'''function load_file(filename, table_name) loads files to a database. Accepts name of file and name of table
where we insert data'''


def load_file(filename: str, table_name: str):
    file = pd.read_json(filename)
    table = table_name
    values = ''  # concatenated string with all values needed to add

    for line in range(len(file)):  # iterate through each string of a pandas dataframe, lines
        c = ''
        for elem in range(len(file.columns)):  # extract each column in line
            element = file.iloc[line, :][elem]
            # type_checker, since data is loaded in different formats
            if type(element) == str:
                c += f"'{element}', "
            elif type(element) == numpy.int64:
                c += f"{element}, "
            else:
                raise TypeError('Необрабатываемый тип данных')
        q_line = f'({c[:-2]}), '
        values += q_line  # adding a set of values into string

    query = f"INSERT INTO {table} VALUES {values[:-2]};"  # final string with the query

    # next, we send the query to the database with our function write()

    write(query)
    print('well done, boss')


'''functions jsonify() and xmlify() return the result of a query in either .json or .xml files'''


def jsonify(tuples):
    dicted = dict(tuples)
    json_dict = json.dumps(dicted, indent=4, sort_keys=True, default=str)
    with open('result.json', 'w') as f:
        f.write(json_dict)


def xmlify(tuples):
    dicted = dict(tuples)
    root = ET.Element('root')
    doc = ET.SubElement(root, 'doc')
    c = 1
    for i, y in dicted.items():
        ET.SubElement(doc, f'number{c}', room=f'{i}').text = f'{y} students'
        c += 1
    tree = ET.ElementTree(root)
    tree.write('result.xml')
