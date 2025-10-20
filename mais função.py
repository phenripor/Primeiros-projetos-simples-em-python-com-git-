def multipli(a , b):
    return a + b 
    
while True:
    number1 = int(input("first number: "))
    if number1 == 0:
        break
    number2 = int(input("Second number: "))
    print("Sum: ", multipli(number1,number2))