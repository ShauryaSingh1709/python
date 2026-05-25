#WAP to reverse half of the string without using slicing and half of the string same.
#I/P : "Aditya" O/P : "idAtya"
s = input("Enter a string: ")
len = len(s)
shau = len//2
rev = ""
for i in range(shau):
    rev = rev + s[shau - i - 1] + s[shau + i]
print("Reversed half of the string is: ", rev)
