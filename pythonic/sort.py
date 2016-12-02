import operator

# sort by key
somelist = [(1, 5, 8), (6, 2, 4), (9, 7, 5)]

somelist.sort(key=operator.itemgetter(1))

print somelist



# Sort by lambda
items = [
    {"id": 6, "name": "No6"},
    {"id": 3, "name": "No3"},

    {"id": 1, "name": "No1"},
    {"id": 2, "name": "No2"},
]

items.sort(key=lambda l: (l["id"]))
items.sort(key=lambda l: (l["name"]), reverse=True)
print items

