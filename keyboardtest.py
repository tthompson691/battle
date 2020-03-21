import keyboard

running = True
i = 1


while running:

    event = 0

    while event == 0:
        selection = keyboard.read_key()

        print("You smashed", str(selection))

        print(i)

        event = 1