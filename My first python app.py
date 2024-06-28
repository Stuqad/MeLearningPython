print('1. Recommended Music')
print('2. Recommended Food')
print('3. Recommended Game')
print('4. Play a game (Guess the number.)')
question = input("What do you want? Choose from the list above. Type 'off' to turn off the program!")
while question != "off":
    if question == "1":
        print("1. Rock")
        print("2. Pop")
        print("3. Classical")
        question = input('What genre of music do you want? Choose from the list above. Type 'off' to turn off the program!')
        if question == "1":
            print('I recommend you listen to - Queen We Will Rock You.')
        elif question == "2":
            print('I recommend you - Prince When Doves Cry.')
        elif question == "3":
            print('I recommend you - Schubert’s Trout.')
        else:
            print('This option does not exist!')
    elif question == "2":
        print('1. Seafood')
        print('2. Vegetarian Food')
        print('3. Dairy Product')
        question = input('What type of food do you want? Choose from the list above. Type 'off' to turn off the program!')
        if question == "1":
            print('I recommend you - Seabass.')
        elif question == "2":
            print('I recommend you - Salad Leaves.')
        elif question == "3":
            print('I recommend you - Milk.')
        else:
            print('This option does not exist!')
    elif question == "3":
        print('1. RPG')
        print("2. Strategy")
        print("3. Simulator")
        question = input("What genre of game do you prefer? Choose from the list above. Type 'off' to turn off the program!")
        if question == "1":
            print('I recommend you - Dark Souls 2.')
        elif question == "2":
            print("I recommend you - Civilization.")
        elif question == "3":
            print("I recommend you - Flight Simulator 2.")
        else:
            print('This option does not exist!')
    elif question == "4":
        guess_number = input("Guess the number (From 0 to 100)! Type 'off' to turn off the program!")
        if guess_number == "off":
            break
        guess_number = int(guess_number)
        attempts = 1
        while guess_number != 39:
            if guess_number < 39:
                print("Wrong number! Higher")
            else:
                print("Wrong number! Lower")
            attempts += 1
            guess_number = input("Guess the number (From 0 to 100)! Type 'off' to turn off the program!")
            if guess_number == "off":
                break
            guess_number = int(guess_number)
            if attempts == 3:
                print('Attempts are over 3/3')
                break
        if guess_number == 39:
            print("Hooray! You guessed the number on attempt number", attempts, ".")
    question = input("What do you want? Choose from the list above. Type 'off' to turn off the program!")
