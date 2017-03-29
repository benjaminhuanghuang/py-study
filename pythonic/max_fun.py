matrix = [[0, 0, 0, 1], [1, 1, 0, 1], [1, 2, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]
# print matrix
#
# for a in matrix:
#     print a
#
#
print "Wrong max:"
print max(matrix)  # wrong!

it = matrix.__iter__()

for item in it:
    print item
