class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_total_cost(self, quantity):
        return self.price * quantity

apple = Product(name='Apple', price=2.50, quantity=5)

print("Product Name:", apple.name)
print("Price per unit:", apple.price)
print("Quantity:", apple.quantity)
print("Total Price:", apple.calculate_total_price())

desired_quantity = 10
total_cost = apple.calculate_total_cost(desired_quantity)
print(f"Total Cost for {desired_quantity} units:", total_cost)

