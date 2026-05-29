#WAP to find the string values from a tuple using packing.
tup = ("Shaurya", "PC", 10, 5, True)
for i in tup:
    if type(i) == str:
        print(i)
        
        
        
        
#--------------- Second Method --------------
def shaurya(*args):
    for i in args:
        if type(i) == str:
            print(i)
shaurya("Shaurya", "PC", 10, 5, True)