#WAP to check wheter the given number is amstrong number or not.
num = int(input("Enter a number: "))
num = str(num)
length = len(num)
sum = 0
for i in num:
    sum = sum + int(i)**length
if sum == int(num):
    print("Number is an amstrong number.")
else:
    print("Not an amstrong number.")
