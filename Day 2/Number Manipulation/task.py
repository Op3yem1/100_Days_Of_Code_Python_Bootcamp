bmi = 84 / 1.65 ** 2
print(bmi)

#flooring i.e ridding all the decimal points
print(int(bmi))

#rounding up/down to nearest whole number
print(round(bmi))

#f-strings
print(f"{round(bmi)} is rounded up from {bmi}")