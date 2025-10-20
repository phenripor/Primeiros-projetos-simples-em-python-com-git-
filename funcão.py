def calculate_tax(value):
    if value < 1000:
        value *= 0.1

    elif value < 2000:
        value *= 0.2

    else:
        value *= 0.3

    return value

while True:
    price = int(input("Enter the price: "))
    if price == 0:
        break
    total = price + calculate_tax(price)
    print("The original price is: ", price , "the tax is: ", calculate_tax(price), "and the total is : ", total)