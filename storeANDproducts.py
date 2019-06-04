from store import Store
from products import Product

def printAllInfo():
	print("Printing All Products")
	for item in Products:
		print("Name: " + item.name + " Price: " + str(item.price) + " Category: " + item.category)

Stores = []
walmart = Store("Walmart")
Stores.append(walmart)
safeway = Store("Safeway")
Stores.append(safeway)

Products = []
milk = Product("Milk", 4.99, "Dairy")
Products.append(milk)
eggs = Product("Eggs", 2.95, "Dairy")
Products.append(eggs)
gfBread = Product("Gluten-Free Bread", 7.50, "Grains")
Products.append(gfBread)

milk.update_price(5, True)
milk.print_info()

gfBread.print_info()

safeway.add_product(gfBread).add_product(eggs).add_product(eggs).add_product(eggs).add_product(eggs)

safeway.sell_product(1)

safeway.inflation(2)

printAllInfo()

safeway.set_clearance("Grains", 5)

printAllInfo()
