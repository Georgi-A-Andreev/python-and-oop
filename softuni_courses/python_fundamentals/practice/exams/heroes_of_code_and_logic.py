heroes_c = int(input())

heroes = {}
for _ in range(heroes_c):
    name, hp_str, mp_str = input().split()
    hp = int(hp_str)
    mp = int(mp_str)

    heroes[name] = [hp, mp]

while True:
    command = input()
    if command == 'End':
        break

    command = command.split(' - ')

    if command[0] == 'CastSpell':
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if mp_needed > heroes[hero_name][1]:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")

    elif command[0] == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]

        if heroes[hero_name][0] - damage <= 0:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")

    elif command[0] == 'Recharge':
        hero_name = command[1]
        amount = int(command[2])
        amount_to_recover = min(200 - heroes[hero_name][1], amount)
        heroes[hero_name][1] += amount_to_recover
        print(f"{hero_name} recharged for {amount_to_recover} MP!")

    elif command[0] == 'Heal':
        hero_name = command[1]
        amount = int(command[2])
        amount_to_recover = min(100 - heroes[hero_name][0], amount)
        heroes[hero_name][0] += amount_to_recover
        print(f"{hero_name} healed for {amount_to_recover} HP!")

for k, v in heroes.items():
    print(k)
    print(f'  HP: {v[0]}')
    print(f'  MP: {v[1]}')
