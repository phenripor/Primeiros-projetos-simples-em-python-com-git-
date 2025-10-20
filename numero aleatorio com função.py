import random
def logic_game(a, b):
    if a == b:
        return "You win!"
    else:
        return "You are wrong! Try again!"
    
while True:
    number_User = int(input("Enter a number between 1 and 59: "))

    if number_User < 1 or number_User > 59:
        print("Invalid number! Please try again.")
        continue

    number_comp = random.randint(1,59)

    print("The computer chose:", number_comp)
    print(logic_game(number_User, number_comp))

    if number_User == number_comp:
        break