# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.

import json, pickle

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)
print (f'импорт через pickle: {my_favourite_group}')
#проверка типа данных, что бы убедиться в правильности импорта
print(type(my_favourite_group))

with open ('group.json', 'r', encoding='utf-8') as f:
    my_favourite_group_json = json.load(f)
print (f'импорт через json: {my_favourite_group_json}')
#проверка типа данных, что бы убедиться в правильности импорта
print(type(my_favourite_group_json))
