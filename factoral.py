#WAP to find the factorial of a number.
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = int(input("Enter a non-negative integer: "))
print(factorial(n))  


#OR DIFFERENT METHOD
#WITH FOR LOOP
num = int(input("Enter a non-negative integer: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

#WITH WHILE LOOP 
num = int(input("Enter a non-negative integer: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial of", num, "is", factorial)