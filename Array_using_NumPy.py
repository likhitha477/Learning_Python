#Python Tutorial for Beginners - Telusko
from numpy import *
arr = array([1,2,3,4,5])
print(arr.dtype) #in array, all the elements are of same type.

#linspace
arr1 = linspace(0,16,10) #16 would be included and 10 is the number of elements printed.
print(arr1)

arr2 = linspace(0,15) #creates 50 elements as default.

#arange
arr3 = arange(1,15,3) #3 is the step size
print(arr3)

#logspace
arr4 = logspace(1,40,5) #the spacing between 1 and 50 depends on log of 5.
print(arr4)
print('%.2f' %arr4[4])

#zeros
arr5 = zeros(5)
print(arr5) #prints float values.

#ones
arr6 = ones(5)
print(arr6)

#copying an array
arr9 = array([2,6,8,1,3])
arr10 = arr9.copy() #deep copy. 2 different arrays with different addresses.
arr9[1] = 7
print(arr9)
print(arr10)

print(id(arr9))
print(id(arr10))

#adding an array
arr = arr + 5
print(arr)

arr7 = array([5,1,2,8,4])
arr8 = arr + arr7
print('arr8',arr8)
print('max of arr8',max(arr8))
