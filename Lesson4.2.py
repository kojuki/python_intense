#первые три варианта - встроенная функция max.
#первый вариант в функцию передает лист (количество значений не ограничено)
def max_func_list (num_list):
    return max(num_list)

#второй использует args (количество значений не ограничено)
def max_func_args (*args):
    return max(args)

#третий для трех переменных (будут взяты первые три значения из введеных)
def max_func_3_num (num1,num2,num3):
    return max(num1,num2,num3)

#следующие три функции с ручным определением максимального значения.
#первый вариант в функцию передает лист (количество значений не ограничено)
def manual_max_list (num_list):
    max = num_list[0]
    for num in num_list:
        if num > max : max = num
    return max

#второй использует args (количество значений не ограничено)
def manual_max_args (*args):
    max = args[0]
    for num in args:
        if num > max : max = num
    return max

#третий для трех переменных (будут взяты первые три значения из введеных)
def manual_max_3_num (num1,num2,num3):
    max = num1
    if num2 > max : max = num2
    if num3 > max : max = num3
    return max

my_num_list = list(map(int, input(f'введите числа (не ограничено по количеству) через запятую: ').split(',')))    #можно вводить более 3х чисел
print (f'исходный лист:\n{my_num_list}')   #исходный лист
print(f'встроенная функция max, с передачей листа в кастомную функцию: {max_func_list(my_num_list)}')
print(f'встроенная функция max, с передачей args в кастомную функцию: {max_func_args(*my_num_list)}')
print(f'встроенная функция max, с передачей первых 3 чисел в кастомную функцию: {max_func_3_num(my_num_list[0],my_num_list[1], my_num_list[2])}')

print(f'кастомная функция определения максимального числа, с передачей листа в функцию: {manual_max_list(my_num_list)}')
print(f'кастомная функция определения максимального числа, с передачей args в функцию: {manual_max_args(*my_num_list)}')
print(f'кастомная функция определения максимального числа, с передачей первых 3 чисел в функцию: {manual_max_3_num(my_num_list[0],my_num_list[1], my_num_list[2])}')