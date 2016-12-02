# in Python, "Object references are passed by value".

# When you tried to reassign a variable, and put something different into the function's box
def reassign(l):
    l = [0, 1]


def append(list):
    list.append(1)


list = [0]
reassign(list)
print list  # still [0]

append(list)
print list  # change to [0,1]
