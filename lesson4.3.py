
def attack(atacker, victim):
    victim['health'] = victim['health'] - atacker['damage']
    return victim


# для игрока сделаем изменение значения существующего ключа
player = {
    'name' : None,
    'health' : 100,
    'damage' : 50
    }
# А для противниа сделаем ввод нового ключа со значением
enemy = {
    'health' : 100,
    'damage' : 50
    }

player['name'] = input('введите имя игрока: ')
enemy['name'] = input('введите имя противника: ')
print(f'исходные параметры игрока: {player}')
print(f'исодные параметры врага: {enemy}')

attack(player, enemy)
print(f'параметры "{enemy["name"]}" после атаки "{player["name"]}": {enemy}')
