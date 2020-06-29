#Recursion - a function calling itself.
def fact(n):
    if(n==0):
        return 1
    return n * fact(n-1)

result = int(input('Enter an integer: '))
result = fact(result)
print(result)
