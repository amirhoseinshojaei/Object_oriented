class Item:

    def __init__(self,name,price,quantity=1):

        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):

        return self.price * self.quantity

item1 = Item("Phone",100,5)
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price,item1.quantity))

item2 = Item("Laptop",1000,2) 
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

#_____________________________________________

class Store:

    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self,name:str,price:float,quantity:int=1):

        # Run validations to the received arguments

        assert price >= 0,f'{price} is not greater than or equal zero'
        assert quantity >0,f'{quantity} is not greater than zero'

        # Assign to self object

        self.name = name
        self.price = price
        self.quantity = quantity

    
    def calculate_total_price(self):

        return self.price * self.quantity
    
    def apply_discount(self):

        self.price = self.price * self.pay_rate
    

item3 = Store('Phone',1000)
item3.apply_discount()
item3.calculate_total_price()
print(item3.apply_discount())
print(item3.price)
print(f'{item3.name},{item3.price},{item3.quantity}')

print(item3.calculate_total_price())

print(Store.__dict__) # All the attributes for Class level
print(item3.__dict__) # All the attributes for instance level


item4 = Store('Tv',2000)
item4.pay_rate = 0.7
item4.apply_discount()
print(item4.price)