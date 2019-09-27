
name = input('Введите имя пациента (или exit что бы завершить работу): ') #Первый ввод для запуска программы или закрытия.
while name != 'exit':
    surname = input('Введите фамилию пациента: ')
    weight = int(input('введите вес пациента: '))
    age = int(input('введите возраст пациента: '))
    if age < 0 :
        print('Хорошая попытка!')
    elif age >= 0 and age <= 30:    # 0 лет = новорожденный, не противоречит задаче)
        if weight < 0 :
            result='кажется мы нашли антиматерию!'
        elif weight >= 0 and weight < 50:
            result='его бы покормить'
        elif weight >= 50 and weight <= 120:
            result='хорошее состояние'
        elif weight > 120:
            result='!WARNING! Heavy object approaching'
    elif age > 30 and age <= 40:
        if weight < 0:
            result='кажется мы нашли антиматерию!'
        elif (weight >= 0 and weight < 50) or weight > 120:
            result='cледует заняться собой'
        elif weight >= 50 and weight <= 120:
            result='хорошее состояние'
    else:
        if weight < 0 :
            result='кажется мы нашли антиматерию!'
        elif (weight >= 0 and weight < 50) or weight > 120:
            result='следует обратится к врачу!'
        elif weight >= 50 and weight <= 120:
            result='хорошее состояние'
    print(name, surname, age, 'год, вес', weight, '-', result)
    name = input('Введите имя пациента (или exit что бы завершить работу): ') #стоит в конце цикла, что бы новый цикл начался либо с имени либо с выхода.
print('Завершение программы')