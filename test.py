List_1 = [2, 2, 1, 5, 2, 34, 1, 65, 7, 5, 2, 3]  # исходный лист
print('Исходный лист: ', List_1)                 # печатать на вывод исходный лист можно только тут, так как посли атрибута List_1.remove исходный лист будет изменен.
List_2 = [2, 5, 65]                              # лист значений для удаления
print('Лист значений для удаления: ', List_2)    # Этот лист можно печатать и перед выводом результата, он не меняется.
for number in List_2:                            # берет каждое значение из списка 2 и записывает в переменную number
    for i in range(List_1.count(number)):        # считает количество number в списке List_1 и создает range из этого параметра.
        List_1.remove(number)                    # Удаляет number из List_1 столько раз, сколько number  входит в List_1.
print('Результат удаления значений второго листа из первого:', List_1)

day = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое',
       '07': 'Седьмое',
       '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одиннадцатое', '12': 'Двенадцатое',
       '13': 'Тринадцатое',
       '14': 'Четырнадцатое', '15': 'Пятнадцатое', '16': 'Шестнадцатое', '17': 'Семнадцатое', '18': 'Восемнадцатое',
       '19': 'Девятнадцатое', '20': 'Двадцатое', '21': 'Двадцать первое', '22': 'Двадцать второе',
       '23': 'Двадцать третье',
       '24': 'Двадцать четвертое', '25': 'Двадцать пятое', '26': 'Двадцать шестое', '27': 'Двадцать седьмое',
       '28': 'Двадцать восьмое', '29': 'Двадцать девятое', '30': 'Тридцатое', '31': 'Тридцать первое'}
month = {'01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня', '07': 'Июля',
         '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'}
date = input('введите дату в формате "dd.mm.yyyy": ').split('.')
if date[0] not in day.keys() or date[1] not in month.keys():
    print('Дата введена не верно')
else:
    print(day[date[0]], month[date[1]], date[2], 'года')


List_1 = [2, 2, 1, 5, 2, 34, 1, 65, 7, 5, 2, 3]  # исходный лист
print('Исходный лист: ', List_1)                 # печатать на вывод исходный лист можно только тут, так как посли атрибута List_1.remove исходный лист будет изменен.
for unical_number in set(List_1):
    if List_1.count(unical_number) > 1:
        for i in range(List_1.count(unical_number)):
            List_1.remove(unical_number)
print(f'Список только из чисел, входящих в изначальный список только 1 раз:\n{List_1}')