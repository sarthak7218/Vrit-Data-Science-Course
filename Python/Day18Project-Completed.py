class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    users = []  #Class variable to store all created users

    def __init__(self, name):
        self.name = self.validate_name(name)
        self.__is_premium = False
        self.__is_admin = False
        self.cart = ShoppingCart()
        User.users.append(self)    #Add the user to the list of users
        if self.name == 'admin':
            self.__is_premium = True
            self.__is__admin = True

    @staticmethod
    def validate_name(name):
        if any(user.name == name for user in User.users):
            print(f"user with the name '{name}' already exists. Please choose a different choose a different name.")
            unique_name = input("Please enter a unique name: ")
            return User.validate_name(unique_name)  # Recursively validate the uniue name.
        return name
    
    @property
    def is_premium(self):
        return self.__is_premium

    @property
    def is_premium(self):
        return self.__is_premium

    def make_admin(self, admin_user):
        if admin_user.is_admin:
            self.__is_admin = True
            self.__is_premium = True

    def  make_premium(self, admin_user):
        if admin_user.is_admin:
            self.__is_premium = True

    def remove_admin(self, admin_user):
        if admin_user.is_admin:
            self.__admin_is_admin = False

    def remove_premium(self, admin_user):
        if admin_user.is_admin:
            self.__is_premium = False

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
    


    
        







    
