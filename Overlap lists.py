a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for x in set(a):  # set command removes duplicates from a list
    if x in set(b):  # a set is a list with unique items
        print(x)


import random
a, b = random.sample(range(20), 10), random.sample(range(20), 10)
result = [i for i in set(a) if i in b]
print(result)
