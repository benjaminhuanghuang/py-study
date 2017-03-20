# coding: utf8
'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
https://www.kancloud.cn/wizardforcel/liaoxuefeng/108528
http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html

purpose:  Enhance a function but do not change the definition of the function
'''


def log(func):
    def wrapper(*args, **kw):
        print 'call function {}'.format(func.__name__)
        return func(*args, **kw)

    return wrapper


# @log
def now():
    print "2017"


'''
此时，wrapper并未执行,因此没有任何输出
'''
wrapper = log(now)

'''
此时，wrapper会被执行，其中 'call %s():' % func.__name__ 会被执行两遍，一次是python看到@log自动执行，一次是wrapper = log(now)

'''
wrapper()


