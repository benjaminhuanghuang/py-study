'''
  An iterable is an object that you can get an iterator from
  An iterator is an object with next (python 2) or __next__ (python 3)

  List comprehension is a tool for transforming any iterable into a new list
'''

list = [1,2,3]

iter = list.__iter__()
while True:
  try:
      print iter.next()
  except StopIteration:
      break
'''
  List comprehension is a tool for transforming any iterable into a new list
'''

numbers = [n for n in list if n%2==0]
