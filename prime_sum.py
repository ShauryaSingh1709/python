n = int(input("Enter number: "))

total = 0

while n > 0:
    digit = n % 10

    if digit in [2, 3, 5, 7]:
        total += digit

    n //= 10

print("Prime Digit Sum =", total)
