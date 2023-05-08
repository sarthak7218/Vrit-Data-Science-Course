class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, name, is_premium = False):
        self.name = name
        self.is_premium = is_premium

def discount_10_percent(func):
    def wrapper(self):
        total_cost = func(self)
        discounted_cost = total_cost * 0.9
        return discounted_cost
    return wrapper

class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total_cost(self):
        total_cost = sum(product.price for product in self.products)
        return total_cost
    
    @discount_10_percent
    def calculate_discounted_cost(self):
        total_cost = sum(product.price for product in self.products)
        return total_cost
    
    def generate_invoice(self):
        invoice = f"Invoice for {self.user.name}:\n"
        invoice += "======================\n"
        for product in self.products:
            invoice += f"{product.name}: ${product.price}\n"
        total_cost = self.calculate_total_cost()
        if self.user.is_premium:
            invoice += "-----------------------\n"
            invoice += f"Sub-Total: ${total_cost}\n"
            final_cost = self.calculate_discounted_cost()
            invoice += f"Discount(10%): ${total_cost - final_cost}\n"
            total_cost = final_cost
        invoice += "----------------------\n"
        invoice += f"Total: ${total_cost}"
        return invoice
    
    def get_products(self):
        yield from self.products

class User:
    def __init__(self, name, is_premium=False, is_admin=False):
        self.name = name
        self.is_premium = is_premium
        self.is_admin = is_admin

    def make_admin(self):
        if self.is_admin:
            self.is_admin = True
            self.is_premium = True
        else:
            print("Only admin users can make other users admin.")

# Create some products
product1 = Product("Shirts", 20)
product2 = Product("Pants", 30)
product3 = Product("Shoes", 50)

# Create a user
user1 = User("Rita", is_premium=False)

# Create a shopping cart for user1
cart1 = ShoppingCart(user1)

# Add products to the cart
cart1.add_product(product1)
cart1.add_product(product2)

# Use the generator to iterate over the products
for product in cart1.get_products():
    print(f"Product: {product.name}, Price: {product.price}")

# Generate and print the invoice for user1
invoice1 = cart1.generate_invoice()
print(invoice1)

# Create an admin user
admin = User("Admin", is_premium=True, is_admin=True)

# Create a new user
user2 = User("Sarthak", is_premium=False)

# Try to make user2 an admin (this should fail)
user2.make_admin()

# Make the admin user an admin
admin.make_admin()

# Try to make user2 an admin again (this should succeed)
user2.make_admin()

# Create a shopping cart for user2
cart2 = ShoppingCart(user2)

# Add products to the cart
cart2.add_product(product2)
cart2.add_product(product3)

# Generate and print the invoice for user2
invoice2 = cart2.generate_invoice()
print(invoice2)

