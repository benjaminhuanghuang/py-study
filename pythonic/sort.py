import operator

# sort by key
somelist = [(1, 5, 8), (6, 2, 4), (9, 7, 5)]

somelist.sort(key=operator.itemgetter(1))

print somelist
