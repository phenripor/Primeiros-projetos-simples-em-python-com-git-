

   
menu = int(input("Press 1 to enter in the menu, 2 to exit\n"))

count_P = 0 # Initialize the counter    
m_Age = 0 # Initialize the age sum
m_Person = "" # Initialize the name of the youngest person
while (True):
    name = str(input("\nEnter your name: \n"))
    count_P += 1
    # below iniciates the logics of age
    age = int(input("Enter your age: \n"))
    if (age > m_Age):
        m_Age = age
        m_Person = name
    menu = int(input("\nPress 1 to continue in the menu, 2 to exit\n"))
    if menu == 2:
        break

print(f"The total of names entered is: {count_P}")
print(f"The oldest person is: {m_Person} with age {m_Age}")
