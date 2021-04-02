a = "asd"
a1 = a
a = 1
print(a1)

if a != 1:
    print("Not 1")
else:
    print("Else")

b = "a is 1" if a == 2 else "a is not 1"

print(b)
if a == 1:
    b = True
else:
    b = False

for i in "abc":
    print(i)

for i in range(1, 10, 5):
    print(i)

string = "abcd"
d = 0
while string[d] != "c":
    d += 1


def a_b(a, b):
    print(a + b)


def fun(*args, **kwargs):
    print(*args)
    print(kwargs)


my_kwargs = {"a": 1, "b": 2}

fun(1, 2, 3, **my_kwargs, c=1)
