import copy
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

l = [10,9.56,'Hello',[7j,True,3]]
p = l

p[1] = 9+7j

print("Value of l: ", l)
print("Value of p: ", p)

#Modification done to with respect to the source variable or destination variable will affect the other variable as well because both variables are pointing to the same memory address.(only in case of multiple values)


#Shallow copy will copy the main memory space of the source variable into the destination variable.
#syntax: Destination variable = source variable.copy()

sh = [10,9.56,'Hello',[7j,True,3]]
ur = sh.copy()
print(id(sh))
print(id(ur))
#Here both have different memory addresses.
ur[1] = 9+7j
print("Value of sh: ", sh)
print("Value of ur: ", ur)
#Now modification done only in ur not in sh because both have different memory addresses.

ab = [10,9.56,'Hello',[7j,True,3]]
cd = ab.copy()
cd[3][1] = False
print("Value of ab: ", ab)
print("Value of cd: ", cd)
#Here modification done in cd is also reflected in ab because both have same memory address for the nested list.
#Modification done with the respect to the main memory layer of source variable or destination variable will not affect each other. But modification done with respect to Nested collection will affect both of them.

#Deep copy will copy the entire value space of the one variable to another.
#syntax: import copy
#destination variable = copy.deepcopy(source_variable)

abc = [10,9.56,'Hello',[7j,True,3]]
cde = copy.deepcopy(abc)
print(id(abc))
print(id(cde))
#Here both have different memory addresses.
#Modification done will not affect any of the variable because both have different memory addresses for the main memory layer and nested collection as well.
cde[3][1] = False
print("Value of abc: ", abc)
print("Value of cde: ", cde)
