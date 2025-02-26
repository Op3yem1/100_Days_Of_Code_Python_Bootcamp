try:
    age = int(input("How old are you?"))
except ValueError:
    print("That is not an acceptable format, Please try again using a numerical entry such as 12")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
