from random import randint

l = []

for i in range(0, 100000000, 10):
    l.append(randint(0, 10) + i)

idx = randint(0, 10000000)
num = l[idx]

for i in l:
    if i == num:
        print(num)
        print("Found")
