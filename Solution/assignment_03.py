# Accept input from the user
n = input("Enter a number: ")

# Method 1: Using string slicing function
reversed_n = n[::-1]
print(f"Digits in reverse order using Method 1: {reversed_n}")

# Method 2: Using loops
reversed_num = 0
num = int(n)

while num > 0:
    rem = num % 10
    reversed_num = (reversed_num * 10) + rem
    num //= 10
print(f"Digits in reverse order using Method 2: {reversed_num}")
