#WAP for following output with input.
# I/P :- {"pro.html", "Google.com", "pro1.txt"}
#O/P :- {'html':'pro', 'com':'Google', 'txt':'pro1'}

s = {"pro.html", "Google.com", "pro1.txt"}
d = {}
for i in s:
    x = i.split(".")
    d[x[1]] = x[0]
print(d)