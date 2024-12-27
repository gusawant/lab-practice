num = input("Enter the number: ")
s = 0
n = int(num)

while n > 0:
    r = n % 10
    s += r ** len(num)
    n //= 10

if int(num) == s:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
