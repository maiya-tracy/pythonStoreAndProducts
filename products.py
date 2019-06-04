class Product:
	def __init__(self, name, price, category):
		self.name = name
		self.price = price
		self.category = category
	def update_price(self, percent_change, is_increased):
		if is_increased == True:
			self.price*=(1 + percent_change/100)
		elif is_increased == False:
			self.price*=(1 - percent_change/100)
		return self
	def print_info(self):
		print("Name: " + self.name + " Price: " + str(self.price) + " Category: " + self.category)
		return self