# a <= range(a, b) < b
for number in range(1, 10):
    print(number)

# PAUSE 1 - The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)