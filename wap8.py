#WAP to find spy number
#Spy number is a number where the sum of its digits is equal to the product of its digits.
#example: 123 is a spy number because 1+2+3=6 and 1*2*3=6
num = int(input("Number do: "))
sum = 0
product = 1
for i in str(num):
    sum += int(i)
    product *= int(i)
if sum == product:
    print(num, "is a spy number")
else:
    print(num, "is not a spy number")