#Even/Odd Factor Product
n = int(input("Enter number: "))

even_product = 1
odd_product = 1

for i in range(1, n + 1):
    if n % i == 0:

        if i % 2 == 0:
            even_product *= i
        else:
            odd_product *= i

print("Even Factor Product =", even_product)
print("Odd Factor Product =", odd_product)
