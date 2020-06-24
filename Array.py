from array import *
#creating an array of user's choice.
arr = array('i', [])

n = int(input('Enter the length of the array'))

for i in range(n):
    x = int(input('Enter the next value'))
    arr.append(x)

print(arr)

#To check whether the value or number is in the array.
val = int(input('Enter the value for search'))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1
