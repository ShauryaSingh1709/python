# a = 10
# print(a)
# def shaurya():
#     a = 20
#     print(a)
# shaurya()
# print(a)
#Here we have output 10,20,10 because the variable a is defined in the global scope and local scope. The local variable a is only accessible within the function shaurya() and does not affect the global variable a.
# a = 10
# print(a)
# def shaurya():
#     global a
#     a = 20
#     print(a)
# shaurya()
# print(a)
#Here we have output 10,20,20 because we have used the global keyword to indicate that we want to use the global variable a inside the function shaurya(). Therefore, when we assign a new value to a inside the function, it modifies the global variable a, which is reflected in the final print statement.

#Global variable is the variable that define inside in the main space and can be accessed from anywhere in the program.

#Local variable is the variable that define inside a function and can be accessed only within that function.
# def outer():
#     a = 10
#     print(a)
#     def inner():
#         a = 50
#         print(a)
#     inner()
#     print(a)
# outer()

#To modify a local variable inside a nested function, we can use the nonlocal keyword.
# def outer():
#     a = 10
#     print(a)
#     def inner():
#         nonlocal a
#         a = 50
#         print(a)
#     inner()
#     print(a)
# outer()
# print(a) #It will give an error in local variable but if we use global instead of nonlocal then we will get output 10,50,50 and 50 because we have used global keyword to indicate that we want to use the global variable a inside the function inner().

#WAP to extract vowels present inside an string and count of vowels.
# def vowels_count(string):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in string:
#         if char in vowels:
#             print(char,end='')
#             count += 1
#     return count
# string = input("Enter a string: ")
# print("Extracted Vowels in the string:", end=' ')
# print("\nNumber of vowels:", vowels_count(string))