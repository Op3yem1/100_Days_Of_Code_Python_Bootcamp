import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#option 1
print(random.choice(friends))
#option 2
print(friends[random.randint(0,len(friends)-1)])