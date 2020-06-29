from functools import reduce
#lambda is an annoymous function used for one line expressions.
seq = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda n: n%2 == 0, seq))
print(evens)
doubles = list(map(lambda n: n*2, evens))
print(doubles)
sum = reduce(lambda a,b: a+b, doubles)
print(sum)
