# Complex
# 1) magic method (+, -, /, *)
# 2) return Complex ->
# complex2 = Complex(2, 5)
# complex3 = complex1 + complex2
# 3) __str__

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        new_complex = Complex(real, imag)
        return new_complex

    def add(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        new_complex = Complex(real, imag)
        return new_complex

    def __str__(self):
        return f"str called"

    def __repr__(self):
        return f"repr called"


c1 = Complex(1, 2)
c2 = Complex(1, 4)
c3 = c1 + c2
arr = [c1, c2, c3]
print(arr)
print(c3)
