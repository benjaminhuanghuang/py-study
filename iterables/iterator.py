a = [1,2,3,4,5]

for x in a:    # interator was used here
  print (x)


# Get an iterator
it = iter(a)   # Call it = a.__iter__()
print(it)           # it is <list_iterator>

while True:
  try:
    val = next(it)   # call it.__next__()
  except StopIteration:      # python use execpt to know itertor is end
    break
  print(f'val={val}')