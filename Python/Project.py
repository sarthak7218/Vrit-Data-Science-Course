#Create the Product Class

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
    def __init__(self):
        self.products =[]

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
    
    def generate_invoice(self, user):
        invoice = f"Invoice for{user.name}:\n"
        invoice += "======================\n"
        for product in self.products:
            invoice += f"{product.name}: ${product.price}\n"
        total_cost = self.calculate_total_cost()
        if user.is_premium:
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
        # for product in self.products:
            # yield product


# Create some products
product1 = Product("Shirts", 20)
product2 = Product("Pants", 30)
product3 = Product("Shoes", 50)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_product(product1)
cart.add_product(product2)

# Use the generator to iterate over the products
for product in cart.get_products():
    print(f"Product: {product.name}, Price: {product.price}")


#--------------Non-Premium User----------------

# Create a user
user = User("Rita", is_premium=False)

# Generate and print the invoice
invoice = cart.generate_invoice(user)
print(invoice)

#--------------Premium User------------------

# Create a user
user = User("Sarthak", is_premium=True)

# Generate and Print the invoice
invoice = cart.generate_invoice(user)
print(invoice)







 


        



