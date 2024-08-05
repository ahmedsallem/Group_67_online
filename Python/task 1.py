class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item_name, price,number_items):
        item = (item_name, price,number_items)
        self.items.append(item)
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
    def total_price(self):
        total = 0
        for item in self.items:
            total += item[1]*item[2]
        return total
    def total_products(self):
        total_p = 0
        for item in self.items:
            total_p += item[2]
        return total_p

cart = ShoppingCart()

cart.add_item("chips", 100,5)
cart.add_item("chiken", 200,8)
cart.add_item("meat", 150,6)
cart.add_item("rice", 120,10)
cart.add_item("water", 80,5)

print("Items in Cart now :")
for item in cart.items:
    print("product :",item[0], "--> price : ", item[1],"--> quantity: ",item[2])
total_p = cart.total_products()
total_cost = cart.total_price()
print("the receipt is : ",cart.items)
print("total products: ",total_p,"    ","Total cost:", total_cost,"$")

cart.remove_item("water")
print("Updated Items :")
for item in cart.items:
    print("product :",item[0], "--> price : ", item[1],"--> quantity: ",item[2])
total_p = cart.total_products()
total_cost = cart.total_price()
print("the receipt is : ",cart.items)
print("total products: ",total_p,"    ","Total cost:", total_cost,"$")