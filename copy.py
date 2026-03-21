#Type of copy 
#1. General copy 
#2. Shallow copy
#3. Deep copy

#General copy will copy the memory address of the variable, so if we change the value of the variable, it will change the value of the original variable as well.
#syntax: destination variable = source variable
#if a = 10 and b = a, then if we change the value of a to 20, then the value of a remains same i.e. 10
a = 10
b = a
print("Value of a: ", a)
print("Value of b: ", b)
a = 20
print("Value of a: ", a)
print("Value of b: ", b)