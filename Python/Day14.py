#01-GENERATORS

def number_generator(start, end):
    for num in range(start, end + 1):
        yield num

my_generator = number_generator(1, 5)
print(my_generator)

def abc():
    pass
print(abc)

def abc():
    return 'this is a string'

ghi = abc()
print(type(ghi))

print(next(my_generator))
print(next(my_generator))


def number_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

my_generator = number_generator(1, 5)
for num in my_generator:
    print(num)

#Recrussive-Funcition

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)   # Recrussive case: n! = n * (n-1) !
    
print(factorial(5))
print(factorial(15000))
