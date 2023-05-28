n = int(input())
hero_dict = {}

for i in range(n):
    hero, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    hero_dict[hero] = [hp, mp]

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' - ')
    hero_name = command[1]

    if command[0] == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[3]
        if mp_needed <= hero_dict[hero_name][1]:
            hero_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name}"
                  f" and now has {hero_dict[hero_name][1]} MP!")
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif command[0] == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        hero_dict[hero_name][0] -= damage
        if hero_dict[hero_name][0] <= 0:
            hero_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            print(f"{hero_name} was hit for {damage} HP "
                  f"by {attacker} and now has {hero_dict[hero_name][0]} HP left!")

    elif command[0] == 'Recharge':
        recharge_amount = int(command[2])
        check = hero_dict[hero_name][1] + recharge_amount
        hero_dict[hero_name][1] = min(200, hero_dict[hero_name][1] + recharge_amount)
        print(f"{hero_name} recharged for "
              f"{min(recharge_amount - (check - 200), recharge_amount)} MP!")

    else:
        amount = int(command[2])
        check = hero_dict[hero_name][0] + amount
        hero_dict[hero_name][0] = min(100, hero_dict[hero_name][0] + amount)
        print(f"{hero_name} healed for {min(amount - (check - 100), amount)} HP!")

for hero_name, my_list in hero_dict.items():
    print(hero_name)
    print(f'  HP: {my_list[0]}')
    print(f'  MP: {my_list[1]}')
