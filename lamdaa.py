from functools import reduce
num = [2, 5, 6, 8, 7, 14, 66]
evens = list(filter(lambda a: a % 2 == 0, num))
doubles = list(map(lambda a: a*2, evens))
sum = reduce(lambda a, b: a+b, doubles)
print(evens)
print(doubles)
print("sum", sum)
