num = int(input("Enter a number: "))

n = num
last = n % 10
n //= 10
shau = 1
while n >= 10:
    n //= 10
    shau += 1

first = n 
middle = (num % (10 ** shau)) // 10
swapped = last * (10 ** shau) + middle * 10 + first

print("result:", swapped)