def pack(*a,**b):
    print(type(a))
    print(a)
    print(type(b))
    print(b)
pack(12,13,a=1,b=2)
pack(10,20,30)
pack(a=1,b=2,c=3)
pack()