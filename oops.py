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



# class Shaurya:
    #Here we will define the properties and functionality of the class.
    
#Object :-
#Object is copy or instance of a class.
#Syntax of object :-
#objectname = classname()
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
