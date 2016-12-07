'''
http://coolshell.cn/articles/11265.html

@decorator
def func():
    pass
will be translate to
    func = decorator(func)

@decorator_one
@decorator_two
def func():
    pass
will be translate to
    func = decorator_one(decorator_two(func))
'''

def decorate(fn):
    print "decorate %s!" % fn.__name__
 
@decorate
def my_fun(a):
    print a

my_fun("test")