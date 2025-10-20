while True:
    value = int(input("Enter the value in meters(if you want to stop, enter 0)\n"))
    
    if value == 0:
        break

    cm = float(value * 100)
    km = float(value / 1000)
    ml = float(value * 1000)

    print("The value in cm is:" , cm)

    print("The value in km is:" , km)

    print("The value in ml is:" , ml)

