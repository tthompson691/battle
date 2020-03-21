import random, keyboard


# User thinks of a number between 1 and 1000, then program will figure it out in a few guesses
input("Think of your number between 1 and 1000. Press Enter to continue.")

running = True

guess_rangeh = 1000
guess_rangel = 1

while running:
    guess = random.randrange(guess_rangel, guess_rangeh)

    print("Is", str(guess), "your number? \n Press UP ARROW if your number is higher, DOWN ARROW if your number is"
                            "lower, or ENTER if correct.")

    keypressed = False
    i = 0
    

    while not keypressed:

        selection = keyboard.read_key()

        if keyboard.is_pressed('up'):
            guess_rangel = guess
            print("You pressed up", i)
            i += 1
            if not keyboard.is_pressed('up'):
                keypressed = True

        elif keyboard.is_pressed('down'):
            guess_rangeh = guess
            print("You pressed down", i)
            i += 1
            if not keyboard.is_pressed('down'):
                keypressed = True

        elif keyboard.is_pressed('enter'):
            print("I win!")
            running = False





