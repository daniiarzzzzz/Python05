def krasivyi_resultat(func):
    def inner(a, b):
        result = func(a, b)
        return f"Sum is {result}"

    return inner


@krasivyi_resultat
def sum(a, b):
    return a + b


print(sum(2, 2))
