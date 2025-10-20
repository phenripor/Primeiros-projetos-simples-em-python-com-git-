ft_Score = int(input("Write your final test score\n"))

if (ft_Score == 100):
    print("Congratulations! You got a perfect score on the year!")
elif (ft_Score >= 90):
    print("You got a excelent note")

elif (ft_Score >= 80):
    print("You got a good note")

elif (ft_Score >= 70):
        print("You got a regular note")

elif(ft_Score >= 60):
     print("You pass on the risk, you can get better on the next year")

else:
     print("You failed the year.")
