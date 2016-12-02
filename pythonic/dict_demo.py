# For each key , value
d = {
    "1": "No1",
    "2": "No2",
    "9": "No9"
}

for key, value in d.iteritems():
    print key, value

# build dict from two lists
x_list = [1, 2, 3]
y_list = ['a', 'b', 'c']

print dict(zip(x_list, y_list))

# create dict from list, use list as key, and default value 1
d = dict.fromkeys(["a", "b", "c"], 3)
print d
