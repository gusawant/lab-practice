class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Read N complex numbers and compute their sum
N = int(input("Enter the number of complex numbers: "))
total = Complex(0, 0)

for i in range(N):
    r, i = map(float, input(f"Enter real and imaginary part of complex number {i + 1}: ").split())
    total += Complex(r, i)

print("Sum of complex numbers:", total)
