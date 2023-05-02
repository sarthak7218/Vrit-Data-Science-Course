#O2- Property-Decorator

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name...")
        return self._name
    
    @name.setter
    def name(self, value):
        print("Setting name...")
        self._name = value

person = Person("Alice")
print(person.name)
person.name = "Bob"
print(person.name)

#DELETER

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name...")
        return self._name
    
    @name.setter
    def name(self, value):
        print("Setting name...")
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

person = Person("Alice")
print(person.name)
del person.name
print(person.name)


#03-Iterators

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.next = 1

    def __iter__(self):
        return self
    
    def __next__(self):
       if self.current >= self.limit:
           raise StopIteration
       
       result = self.current
       self.current, self.next = self.next, self.current + self.next
       return result
    
fib = Fibonacci(30)

for num in fib:
    print(num)







    



