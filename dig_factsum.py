n = int(input("Enter number: "))

total = 0

while n > 0:
    digit = n % 10

    total += factorial(digit)

    n //= 10

print("Factorial Sum =", total)
