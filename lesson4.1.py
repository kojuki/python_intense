def person (name,age,city):
    return(f'{name} ,{age} год(а), проживает в городе {city}')

name, age, city = input(f'введите имя,возраст и город, разделенные запятой, без пробелов:').split(sep=',')
print(person(name,age,city))