import art

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def add(n1, n2):
    return n1 + n2

math_operators = {"+": add,
                  "-":subtract,
                  "*":multiply,
                  "/":divide}
calculator_on = True
carry_on = "N"


while calculator_on:
    if carry_on == "N":
        print(art.logo)
        result = 0
        first_num = int(input("Please enter the 1st number: "))
    second_num = int(input("Please enter the 2nd number: "))
    operator = input(f"Would you like to add (a), subtract (s), multiply (m) or divide (d) {first_num} and {second_num}? ").lower()
    if operator == "a":
        result = add(first_num,second_num)
    elif operator == "s":
        result = subtract(first_num, second_num)
    elif operator == "d":
        result = divide(first_num, second_num)
    elif operator == "m":
        result = multiply(first_num, second_num)
    else:
        print("Invalid operator chosen, please check your spelling and try again ")
    print(f"The result is {result}")
    carry_on = input("Would you like to continue using this result in further calculations? Y/N ").upper()
    if carry_on == "Y":
        first_num = result
    else:
        if input("Would you like to stop calculating? Y/N ").upper() == "Y":
            calculator_on = False