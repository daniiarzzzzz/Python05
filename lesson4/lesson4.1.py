def decorate(func):
    def inner_func(a, b):
        result = func(a, b)
        return f"Result is lkdjfslkdjfl;skd {result}"

    return inner_func


@decorate
def a_b(a, b):
    return a + b


@decorate
def a_mul_b(a, b):
    return a * b


@decorate
def a_div_b(a, b):
    return a / b


print(a_div_b(2, 2))
print(a_b(2, 2))
print(a_mul_b(2, 2))
