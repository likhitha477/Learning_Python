#Distinguish names that are 8 or more characters from less than 8 characters.

def count(lst):
    a = 0
    b = 0
    for i in range(len(lst)):
        if len(lst[i])<8:
            a+=1
        else:
            b+=1
    return a,b

lst = []
x = int(input('Enter the number of names you want to enter: '))
for k in range(x):
    lst.append((input()))
print('list: ', lst)
less_than_eight, greater_than_equal_to_eight = count(lst)
print("less than eight characters: {} and greater or equal to 8 characters: {}".format(less_than_eight, greater_than_equal_to_eight))
