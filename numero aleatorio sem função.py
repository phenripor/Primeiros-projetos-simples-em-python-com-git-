import random


user_input = input("Do you want to play a game? (press 'e' to enter or 'x' to exit): ")

while True:

    number = random.randint(1, 100)
    print("Your number is:", number)

    number_Luck = random.randint(1, 100)
    print("The lucky number is:", number_Luck)

    if number == number_Luck:
        print("You won! (+1000 dol in your account)")
    else:
        print("You lost, try again! (-3000 dol in your account)")
        user_input = input("Do you want to continue playing? (press 'e' to enter or 'x' to exit):")

        if user_input.lower() == "x":
          print("Don't delay to back")
          break
          