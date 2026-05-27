n = int(input("Enter number: "))

product = 1

for i in range(1, n + 1):
    if n % i == 0:
        product *= i

print("Factor Product =", product)
