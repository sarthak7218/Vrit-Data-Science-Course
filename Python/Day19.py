import numpy as np

## Creating Numpy Arrays

#np.array()

list1 = [1, 2, 3]
print(type(list))
array1 = np.array(list1)
print(array1)
print(type(array1))
print(array1.ndim)

list2 = [[1, 2], [3, 4]]
array2 = np.array(list2)
print(array2)
print(type(array2))
print(array2.ndim)


print(np.zeros(5))

print(np.zeros(2, 3))

print(np.ones(5))

