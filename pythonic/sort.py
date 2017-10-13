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
    {"id": 2, "name": "No3"},
]

items.sort(key=lambda l: (l["id"]))
items.sort(key=lambda l: (l["name"]), reverse=True)
print items

# Sort by multiple file
items.sort(key=lambda i: (i["id"], i["name"]))
print ">> sort by id and name"
print items

colors = ['red', 'green', 'blue', 'yellow']
for color in sorted(colors):
    print color

for color in sorted(colors, reverse=True):
    print color
    
#  Custom sort order
def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
       return 1
    return 0
print sorted(colors, cmp = compare_length)



