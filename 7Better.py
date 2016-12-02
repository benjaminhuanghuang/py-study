# Case 1
cities = ['New York', 'London']

# The bad way
i = 0
for city in cities:
    print i, city
    i += 1

# The better way
for i, city in enumerate(cities):
    print i, city

# Case 2
x_list = [1, 2, 3]
y_list = ['a', 'b', 'c']
# The bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print x, y
# The better way
for x, y in zip(x_list, y_list):
    print x, y

print dict(zip(x_list, y_list))

# Case 3
x = 10
y = -10
# bad way
tmp = y
y = x
x = tmp
# better way
x, y = y, x

# Case 4
ages = {
    'Tom': 10,
    'Jake': 20
}

# bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknow'

# better way
age = ages.get('Dick', 'Unknown')

# Case 5
needle = 'd'
haystack = ['a', 'b', 'c']
# bad way
found = False
for letter in haystack:
    if needle == letter:
        found = True
        break
if not found:
    print 'Not found'

# better way
for letter in haystack:
    if needle == letter:
        found = True
        break
else:  # If no break occurred
    print 'Not found'

# Case 6
# bad way
f = open('a.txt')
text = f.read()
for line in text.splint('\n'):
    print line
f.close()

# better way

with open('a.txt') as f:
    for line in f:
        print line

# Case 7
try:
    print int('x')
except:
    print 'Conversion failed!'
else:  # If no exception
    print 'Conversion successful!'
finally:
    print 'Done!'
