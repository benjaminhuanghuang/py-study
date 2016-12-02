# Apply function of two arguments cumulatively to the items of iterable

def myadd(x, y):
   return x + y


sum = reduce(myadd, (1, 2, 3, 4, 5, 6, 7))
print sum

sum = reduce(lambda x, y: x + y, (1, 2, 3, 4, 5, 6, 7))
print sum
