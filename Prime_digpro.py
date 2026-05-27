n = int(input("Enter number: "))

product = 1

while n > 0:
    digit = n % 10

    if digit in [2, 3, 5, 7]:
        product *= digit

    n //= 10

print("Prime Digit Product =", product)
