year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994: #Pause 1: 1994 not accounted for in if statement. Change operator to <=
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
