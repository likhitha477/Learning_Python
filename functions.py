def greet():
    print("Hello, World!")
    print("Good Morning")

greet() #calling the function

def add(a,b):
    c=a+b
    print(c)
add(5,4)

def add(a,b):
    c=a+b
    return c
result = add(5,4)
print(result)

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x ",x)

a = 10
print("id of a", id(a))
update(a)
print("a ",a)

def sum(a, *b):
    print(a)
    print(b)
sum(4,7,8,9)

def summation(*b):
    c = 0
    for i in b:
        c = c+i
    print(c)

summation(4,7,8,9)

def bio(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
bio('Zac', age = 24, city = 'Rio')    
