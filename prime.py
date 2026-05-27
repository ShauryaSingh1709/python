m = int(input("Enter start: "))
n = int(input("Enter end: "))

total = 0

for num in range(m, n + 1):
    if is_prime(num):
        total += num

print("Prime Sum =", total)
