from functions import write, jsonify, xmlify
from query_text import *


q1 = query_one      # список комнат и количество студентов в каждой из них
q2 = query_two      # топ-5 комнат, где самый маленький возраст среди студентов
q3 = query_three    # топ-5 комнат с самой большой разницей в возрасте студентов
q4 = query_four     # список комнат, где живут разнополые студенты

i1 = index_one      # индекс b-tree для айдишника студентов
i2 = index_two      # индекс b-tree для айдишника комнат

write(q3)           # выведут информацию
write(q4)

write('SELECT VERSION();')  # выведет информацию

jsonify(write(q2))  # создаст .json файл

xmlify(write(q3))   # создаст .xml файл
