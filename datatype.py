#datatypes = Type of data that can be stored in a variable. 
#To specify the type of data that can be stored in a variable.

#Two types of Data types:
#1. Single value Data Type 
#in this we have two types of data types:
#1.1 Numeric Data Type:
#- Integer
#- Float
#- Complex
#1.2 Boolean (bool)

#2. Collection Data Type
#in this we have five types of data types:
#list
#tuple
#set
#dictonary(dict)

#Int(Data type)
#Real numbers without decimal points.
#from -infinity to +infinity.

#Default value of int is 0.
#non default value of int is any whole number.
#To check wheter the value is default or non default value we use:
#Bool (variable/value)
#Here Default value = False
#Non default value = True

a = 10
bool(a) 
print(bool(a)) #check whether the value of a is default or non default value.
print(type(a)) #check datatype of variable a

#Float(Data type)
#Real numbers with decimal points.
#from -infinity to +infinity.

#Default value of float is 0.0.
#Non default value of float is any real number with decimal points.
b = 10.5
print(bool(b)) #check whether the value of b is default or non default value.
print(type(b)) #check datatype of variable b

#Complex(Data type)
#Complex numbers are numbers or combination of a real number and an imaginary number.
#Default value of complex is 0j.
#Non default value of complex is any real number with imaginary number.
# a+bj here a is real number and b is imaginary part and j is imaginary part where j = sqrt(-1)
c = -4j + 3 
print(c)
#in this compiler will switch the real part and imaginary part and will print the output in the form of a+bj where a is real part and b is imaginary part.
#we cant use any other alphabet other than j for imaginary part in complex numbers because it is fixed in python.

#Boolean (Data Type) 
#Boolean is a data type that can have only two values: True or False.
#Default value of bool is False.
#we use boolean to check conditions.

#String (Data type)
#String is a collection of characters enclosed in single quotes(' '), double quotes(" ") or  single triple quotes(''' ''').
#we use double quotes when we have to use apostrophes in our string.
#example of string:
s1 = 'Shaurya'
s2 = "Shaurya's PC"
#we use single triple quotes when we have to use for multi line string.
s3 = '''Hello
Shaurya's PC'''
print(s1)
print(s2)   
print(s3)
#default value of string is empty string.

#string length function
print(len(s1)) #to check the length of string s1

#string split function
print(s1.split('s1')) 

#count function used to count the character occurrence in a string.
s = 'Shaurya'
print(s.count('a')) #to count the occurrence of character 'a' in string s

#UpperCase function used to convert the string into uppercase.
b = 'shaurya'
print(b.upper()) #to convert the string b into uppercase.

#Capitalize function used to convert the first character of the string into uppercase and rest of the characters into lowercase.
print(b.capitalize()) #to convert the first character of the string b into uppercase and rest of the characters into lowercase.

#LowerCase function used to convert the string into lowercase.
s = 'SHAURYA'
print(s.lower()) #to convert the string s into lowercase.

#String indexing
#String indexing is used to access the individual characters of a string.
s9 = 'Hello Everyoneeeeeeeee'
print(s9[0]) #to access the first character of the string s9
print(s9[-1]) #to access the last character of the string s9
#positive indexing starts from 0 and negative indexing starts from -1. If we want to access the last character of the string we can use negative indexing.
#string is immutable which means we cannot change the characters of a string once it is created. We can only create a new string with the desired changes.


#Mutuable Data Types
#Mutable data types are data types that can be changed after they are created.
#List, Set and Dictionary are mutable data types in Python.


#List (Data type)
#List is a collection of items which is ordered and changeable. It allows duplicate members.
#List is defined by enclosing the items in square brackets [].
#Example of list:   
l1 = [1, 2, 3, 4, 5] #Homogeneous list (list with same data type)
l2 = ['Shaurya', 'PC', 10, 10.5, True] #Heterogeneous list (list with different data types)
l3 = [1, 2, 3, 4, 5, 'Shaurya', 'PC', 10, 10.5, True, [45, "shaurya"]] #Mixed list (list with both homogeneous and heterogeneous data types and also with nested list)
print(l1)
print(l2)
print(l3)
#Default value of list is empty list [].

#Memory allocation of list
#List is a mutable data type which means it can be changed after it is created. When we create a list, it is stored in a specific memory location. When we change the list, it is stored in the same memory location. This is because of the mutable nature of the list.
l4 = [1, 2, 3, 4, 5]
print(l4)
print(id(l4)) #to check the memory location of list l4
l4.append(6) #to change the list l4 by adding an element 6
print(l4)
print(id(l4)) #to check the memory location of list l4 after changing it.
l4.remove(2) #to change the list l4 by removing an element 2
print(l4)
print(id(l4)) #to check the memory location of list l4 after removing an element 2  
#inbuilt functions of list:
#append function used to add an element at last index in a list.
#insert function used to add an element at a specific index in a list.
#remove function used to remove an element from a list.
#pop function used to remove an element from a list at a specific index and also returns the removed element.



#Tuple (Data type)
#Tuple is a collection of items which is ordered and unchangeable. It allows duplicate members.
#Tuple is defined by enclosing the items in parentheses (). 
#Syntax of tuple: tuple_name = (item1, item2, item3, ...)
#Homogeneous tuple (tuple with same data type)
#Hetrogeneous tuple (tuple with different data types)
#Mixed tuple (tuple with both homogeneous and heterogeneous data types and also with nested tuple)
#Most secure data type because it is immutable which means we cannot change the characters of a tuple once it is created. We can only create a new tuple with the desired changes.
a = (1, 2, 3, 4, 5) #Homogeneous tuple
b = ('Shaurya', 'PC', 10, 10.5, True) #Heterogeneous tuple
c = (1, 2, 3, 4, 5, 'Shaurya', 'PC', 10, 10.5, True, [45, "shaurya"]) #Mixed tuple
c[-1][0] = 50 #to change the first element of the nested list in tuple c to 50
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
#Default value of tuple is empty tuple ().
#Tuple is supportive indexing and slicing just like list. We can access the individual characters of a tuple using indexing and slicing. We can also use negative indexing to access the characters from the end of the tuple.
print(a[0]) #to access the first character of the tuple a
print(a[-1]) #to access the last character of the tuple a
#Tuple is immutable but list is mutable. We can change the list but we cannot change the tuple. If we want to modify the tuple, we can convert the tuple into a list, modify the list and then convert it back to a tuple.
a = 10,20,30
print(a)
#by this we can also create tuple without using parentheses. This is called tuple packing. We can also unpack the tuple into individual variables.


#Set (Data type)
#Set is a collection of items which is unordered and unchangeable(or collection of homogeneous and heterogeneous values). It does not allow duplicate members.
#Set is defined by enclosing the items in curly braces {}.
#Example of set:
set1 = {"Shaurya", "Github", "Instagram"}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3, 4, 5, "Shaurya", "Github", "Instagram", (45, "shaurya")} #Mixed set
print(set1)
print(set2)
print(set3)
#Default value of set is empty set set().
#set only allow immutable value
#Set not allow duplicate members. If we try to add duplicate members in a set, it will automatically remove the duplicate members and will only keep one member.
set4 = {1, 2, 3, 4, 5, 1, 2, 3} #Set with duplicate members
print(set4) #Output will be {1, 2, 3, 4, 5} because set will automatically remove the duplicate members and will only keep one member.
#Set not support indexing coz it is unordered collection of items. We cannot access the individual characters of a set using indexing. We can only access the individual characters of a set using loops or by converting the set into a list or tuple.
#order of input is not same as order of output so set is unordered.
#add function used to add an element in a set.
set4.add(6) #to add an element 6 in set4
print(set4)
#remove function used to remove an element from a set.
set4.remove(2) #to remove an element 2 from set4
print(set4)
#pop function used to remove random element from a set.
set4.pop() #to remove random element from set4
print(set4)

#Dictionary (Data type)
#Dictionary is a collection of items which is ordered and changeable. It does not allow duplicate members. It is defined by enclosing the items in curly braces {} and each item is a key-value pair.
#Syntax of dictionary: dict_name = {key1: value1, key2: value2, key3: value3, ...}
#Example of dictionary: 
dict1 = {"name": "Shaurya", "age": 20, "city": "Delhi"} #Homogeneous dictionary (dictionary with same data type)
dict2 = {"name": "Shaurya", "age": 20, "city": "Delhi", "hobbies": ["coding", "gaming"], "is_student": True} #Heterogeneous dictionary (dictionary with different data types)
print(dict1)    
#keys of a dictionary are unique and values of a dictionary can be duplicate. We can access the values of a dictionary using keys. We can also use the get() function to access the values of a dictionary using keys.
print(dict1["name"]) #to access the value of key "name" in dictionary dict1
print(dict1.get("age")) #to access the value of key "age" in dictionary dict1 using get() function
#Default value of dictionary is empty dictionary {}.
#keys should be immutable data type which means we can use int, float, string, tuple as keys in a dictionary but we cannot use list, set, dictionary as keys in a dictionary because they are mutable data types. Values of a dictionary can be of any data type. We can also use list, set, dictionary as values in a dictionary because they are mutable data types.
#dictionary does not support indexing coz it is unordered collection of items. We cannot access the individual characters of a dictionary using indexing. We can only access the individual characters of a dictionary using keys or by converting the dictionary into a list or tuple.
dict4 = {"Shaurya": 20, "Raj": 25, "Vashu": 21}
print(dict4)
#default value of dictionary is empty dictionary {}.
#Inbuilt functions of dictionary:
#keys() function used to get the keys of a dictionary.
print(dict4.keys()) #to get the keys of dictionary dict4
#values() function used to get the values of a dictionary.
print(dict4.values()) #to get the values of dictionary dict4
#items() function used to get the key-value pairs of a dictionary.
print(dict4.items()) #to get the key-value pairs of dictionary dict4
#get() function used to get the value of a key in a dictionary.
print(dict4.get("Shaurya")) #to get the value of key "Shaurya" in dictionary dict4 using get() function
#update() function used to update the value of a key in a dictionary.
dict4.update({"Shaurya": 21}) #to update the value of key "Shaurya" in dictionary dict4 to 21
print(dict4)

#Mutuable vs Immutable Data Types
#Mutable data types are data types that can be changed after they are created. List, Set and Dictionary are mutable data types in Python.
#Immutable data types are data types that cannot be changed after they are created. Int, Float, Complex, Boolean, String and Tuple are immutable data types in Python.

