#WAP TO FIND THE LARGEST EVEN NUMBER IN A LIST.
shaurya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
meow = 0
for i in shaurya:
    if i % 2 == 0:
        if i > meow:
            meow = i
print(meow)