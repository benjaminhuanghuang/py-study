### build dict from two lists
x_list = [1, 2, 3]
y_list = ['a', 'b', 'c']

print zip(x_list, y_list)

print dict(zip(x_list, y_list))

names = ['raymond', 'rachel', 'mathew']
colors = ['red', 'green', 'blue','yellow']

# bad
n = min (len(names), len(colors))
for i in range(n):
    print names[i], "->", colors[i]

# better
for name, color in zip(names, colors):
    print name, "->", color
