# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json,
# group.pickle соответственно. В файле group.json указать кодировку utf-8.


import json, pickle
my_favourite_group = {
                    'name': 'Г.М.О.',
                    'tracks': ['Последний месяц осени', 'Шапито'],
                    'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]
                    }
with open('group.json', 'w' , encoding='utf-8') as f:
    json.dump(my_favourite_group, f)  #  .dump Пишет в файл
print (f'вывод json: {json.dumps(my_favourite_group)}')   # .dumps пишет в память. Можно использовать для вывода в терминал
print(type(json.dumps(my_favourite_group)))  #для наглядности типа данных

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f) #  .dump Пишет в файл
print(f'вывод pickle в байты: {pickle.dumps(my_favourite_group)}') # .dumps пишет в память. Можно использовать для вывода в терминал
print(type(pickle.dumps(my_favourite_group))) #для наглядности типа данных

#альтернативный вариант. аналогично можно сделать с json
with open('group2.pickle', 'wb') as f:
    result = pickle.dumps(my_favourite_group)  #преобразование в байты и пишет их в переменную
    print (f'второй вывод pickle в байты: {result}') #вывод в терминал в формате байт из переменной
    f.write(result) #запись байтов из переменной в файл
    print(type(result)) #для наглядности типа данных


