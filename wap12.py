#WAP to check the given character is Uppercase or Lowercase or Special character or Digit.
ch = input("Enter a character: ")
if ch.isupper():
    print("Character is uppercase")
elif ch.islower():
    print("Character is lowercase")
elif ch.isdigit():
    print("Character is a digit")
else:
    print("Character is a special character")


#-----------------------Second method-----------------------
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Character is uppercase")
elif 'a' <= ch <= 'z':
    print("Character is lowercase")
elif '0' <= ch <= '9':
    print("Character is a digit")
else:
    print("Character is a special character")