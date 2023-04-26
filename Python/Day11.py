class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"({self.name} is {self.age} years old)"
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
    def __len__(self):
       return self.age
    
    def __call__(self):
         return f"{self.name} is being called"
   
person = Person("Alice", 30)

print(person)        #prints "Alice is 30years old"
print(str(person))   #also prints "Alice is 30 years old"
print(repr(person))  #prints "Person('Alice', 30)"
print(len(person))   #prints 30
print(person())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"({self.name} is {self.age} years old)"
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
    def __len__(self):
       return self.age
    
    def __call__(self):
         return f"{self.name} is being called"
   
person = Person("Sarthak", 25)

print(person)        #prints "Sarthak is 25years old"
print(str(person))   #also prints "Sarthak is 25 years old"
print(repr(person))  #prints "Person('Sarthak', 25)"
print(len(person))   #prints 25
print(person())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)
    
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y)
    
    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Point(x, y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2)      
print(p2 - p1)      
print(p1 * p2)
print(p2 / p1)
print(p1 == p2)
print(p1 < p2)












