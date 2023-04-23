#Lambda Function
#Anonymous Function
#C++:Inlin Function
  
  #def square(x):
  #     return x ** 2
square = lambda x : x ** 2
num = 3
print (square(num))



a = [1, 2, 3, 4]
sum_calc = lambda x: sum(x)
print(sum_calc(a))

#Built-in Functions
# It displays us the result
print()

#it takes input from the user in type
input()

#Calculates the length of a sequence
len()

#Returns data type of an object
type()

#Returns all the attributes and methods of a data type
dir()
a = 12
print (dir(a))

#It returns index and value of items in a sequence
#enumerate()
a = [1, 2, 3, 4]
for i in a :
    print(i)

for i in enumerate(a):
    print(i)

for idx, val in enumerate(a):
    print(f"Index:{idx}, Value: {val}")

zip()
a = [1, 2, 3, 4]
b = ['a', 'b','c','d']

for i in zip(a, b):
    print(i)

for i, j in zip ( a, b )
  print (len(f'First :{i}, Second: {j}, filter()'))


a = [1, 2, 3, 4]
abc = reduce(lambda x , y: x + y, a)
print(abc)

