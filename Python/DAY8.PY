#Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark (self):
        print(f"{self.name} is barking!")

my_dog = Dog('Tommy', 6)
print(type(my_dog))

print(dir(my_dog))

class Snake:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight

    def hiss (self):
        print(f"{self.length} is hissing!")

my_snake = Snake('20m', 23)
print(type(my_snake))

print(dir(my_snake))
print("\n")
print(my_snake.length)

class Person:
    count = 0 # Class attributes

    def __init__(self,name):
        self. name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls): #Defining Class method
        return cls.count
    
    @staticmethod
    def get_full_name(firstname, secondname):
        return f'{firstname} {secondname}'
    
print(Person.get_count())

person1 = Person("Alice")
print(Person.get_count())

person2 = Person("Bob")
print(Person.get_count())

print(Person.get_full_name('Chandler', 'Bling'))

person1.get_full_name('Chandler', 'Bing')








      



    



    