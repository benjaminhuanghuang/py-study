# Apply function to every item of iterable and return a list of the results.

# c[i] = x + y or x+10
c = map(lambda x, y: x + y if y else x + 10, [1, 2, 3, 4, 5], (1, 2, 3, 4))
print c
# [2, 4, 6, 8, 15]


my_list = [1, 2, 3, 4]
result = map(lambda x: str(x), my_list)
print result
# ['1', '2', '3', '4']
