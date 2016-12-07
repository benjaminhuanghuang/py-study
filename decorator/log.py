'''
1. put @log above def now() equals run code:
    now = log(now)

2. Call now equals run the wrapper() function returned by log

3. in the wrapper function, write log then call the original function.

'''

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2013-12-25'
now()