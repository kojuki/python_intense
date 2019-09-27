

#используя lambda функцию внутри функции
def attack_lambda(attacker, victim):
    victim['health'] = victim['health'] - (lambda atk, arm: atk/arm)(attacker['damage'], victim['armor'])
    return victim

#используя обычную функцию внутри функции
def attack(attacker, victim):
    victim['health'] = victim['health'] - armor_mod(attacker['damage'], victim['armor'])
    return victim

def armor_mod(atk, armor):
    total_dmg= atk/armor
    return total_dmg

player = {
    'name' : None,
    'health' : 100,
    'damage' : 30,
    'armor' : 1.2
    }
enemy = {
    'name' : None,
    'health' : 100,
    'damage' : 30,
    'armor' : 1.2
    }

player['name'] = input('введите имя игрока: ')
enemy['name'] = input('введите имя противника: ')
print(f'исходные параметры игрока: {player}')
print(f'исодные параметры врага: {enemy}')

attack(player, enemy)
print(f'параметры "{enemy["name"]}" после атаки "{player["name"]}" обычными функциями: {enemy}')
attack_lambda(player, enemy)
print(f'параметры "{enemy["name"]}" после атаки "{player["name"]}" лямбда функцией: {enemy}')