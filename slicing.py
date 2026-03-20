#Slicing is to extract a position of the element from the list , tuple or string
#in slicing we can only use list , tuple , string 
#syntax for slicing
#variable_name[starting index:ending index:update index]
#Rules for slicing
#1. If we are traversing from left to right ending index +1
#2. If we are traversing from right to left starting index -1
s = "HarryPotter"
print(s[0:5:1]) #Harry (0 to 4 index 5 written coz of rule 1 and why we used 1 bcoz we are going one step at a time)
print(s[5:11:1]) #Potter (5 to 11 index 11 written coz of rule 1 and why we used 1 bcoz we are going one step at a time)
print(s[-6:0:1]) #output will be blank coz of rule 2 we are traversing from right to left and we have to write starting index -1 but we have written 0 so it will not print anything
#3. If the ending index is end or the collection then you can skip it example syntax will be variable_name[starting index::update index]
print(s[-6::1]) #Output :- Potter (0 to end index and we are going one step at a time)
print(s[-6::]) #Output :-  Potter (0 to end index and we are going one step at a time)
#4. If the starting index is zero then you can skip it example syntax will be variable_name[:ending index:update index]
print(s[:5:1]) #Output :- Harry 
print(s[:5:]) #Output :- Harry 
print(s[4::-1]) #Output :- yrraH (4 to 0 index and we are going one step at a time)
print(s[::-1]) #Output :- rettePyrraH (end to start index and we are going one step at a time)
#if i want to print Hryotr then i will write
print(s[0:11:2]) #Output :- Hryote (0 to 10 index and we are going two steps at a time)
print(s[::2]) #Output :- Hryote (0 to end index and we are going two steps at a time)