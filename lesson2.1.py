print('Задание 1', '', sep='\n')                 # вывод начала задания и пропуск 1 строки
#============================================Задание 1============================================
#===============Условие===============
#Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#Примечание. Списки создайте вручную, например так:
#my_list_1 = [2, 5, 8, 2, 12, 12, 4]
#my_list_2 = [2, 7, 12, 3]
#============Конец условия============

List_1 = [2, 2, 1, 5, 2, 34, 1, 65, 7, 5, 2, 3]  # исходный лист
print('Исходный лист: ', List_1)                 # печатать на вывод исходный лист можно только тут, так как посли атрибута List_1.remove исходный лист будет изменен.
List_2 = [2, 5, 65]                              # лист значений для удаления
print('Лист значений для удаления: ', List_2)    # Этот лист можно печатать и перед выводом результата, он не меняется.
for number in List_2:                            # берет каждое значение из списка 2 и записывает в переменную number
    for i in range(List_1.count(number)):        # считает количество number в списке List_1 и создает range из этого параметра.
        List_1.remove(number)                    # Удаляет number из List_1 столько раз, сколько number  входит в List_1.
print('Результат удаления значений второго листа из первого:', List_1)
#=========================================Конец задания 1=========================================
print('Конец задания 1', '', sep='\n')           # вывод конца задания и пропуск 1 строки

print('Задание 2', '', sep='\n')                 # вывод начала задания и пропуск 1 строки
#============================================Задание 2============================================
#===============Условие===============
#Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде
#Например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
#============Конец условия============

# объявим словари для дня и месяца
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
# Если делать программу зацикленой, то нужно раскоментить строки 41 42 54 и расставить отступы с 42 по 54 строку
#date = None
#while True:
# Интерактивный ввод даты и преобразование его к типу данных list используя разделитель точку
date = input('введите дату в формате "dd.mm.yyyy": ').split('.')
# проверка даты на ввод. Если дата введена не через точку, если в поле дня введено более 31 или менее 01,
# или не двузначное число (1 вместо 01) - выдаст ошибку.
# Год проверять нет смысла, так как он может быть любой. Отрицательный - до нашей эры.
if date[0] not in day.keys() or date[1] not in month.keys():
    print('Дата введена не верно')
else:
# Если проверка введенных дат проходит - выводим, что просили в условии задачи.
    print(day[date[0]], month[date[1]], date[2], 'года')
#Если циклили программу - далее точка выхода из цикла.
#        break
#=========================================Конец задания 2=========================================
print('Конец задания 2', '', sep='\n')           # вывод конца задания и пропуск 1 строки

print('Задание 3', '', sep='\n')                 # вывод начала задания и пропуск 1 строки
#============================================Задание 3============================================
#===============Условие===============
#Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.
#Примечание. Списки создайте вручную, например так: my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#В этом случае ответ будет: [5, 8]
#============Конец условия============
List_1 = [2, 2, 1, 5, 2, 34, 1, 65, 7, 5, 2, 3]  # исходный лист
print('Исходный лист: ', List_1)                 # печатать на вывод исходный лист можно только тут, так как посли атрибута List_1.remove исходный лист будет изменен.
#Запускаем цикл проверки уникальных чисел изначального списка unical_number. Для этого преобразуем лист в множество set(List_1) (множество содерджит только уникалные значения, все повторы убираются)
#По этому множеству будет проверяться количество вхождений чисел в начальный список.
for unical_number in set(List_1):
#Если уникальное число входит в изнчальный список более 1 раза
    if List_1.count(unical_number) > 1:
#Запускаем цикл удаления этого числа из изначального списка столько раз, сколько оно входит.
        for i in range(List_1.count(unical_number)):
            List_1.remove(unical_number)
print(f'Список только из чисел, входящих в изначальный список только 1 раз:\n{List_1}\n')
#Новый формат вывода "Python f-string". Работает с версии 3.6 и старше. Намного удобней по сравнению с .format()


#=========================================Конец задания 3=========================================
print('Конец задания 3', '', sep='\n')           # вывод конца задания и пропуск 1 строки