import psycopg2
from connection_settings import *
from query_text import query_one, query_two, query_three
import json
import xml.etree.cElementTree as ET


def jsonify(tuples):
    dicted = dict(tuples)
    json_dict = json.dumps(dicted)
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


def get_info(query, format, printer=False):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:

            cursor.execute(query)
            c = cursor.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
    if format == 'json':
        jsonify(c)

    elif format == 'xml':
        xmlify(c)

    if printer is True:
        for i in c:
            print(i, end='\n')
    return c


'''with open('result.txt', 'w') as f:
            f.write('room  students \n')
            for i in cursor.fetchall():
                f.write(str(i))
                f.write('\n')'''
