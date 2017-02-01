### For each key , value
d = {
    "1": "No1",
    "2": "No2",
    "9": "No9"
}

for key, value in d.iteritems():
    print key, value


#For Python 2.x:

for key, value in d.iteritems():
    pass
#For Python 3.x:
for key, value in d.items():
    pass

### build dict from two lists
x_list = [1, 2, 3]
y_list = ['a', 'b', 'c']

print dict(zip(x_list, y_list))

### create dict from list, use list as key, and default value 1
d = dict.fromkeys(["a", "b", "c"], 3)
print d

### Calculate element occur times
from collections import Counter

nums = [1, 2, 3, 3, 5, 7, 7, 9, 9, 9, 9]
dic = Counter(nums)
print dic

### Get default dict, avoid error when the key does not exist
import collections
list_dic = collections.defaultdict(list)
print list_dic["a"]
digits = collections.defaultdict(int)
print digits["a"]

