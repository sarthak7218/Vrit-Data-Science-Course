
class Example:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a
    
example = Example()
val = example.add(1, 2)
print(val)

class Example:
    def add(self, *args):
        if len(args)==1:
            return args[0]
        elif len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[1] + args[2]
        
example = Example()
val = example.add(1, 2, 3)
print(val)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am an animal.")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow!")

my_cat = Cat("Fluffy", 3, "gray")
print(my_cat.name)
print(my_cat.age)
print(my_cat.color)
my_cat.speak()
my_cat.intro()



