# Sort

items = [
    {"id": 6, "name": "No6"},
    {"id": 3, "name": "No3"},

    {"id": 1, "name": "No1"},
    {"id": 2, "name": "No2"},
]

items.sort(key=lambda l: (l["id"]))

print items
