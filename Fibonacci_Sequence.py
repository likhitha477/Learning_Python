def fib(n):
    a = 0
    b = 1
    if n < 0:
        print('Enter a positive integer')
    elif n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        print(c)

fib(100)
