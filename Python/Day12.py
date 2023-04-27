#Arithmetic Function

#Math-Module

import math

print(math.pow(2, 3))
print(math.sqrt(49))
print(math.ceil(4.1))
print(math.floor(-4.9))
print(math.trunc(-4.9))
print(math.fabs(-4.9))


print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
print(math.tan(math.pi/2))
print(math.radians(180))
print(math.degrees(math.pi/2))
print(math.hypot(3, 4))


print(math.factorial(5))
print(math.comb(5, 2))
print(math.isclose(0.1 + 0.2, 0.3))
print(math.isqrt(16))
p = (1, 2, 3)
q = (4, 5, 6)
print(math.dist(p, q))
print(math.erf(0.5))
print(math.gamma(5))
print(math.perm(5, 3))


#Exception-Handling

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ValueError:
    print('Invalid data type! Required: int or float type!')
except ZeroDivisionError:
    print("Cannot divide by 0")


num_str = "abc"
try:
    num = int(num_str)
    print(num)
except (ValueError, TypeError):
    print("Could not convert input to integer.")


num_str = "abc"
try:
    num = int(num_str)
    print(num)
except Exception:
    print("An exception occured.")


num_str = "abc"
try:
    num = int(num_str)
    print(num)
except Exception as e :
    print(e)


try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is", result)


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("The result is", z)
finally:
    print("This block is always executed.")


raise ExceptionType("Exception Message")
x=10
if x>5:
    raise ValueError("x should not be greater than 5")


class MyException(Exception):
    def __init__(self, arg1, arg2):
        self.arg1=arg1
        self.arg2=arg2
        
        










    

    
    






