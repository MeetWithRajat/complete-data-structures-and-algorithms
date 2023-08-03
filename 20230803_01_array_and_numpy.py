import array
import numpy as np

arr1 = array.array("i", [1, 2, 3, 4])
print(arr1)
print("\nPrinting arr1")
print(type(arr1))

arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)
print("\nPrinting arr2")
print(type(arr2))

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]])
print("\nPrinting arr3")
print(arr3)

arr4 = np.insert(arr3, 0, [0, 0, 0, 0], axis=1)
print("\nPrinting arr4")
print(arr4)

arr5 = np.insert(arr3, 0, [0, 0, 0, 0], axis=0)
print("\nPrinting arr5")
print(arr5)

arr6 = np.array([[1, 1, 1, 1]])
print("\nPrinting arr6")
print(arr6)

arr7 = np.insert(arr3, 4, arr6, axis=1)  # must have to specify axis, otherwise error
print("\nPrinting arr7")
print(arr7)

arr8 = np.append(arr3, arr6, axis=0)
print("\nPrinting arr8")
print(arr8)

arr9 = np.append(arr3, arr6.T, axis=1)
print("\nPrinting arr9")
print(arr9)