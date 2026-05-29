m = int(input("Enter start: "))
n = int(input("Enter end: "))

product = 1

for num in range(m, n + 1):
    if is_prime(num):
        product *= num

print("Prime Product =", product)
