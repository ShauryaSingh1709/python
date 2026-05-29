#DOUBLE PACKING/DICTIONARY PACKING
#It is required for the user to pass the data in the form of key=value then we will get the data in the form of dictionary.
#Syntax of double packing:- 
#func_name(key1=value1, key2=value2, key3=value3, ...)
#HEre keys should follow identifiers rules.

def pack(**b):
    print(type(b))
    print(b)
pack(a=1, b=2, c=3)