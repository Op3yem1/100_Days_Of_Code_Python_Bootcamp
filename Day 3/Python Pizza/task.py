print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

#start here
price = 0
if size == "L":
    price +=25
elif size == "M":
    price += 20
else:
    price += 15
if extra_cheese == "Y":
    price += 1
if pepperoni == "Y":
    if size =="S":
        price += 2
    else:
        price += 3

print(f"Your final bill is: ${price}.")