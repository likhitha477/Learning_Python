from numpy import *
arr1 = array([
[1,2,3,4,6,2],
[5,6,7,8,7,9]
])
print(arr1)
print(arr1.ndim)
print(arr1.shape) #gives you the number of rows and columns.
print(arr1.size) #numbers of elements in the block.

#convert 2D array into 1D
arr2 = arr1.flatten()
print(arr2)

#convert single dimensional array into multidimensional array
arr3 = arr2.reshape(3,4) #converts to 3X4 matrix.
print(arr3)
arr4 = arr2.reshape(2,2,3) #create 3D array which has 2 2-D arrays.
print(arr4)

#matrices
arr5 = array([
[1,2,3,4],
[5,6,7,8]
])
m = matrix(arr5)
print('m: ',m)

m1 = matrix('1 2 3; 4 5 6; 7 8 1')
print(m1)
print(diagonal(m1)) #prints diagonal elements.

#multiplying matrices
m2 = matrix('1 2 3; 4 5 6; 7 8 9')
m3 = m1 * m2
print(m3)
