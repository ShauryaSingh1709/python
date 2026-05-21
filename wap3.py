#WAP to find the sum of digits of a number.
num = int(input("Enter Number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("Sum of digits is:", sum)