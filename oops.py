#OOPs stands for Object Oriented Programming System/Structure.
#Class is a blueprint of an object.
#Object is copy or insstance of a class.

#Advantages of OOPs :-
#1. Avoid repetition of code.
#2. It is easy to maintain and modify the code.
#3. It is easy to reuse the code.
#4. It is easy to test the code.
#5. It is easy to debug the code.
#6. Make code easier to understand and use.
#7. We can organize the code properly.
#8. Solving real world problems.
#9. It is way of programming , where we have to create class and objects.

#Class :- 
# 1. Properties(Represented by variables)
# 2. Functionality(Represented by functions)
#syntax of class :-
#class classname:
#classname should be in capital letter but it's not mandatory.

#Types of class :-
#1. User defined class :- It is a class which is defined or created by the user.
#2. Built in class(Inbuilt class) :- It is a class which is predefined by the python.

#Example of user defined class :-
from pyclbr import Class


class Creation:
    a = 10
    b = 20
demo = Creation()
print(type(demo)) #Output :- <class '__main__.Creation'>
#Here __main__ is representing that class is created by the user or we can say it is a user defined class.
#Memory allocation :- 
#Method area :- It will be created into two parts :-
#1. Main Space :- Creation [0X11] and demo [0X22]
#2. Method Area :- Key and Value pair will be stored in the method area.
#key = a and b #for class Creation
#value = 10 (A1) and 20 (A2) #for class Creation and here A1 and A2 are refrence 
#Key = a and b #for object demo
#Value = A1 and A2 #for object demo

#Whenever we want to access the values from the class or object we have to use a syntax
#For class:- Cname.var
#For object;- obj.var

#Access the values of class and object :-
print(Creation.a) #Output :- 10
print(demo.a) #Output :- 10
print(Creation.b) #Output :- 20
print(demo.b) #Output :- 20

Class Creation:
    a = 10
    b = 20
demo1 = Creation()
demo2 = Creation()
print(Creation.a, Creation.b) #Output :- 10 20
print(demo1.a, demo1.b) #Output :- 10 20
print(demo2.a, demo2.b) #Output :- 10 20
    

# class Shaurya:
    #Here we will define the properties and functionality of the class.
    
#Object :-
#Object is copy or instance of a class.
#Syntax of object :-
#objectname = Classname()
# shau = Shaurya() #Here shau is the object of class Shaurya.

#Example of class and object :-
class Smartphone:
    ram = 8
    rom = 256
    color = "Black"
S1 = Smartphone()
S2 = Smartphone()
print(type(S1)) #Output :- <class '__main__.Smartphone'>
#To access the properties using class
print(Smartphone.color) #Output :- Black
#To access the properties using object
print(S1.color) #Output :- Black

#To modify the properties using class
Smartphone.color = "White"
print(Smartphone.color) #Output :- White
#To modify the properties using object
S1.color = "Red"
print(S1.color) #Output :- Red

#Memory allocation of class and object :-
#Smartphone class will be stored in the memory only once but S1 and S2 will be stored in the memory separately.
#Smartphone will store ram = 8, rom = 256, color = "Black" in the memory and S1 and S2 will store the address of the class in the memory.
#Print all property of Smartphone , S1 and S2 :-
print(Smartphone.ram, Smartphone.rom, Smartphone.color) #Output :- 8 256 White
print(S1.ram, S1.rom, S1.color) #Output :- 8 256 Red
print(S2.ram, S2.rom, S2.color) #Output :- 8 256 White
#If we chnage the property of class then it will change for all the objects but if we change the property of object then it will change only for that object.


#Actual Program for Bank Data :-
class Bank:
    bname = "SBI"
    loc = "Bangalore"
    Manager = "Aditya"
cus1 = Bank()
cus2 = Bank()
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Bangalore Aditya
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Bangalore Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Bangalore Aditya
#Modification of class property :-
Bank.loc = "Chandigarh"
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Chandigarh Aditya
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Chandigarh Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Chandigarh Aditya
#Modification of object property :-
cus1.loc = "Jharkhand"
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Chandigarh Aditya
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Jharkhand Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Chandigarh Aditya

cus2.loc = "Mumbai"
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Chandigarh Aditya  
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Jharkhand Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Mumbai Aditya

#Modification done with respect to class will affect all the objects.
#Reason:- Objects are instance/Copy of the class.


#Modification done with respect to object will not affect the class and other objects.
#Reason:- Class are not depending on the objects.