# coding: utf8
'''

http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
https://www.kancloud.cn/wizardforcel/liaoxuefeng/108528


purpose:  Enhance a function but do not change the definition of the function
'''
'''
如果decorator本身需要传入参数，比如log的文本，就需要编写一个返回decorator的高阶函数。

now = log('-log message-')(now)
首先执行log('-log message-')，返回的是decorator函数，再调用返回的decorator函数，参数是now函数，返回值最终是wrapper函数。
'''
def log(message):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (message, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log("log message")
def now():
    print "2017"

# decorator = log('-log message-')
# decorated_func = decorator(now)
# decorated_func()

# now()
'''
函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
'''
print now.__name__
