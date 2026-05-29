m = int(input("Enter start: "))
n = int(input("Enter end: "))

total = 0


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


for num in range(m, n + 1):
    if is_prime(num):
        total += num

print("Prime Sum =", total)