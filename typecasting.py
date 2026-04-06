#Typecasting means to convert one data type to another data type. 
'10' == 10 #This will give false because they are of different data types.
#To convert the string '10' to an integer, we can use the int() function.
int('10') == 10 #This will give true because now both are of the same data type.
# for single value data types to multiple value data type only string is supported
# for multiple value data types to single value data type only bool is supported.

#Int to other data types
# Int can be converted to int , float , complex , bool , string and can not into list , tuple , set and dict.

#Float to other data types
# Float can be converted to int , float , complex , bool , string and can not into list , tuple , set and dict.

#Complex to other data types
# Complex can be converted to complex , bool , string and can not into int , float , list , tuple , set and dict.


#Bool to other data types
# Bool can be converted to int , float , complex , bool , string and can not into list , tuple , set and dict.


#String to other data types
# String can be converted into int , float , complex only if it is number in string format otherwise it will give error. 
# String can be converted to bool and string , list , tuple , set but can not into dict.

#List to other data types
# List can be converted to bool , string , list , tuple and set(only if it is immutable value) but can not into int , float , complex.
# List can be converted to dict only if it is list of lists with 2 values in each list otherwise it will give error.

#Tuple to other data types
# Tuple can be converted to bool , string , list , tuple and set(only if it is immutable value) but can not into int , float , complex.
# Tuple can be converted to dict only if it is list of tuples with 2 values in each tuple otherwise it will give error.

#Set to other data types
# Set can be converted to bool , string , list , tuple and set but can not into int , float , complex and dict(only if length of 2).

#Dict to other data types
# Dict can be converted to bool , string , list , tuple and set but can not into int , float , complex. 