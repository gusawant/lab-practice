import math

num = int(input("Enter the number: "))

# a) Square root of number
sqrt = math.sqrt(num)
print("Square root of", num, "is", sqrt)

# b) Square of number
sqr = num ** 2
print("Square of", num, "is", sqr)

# c) Cube of number
cube = num ** 3
print("Cube of", num, "is", cube)

# d) Check for prime
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# d) Factorial of number
fact = 1

if num == 0 or num == 1:
    print("Factorial of", num, "is 1")
elif num > 1:
    for i in range(2, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)

# f) Prime factors
factors = []
n = num

for i in range(2, n + 1):
    while n % i == 0:
        factors.append(i)
        n //= i
print("Prime factors of", num, "are", factors)
