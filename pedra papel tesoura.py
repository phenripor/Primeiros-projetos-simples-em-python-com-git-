while True:
    hand1 = input("Rock, paper or scissors?")
    hand2 = input("Rock, paper or scissors?")
    if hand1 == hand2:
       print("It's a tie!")
    elif (hand1 == "rock" and hand2 == "scissors"):
        print("Hand 1 wins!")
    elif (hand1 == "scissors" and hand2 == "paper"):
        print("Hand 1 wins!")
    elif (hand1 == "paper" and hand2 == "rock"):
        print("Hand 1 wins!")
    else:
        print("Hand 2 wins!")