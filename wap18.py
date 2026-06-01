#Create a class called Mobile :-
#Brand, price using object members.
#Create two different objects.
#Display both objects details seperately.
#Add a class member called category = electronics.
class Mobile:
    category = "electronics"
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Category :-", Mobile.category)
        print("Brand :-", self.brand)
        print("Price :-", self.price)
        
mob1 = Mobile("Samsung", 10000)
mob2 = Mobile("Iphone", 20000)
mob1.display()
mob2.display()



