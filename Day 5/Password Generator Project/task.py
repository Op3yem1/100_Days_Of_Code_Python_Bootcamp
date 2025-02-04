import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_types = ['letters', 'numbers', 'symbols']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Option 1: Basic password
my_password = ''
for char in range (0, nr_letters):
    my_password += random.choice(letters)
for char in range (0, nr_symbols):
    my_password += random.choice(symbols)
for char in range (0, nr_numbers):
    my_password += random.choice(numbers)
print(my_password)

# Option 2: Symbols letters and numbers in random places to make the password harder to crack!
my_hardpassword = ''
complete = False
total_chars = sum([nr_symbols,nr_numbers,nr_letters])
while not complete:
    char_choice = random.choice(all_types)
    if char_choice == 'letters' and nr_letters != 0:
         my_hardpassword += random.choice(letters)
         nr_letters -= 1
    elif char_choice == 'numbers' and nr_numbers != 0:
        my_hardpassword += random.choice(numbers)
        nr_numbers -= 1
    elif char_choice == 'symbols' and nr_symbols != 0:
        my_hardpassword += random.choice(symbols)
        nr_symbols -= 1
    if len(my_hardpassword) == total_chars:
        complete = True
print(my_hardpassword)