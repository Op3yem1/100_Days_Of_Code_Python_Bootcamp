def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? Loops from i == 1 to 19
# 2. When is the function meant to print "You got it"? When i == 20
# 3. What are your assumptions about the value of i? That i reaches 20

#Fix
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()