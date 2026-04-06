marks = float(input("Enter your marks: "))
if marks > 100 or marks < 0:
    print("Invalid Input")
elif marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 70 and marks <= 89:
    print("Grade B")
elif marks >= 50 and marks <= 69:
    print("Grade c")
else:
    print("Fail")



#Nested if
#Use Nested if to check if a character is a vowel or a consonant using ascii value
character = input("Enter a character: ")
if character >= "a" and character <= "z" or character >= "A" and character <= "Z":
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u" or character == "A" or character == "E" or character == "I" or character == "O" or character == "U":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Special Character")



#Alt way 
character = input("Enter a character: ")
if character in "aeiouAEIOU":
    print("Vowel")
elif character in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    print("Consonant")
else:
    print("Special Character")


