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

class Creation:
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

#States or Property :- 
# The data and information stored inside a class/object is known as states or property of class/object.
#                                             OR
# The variable or functionalities stored inside the class are called as states.

#There are 2 types of states or property :-
#1. Generic state/ class state/ static state.
#2. Specific state/ object state.
#-- These are the properties which will be common for every object.
#1. Generic state :- The Properties which are common for all the object are termed as generic state.
#Example for generic state :-
class School:
    sname = "CGC"
    loc = "Chandigarh"
    principal = "Aditya"
    time = "12:30-4:30"
st1 = School()
st2 = School()
print(School.sname, School.loc, School.principal, School.time) #Output :- CGC Chandigarh Aditya 12:30-4:30
print(st1.sname, st1.loc, st1.principal, st1.time) #Output :- CGC Chandigarh Aditya 12:30-4:30
print(st2.sname, st2.loc, st2.principal, st2.time) #Output :- CGC Chandigarh Aditya 12:30-4:30
#2. Object state or Specific state ;- The properties which will we create outside the class after the class creation is called as specific or object state.
#Example for object state :-
class School:
    sname = "DAV"
    loc = "Bangalore"
    principal = "Joseph Vijay"
    time = "9:00am to 12:00pm"
st1 = School()
st1.name = "Shaurya"
st1.id = 23
st1.age = 20
st1.bg = "AB+"

st2 = School()
st2.name = "Raj"
st2.id = 24
st2.age = 18
st2.bg = "O+"
print(st1.name, st1.id, st1.age, st1.bg, st1.sname, st1.loc, st1.principal, st1.time) #Output :- Shaurya 23 20 AB+ DAV Bangalore Joseph Vijay 9:00am to 12:00pm
print(st2.name, st2.id, st2.age, st2.bg, st2.sname, st2.loc, st2.principal, st2.time) #Output :- Raj 24 18 O+ DAV Bangalore Joseph Vijay 9:00am to 12:00pm


#Difference between method and function :-
#Function which we declare inside the class is called as methods.
#If we declare the function outside the class then it is called as function.

#<--example of Function-->
def add():
    print("Hello")
#add() is a function because it is declared outside the class.

#<--example of method-->
class Demo:
    def show():
        print("Hello")
#show() is a method because it is declared inside the class.

#Constructor or __init__ method or Initialisation :-
#It runs automatically when an object is created.
#It is used to initialize the member of the object.
#No need of calling the method by default it is execute when we create an object.
#self is the mandatory argument to pass for the __init__ method.
#We can pass argument in the object creation only if there is __init__ method present inside the class.
#__init__ is the constructor method in python.
#For __init__ method, passing self is mandatory to store the address of the object.
#Syntax for constructor method :-
#class Cname:
    #Block of code
    #def __init__(self, arg1, arg2, arg3,......argn):
        # self.arg1 = arg1
        # self.arg2 = arg2
        # self.arg3 = arg3
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # self.argn = argn
#Obj_name = Cname(arg1, arg2, arg3,.....argn)

class School:
    sname = "Carmel"
    loc = "Bangalore"
    principal = "Shaurya"
    timing = "9:00am to 12:00pm"
    def __init__(self, name, sid, age, bg):
        self.name = name
        self.sid = sid
        self.age = age
        self.bg = bg
st1 = School("Akanksha", 16, 24, "B+")
st2 = School("Alavya", 17, 20, "AB+")
print(st1.name, st1.sid, st1.age, st1.bg, st1.sname, st1.loc, st1.principal, st1.timing) #Output :- Akanksha 16 24 B+ Carmel Bangalore Shaurya 9:00am to 12:00pm
print(st2.name, st2.sid, st2.age, st2.bg, st2.sname, st2.loc, st2.principal, st2.timing) #Output :- Alavya 17 20 AB+ Carmel Bangalore Shaurya 9:00am to 12:00pm
    