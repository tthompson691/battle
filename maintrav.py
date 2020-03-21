from Classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "A ZUKO ATTACKS!" + bcolors.ENDC)


while running:
    print("===========================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKGREEN + "You" + bcolors.ENDC + " attacked for",
              bcolors.BOLD + bcolors.OKBLUE + str(dmg) + bcolors.ENDC, "points of damage. Enemy HP:",
              bcolors.OKBLUE + str(enemy.get_hp()) + bcolors.ENDC)

    elif index == 1:
        print("=======================")
        print(bcolors.OKGREEN + "You" + bcolors.ENDC + " chose to cast a spell. Choose a spell you stupid idiot")
        player.choose_magic()

        magchoice = input("Choose spell:")
        magindex = int(magchoice) - 1

        magcost = magic[magindex]["cost"]

        if magcost > player.mp:
            print(bcolors.FAIL + "Not enough mp!"+ bcolors.ENDC)

        else:
            magdmg = player.generate_spell_damage(magindex)
            enemy.take_damage(magdmg)

            player.reduce_mp(magic[magindex]["cost"])

            print(bcolors.OKGREEN + "You" + bcolors.ENDC + " cast", magic[magindex]["name"], "for",
                 bcolors.OKGREEN + bcolors.BOLD + str(magdmg) + bcolors.ENDC, "damage.")
            print(bcolors.FAIL + "Enemy's" + bcolors.ENDC + " HP is now",
                  bcolors.OKBLUE + str(enemy.get_hp()) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Your" + bcolors.ENDC + " MP is now", bcolors.WARNING + str(player.get_mp())
                  + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "Enemy" + bcolors.ENDC, "attacks for", bcolors.FAIL + bcolors.BOLD + str(enemy_dmg)
          + bcolors.ENDC, "damage.")
    print(bcolors.OKGREEN + "Your" + bcolors.ENDC, "HP:", bcolors.OKBLUE + bcolors.BOLD + str(player.get_hp())
          + bcolors.ENDC)


