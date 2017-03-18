# coding: utf8
'''

http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
https://www.kancloud.cn/wizardforcel/liaoxuefeng/108528


purpose:  Enhance a function but do not change the definition of the function
'''

# Step 1. Define a function
# Step 2. Add a decorator to myfunc
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# @log
def now():
    print "2017"

decorated_func = log(now)
decorated_func()
'''
此时执行代码会输出
call wrapper():
call now():
2017
这是因为把@log放在def new() 之前，也会引发函数调用。
如果注释掉@log再执行，输出为
call now():
2017
'''

# now()
