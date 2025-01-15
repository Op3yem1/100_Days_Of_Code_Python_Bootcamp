print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = (input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people are splitting the bill? "))

#start here
adjusted_percent = float("1."+tip)
payment_amount = round((bill * adjusted_percent)/people,2)
print(f"Each person should pay £{payment_amount}")
