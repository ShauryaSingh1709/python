#Operator is a symbol that performs a specific task.
#Operands are the values on which the operator performs the task.
#Types of operators:
#1. Arithmetic operators
#2. Comparison operators
#3. Logical operators
#4. Assignment operators
#5. Bitwise operators
#6. Relational operators
#7. Identity operators
#8. Membership operators

#Arithmetic Operators are:- 
#1. Addition (+)
#2. Subtraction (-)
#3. Multiplication (*)
#4. Division (/)
#5. Modulus (%)
#6. Floor Division (//)
#7. Exponentiation (**)

#Syntax for arithmetic operators:
#For addition: a + b
#For subtraction: a - b
#For multiplication: a * b
#For division: a / b
#For modulus: a % b
#For floor division: a // b
#For exponentiation: a ** b

#Addition operation :- 
#In single value it will add the two values and give the result.
#In multiple values it will concatenate the values and give the result.
aaa = 10 
bbb = 20
print("Addition of aaa and bbb: ", aaa + bbb)   
ccc = "Hello "
ddd = "World"
print("Addition of ccc and ddd: ", ccc + ddd)

#In case of single value it did add them and in term of multiple values it concatenated them.
aa = 10+7j
bb = 9.56j
print("Addition of aa and bb: ", aa + bb)
#In case of complex number it will add the real part and imaginary part separately and give the result.

aaaaa = True + True 
print("Addition of aaaaa: ", aaaaa)
#In case of boolean value it will consider True as 1 and False as 0 and add them and give the result.

#In case of list it will concatenate the two lists and give the result.
l1 = [10,9.56,'Hello']
l2 = [7j,True,3]
print("Addition of l1 and l2: ", l1 + l2)

#In case of dictionary it will concatenate the two dictionaries it will not add them and give error.

#In case of tuple it will concatenate the two tuples and give the result.
t1 = (10,9.56,'Hello')
t2 = (7j,True,3)
print("Addition of t1 and t2: ", t1 + t2)

#subtraction operation :-
#In single value it will subtract the two values and give the result.
#In multiple values it will give error because it cannot subtract the values.
# aaa = 10 
# bbb = 20    
# print("Subtraction of aaa and bbb: ", aaa - bbb)
# ccc = "Hello "
# ddd = "World"
# print("Subtraction of ccc and ddd: ", ccc - ddd)

#For complex number it will subtract the real part and imaginary part separately and give the result.
aa = 10+7j
bb = 9.56j  
print("Subtraction of aa and bb: ", aa - bb)

#In case of boolean value it will consider True as 1 and False as 0 and subtract them and give the result.
aaaaa = True - True 
print("Subtraction of aaaaa: ", aaaaa)

#In case of list it will give error because it cannot subtract the values.

#In case of dictionary it will give error because it cannot subtract the values.

#In case of tuple it will give error because it cannot subtract the values.

#In case of set it will work as a difference operator and give the result.
s1 = {10,9.56,'Hello'}
s2 = {7j,True,3}
print("Subtraction of s1 and s2: ", s1 - s2)

#Multiplication operation :-
#In single value it will multiply the two values and give the result.
#In multiple values it will repeat the values and give the result.

#For complex number it will multiply the real part and imaginary part separately and give the result.
aa = 10+7j
bb = 9.56j  
print("Multiplication of aa and bb: ", aa * bb)

#In case of list it will repeat the list and give the result.

#In case of tuple it will repeat the tuple and give the result.

#In case of set it will give error because it cannot multiply the values.

#In case of dictionary it will give error because it cannot multiply the values.

#In case of boolean value it will consider True as 1 and False as 0 and multiply them and give the result.
aaaaa = True * True 
print("Multiplication of aaaaa: ", aaaaa)


#In case of string it will repeat the string and give the result.
s = "Hello "    
print("Multiplication of s: ", s * 3)


#Division operation :-
#Types of division operators:-
#1. Division (/)
#2. Floor Division (//)
#3. Modulus (%)

#Only applicable for single value data types.

#Divison (/) will repeat exact divsion value with floating numbers.

#Floor Division (//) will repeat the division value without floating numbers.

#Modulus (%) will give the remainder of the division value.

#Power (**) will give the result of the first value raised to the power of the second value.
print("Power of 2 and 3: ", 2 ** 3)

#In case of complex number power operation will give the result of the first value raised to the power of the second value.
aa = 10+7j
print("Power of aa and aa: ", aa ** aa)


#Logical operators are:-
#1. And (and)
#2. Or (or)
#3. Not (not)

#And (and) operator will check if operand is holding the default value it will return False and in non default value it will return True.
#It work like multiplication Operator

# 0 and 0 will give 0
# 0 and 1 will give 0   
# 1 and 0 will give 0
# 1 and 1 will give 1

#if operand1 is false then it will return operand1 value and if operand1 is true then it will return operand2 value.
# It will search for default value in both operand and if it find it then it will return False otherwise it will return True.

#Logical OR (or) operator will find any non default value in both operand and if it find it then it will return True otherwise it will return last operand value.
# 0 or 0 will give 0
# 0 or 1 will give 1
# 1 or 0 will give 1
# 1 or 1 will give 1

#it start checking from left to right .


#Logical NOT (not) operator will return the opposite of the operand value.
#syntax: not operand


#Relational operators are:-
#1. Equal to (==)
#2. Not equal to (!=)
#3. Greater than (>)
#4. Less than (<)
#5. Greater than or equal to (>=)
#6. Less than or equal to (<=)

#Equal to operator (==) will check if the values of both operands are equal or not and return True or False accordingly.
#It will compare single value for single value data types
#It will compare both datatype and value for multiple value data types.

#Not equal to operator (!=) will check if the values of both operands are not equal or not and return True or False accordingly.


#Greater than operator (>) will check if the value of left operand is greater than the value of right operand and return True or False accordingly.
#In case of multiple value data types it will compare the first value of both operand and if it is equal then it will compare the second value and so on.

#Less than operator (<) will check if the value of left operand is less than the value of right operand and return True or False accordingly.
#In case of multiple value data types it will compare the first value of both operand and if it is equal then it will compare the second value and so on.

#Greater than or equal to operator (>=) will check if the value of left operand is greater than or equal to the value of right operand and return True or False accordingly.
#In case of multiple value data types it will compare the first value of both operand and if


