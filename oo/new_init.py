'''
https://spyhce.com/blog/understanding-new-and-init

__new__ is called automatically when calling the class name (when instantiating),
__init__ is called every time an instance of the class is returned by __new__ passing the 
returned instance to __init__ as the 'self' parameter, 
'''

class A(object):
  def __new__(cls):
    print("A.__new__ is called")  # -> this is never called
    # return super(A, cls).__new__(cls)

  def __init__(self):
    print("A.__init__ called")

a = A()