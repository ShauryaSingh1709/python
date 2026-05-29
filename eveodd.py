#Even/Odd Factor Sum
n = int(input("Enter number: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if n % i == 0:

        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

print("Even Factor Sum =", even_sum)
print("Odd Factor Sum =", odd_sum)
