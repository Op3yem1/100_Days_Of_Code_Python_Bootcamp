import random

#Random Whole Numbers Within a Range - up to and including the upper bound
print(random.randint(1, 10))

#Random float where 0.0 >= x < 1.0
print(random.random())
#Random float where 0.0 >= x < 10.0 (1 x factor specified)
print(random.random() * 10)
#Alternative way to create random float ange specified e.g 0.0 <= x >= 50.0
print(random.uniform(1,50))

#NB: random.random() does not include the upper bound, random.uniform() does

#HEADS OR TAILS
choice = (random.randint(1,2))
if choice == 1:
    print(f"{choice} - Heads")
else:
    print(f"{choice} - Tails")