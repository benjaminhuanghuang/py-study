class MyListIterator:
  # index is the start position
  def __init__(self, my_list, index= 0):
     self.my_list = my_list
     self.index = index

  def __next__(self):
    if self.index < len(self.my_list.data):
      val = self.my_list.data[self.index]
      self.index += 1
      return val
    else:
      raise 

class MyList:
  def __init__(self, data):
    self.data = list(data)
  
  def __iter__(self):
    return MyListIterator(self)


my_list = MyList([1,2,3,4,5])

for x in my_list:
  print(x)