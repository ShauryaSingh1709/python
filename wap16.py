#WAP to print all keys present inside a dict using double packing.
def shaurya(**b):
    for i in b:
        print(i)
shaurya(Shaurya = 20, Raj = 50, Vashu = 21)


#-------------------------Values------------------

def shaurya(**b):
    for i in b.values():
        print(i)
shaurya(Shaurya = 20, Raj = 50, Vashu = 21)