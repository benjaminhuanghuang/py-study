# Merge some list items in a Python List

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
items[3:6] = [reduce(lambda x, y: x + y, items[3:6])]
print items


items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
items[3:6] = [''.join(items[3:6])]
print items