from queries_to_db import get_info
from query_text import *

q1 = query_one # список комнат и количество студентов в каждой из них
q2 = query_two # топ-5 комнат, где самый маленький возраст среди студентов
q3 = query_three # топ-5 комнат с самой большой разницей в возрасте студентов
q4 = query_four # список комнат, где живут разнополые студенты

query = q4

"""
to 
"""
get_info(query, 'xml', True)

