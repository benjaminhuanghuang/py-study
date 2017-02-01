def multipliers():
    return [lambda x: i * x for i in range(4)]


print [m(2) for m in multipliers()]

# [6, 6, 6, 6] (not [0, 2, 4, 6])
