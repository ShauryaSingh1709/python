#Unpacking:- It is phenomenon of breaking a collection into individual values in a sequence.
#Here, no. of variables should be equal to the length of the collection.
#syntax:- def func_name(var1, var2, var3, ...):
#         Statement block
#func_name(*col)

#Prog for unpacking:-

def unpack(v1, v2, v3, v4):
    print(v1, v2, v3, v4)
#unpack(*'abcd') #-- for str
#unpack(*[1,2,3,4]) #-- for list
#unpack(*(1,2,3,4)) #-- for tuple
#unpack(*{1,2,3,4}) #-- for set
#unpack(*{'a':1, 'b':2, 'c':3, 'd':4}) #-- for dict
#unpack(*{'a':1, 'b':2, 'c':3, 'd':4}.values())
#unpack(*{'a':1, 'b':2, 'c':3, 'd':4}.items())
unpack(*range(1,5))