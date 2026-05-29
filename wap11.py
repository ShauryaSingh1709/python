#WAP and take two coordinates i.e. x and y and check in which points the data points are present.
x = int(input("X coordinate: "))
y = int(input("Y coordinate: "))
if x >0 and y >0:
    print("First Quad")
elif x <0 and y >0:
    print("Second Quad")
elif x <0 and y <0:
    print("Third Quad")
elif x >0 and y <0:
    print("Fourth Quad")
elif x == 0 and y != 0:
    print("Y axis")
elif x != 0 and y == 0:
    print("X axis")
else:
    print("Origin")