def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return num1 / num2

print("Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = None

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    try:
        result = divide(num1, num2)
    except ValueError as e:
        print(e)
        exit()
else:
    print("Error: Invalid choice!")

print("Result: ", result)


import sklearn
print("scikit-learn version:", sklearn.__version__)
