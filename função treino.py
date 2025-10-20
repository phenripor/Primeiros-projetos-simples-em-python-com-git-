def calculate_tax(value):
    if value < 1000:
        value *= 0.1

    elif value < 2000:
        value *= 0.2

    elif value < 3000:
        value *= 0.30

    else:
        value *= 0.4

    return value

prices = []
while True:
   cli_value = float(input("Enter the value:\n (Enter 0 to exit) "))
   if cli_value == 0:
       break
   

   for i in range(cli_value):
       price = float(input("Enter the price of the product:\n "))
       prices.append(price)

print(f"The total value with tax is: {total:.2f}")