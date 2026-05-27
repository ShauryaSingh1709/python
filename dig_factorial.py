n = int(input("Enter number: "))

while n > 0:
    digit = n % 10

    print(digit, "=", factorial(digit))

    n //= 10
