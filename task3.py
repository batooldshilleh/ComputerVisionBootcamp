class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

apple = Product(name='Apple', price=2.50, quantity=5)


print("Product Name:", apple.name)
print("Price per unit:", apple.price)
print("Quantity:", apple.quantity)
print("Total Price:", apple.calculate_total_price())

