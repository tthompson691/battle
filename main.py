from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item
import random

#comment text 2


print("\n\n")
# Create black magic
fire = Spell("Fire", 25, 100, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 99999)
hielixer = Item("MegaElixer", "elixer", "Fully restors party's HP/MP", 99999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]

# instantiate people
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Zuko   ", 11200, 701, 525, 25, enemy_spells, [])
enemy2 = Person("Bubba  ", 1250, 130, 560, 325, enemy_spells, [])
enemy3 = Person("Pup pup", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "A ZUKO ATTACKS!" + bcolors.ENDC)


while running:
    print("===========================")

    print("\n\n")
    print("NAME                         HP                                     MP")
    for player in players:

        player.get_stats()                                                   # print each party member's health/mp bars

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()                                                  # print enemy's health/mp bars

    for player in players:                                                      # choose attack, magic, or item
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:   # attack
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)                               # choose target

            enemies[enemy].take_damage(dmg)
            print(bcolors.OKGREEN + "You" + bcolors.ENDC + " attacked " + enemies[enemy].name + " for",
                  bcolors.BOLD + bcolors.OKBLUE + str(dmg) + bcolors.ENDC + " damage.")

            if enemies[enemy].get_hp() == 0:                                  # if an enemy has died, remove it from the
                print(enemies[enemy].name.replace(" ", "") + " has died.")                   # list
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), "points of damage" +
                      bcolors.ENDC + " to " + enemies[enemy].name)

                if enemies[enemy].get_hp() == 0:                                  # if an enemy has died, remove it from
                    print(enemies[enemy].name.replace(" ", "") + " has died.")                   # the list
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name,  "heals for", str(item.prop), "HP." + bcolors.ENDC)

            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals " + str(item.prop) + " points of damage" + bcolors.ENDC
                      + " to " + enemies[enemy].name)

                if enemies[enemy].get_hp() == 0:                          # if an enemy has died, remove it from the
                    print(enemies[enemy].name.replace(" ", "") + " has died.")           # list
                    del enemies[enemy]

    # check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for player in players:
        if player.get_hp == 0:
            defeated_players += 1

    # Check if enemy won
    for enemy in enemies:
        if enemy.get_hp == 0:
            defeated_enemies += 1

    # Check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False

    print("\n")
    # enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, 2)
            enemy_dmg = enemies[0].generate_damage()

            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name.replace(" ", "") + bcolors.ENDC, "attacks " +
                players[target].name.replace(" ", "") + " for", bcolors.FAIL +
                bcolors.BOLD + str(enemy_dmg) + bcolors.ENDC, "damage.")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals" + enemy.name + "for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals " +
                      str(magic_dmg) + " damage to " + players[target].name.replace(":", "") + bcolors.ENDC)
                if players[target].get_hp() == 0:                          # if an enemy has died, remove it from the
                    print(players[target].name.replace(" ", "") + " has died.")           # list
                    del players[player]


