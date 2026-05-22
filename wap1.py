S = "Python is very Good"
#Output is "nohtyP si yrev dooG" do this without imbuilt functions and slicing.
rev = ""
word = ""
for i in S:
    if i == " ":
        rev = rev + word + " "
        word = ""
    else:
     word = i + word
rev = rev + word
print(rev)