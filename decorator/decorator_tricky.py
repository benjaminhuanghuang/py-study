# coding: utf-8
'''
In Flask, decorator was used to register route function like
    @user.route('/next_page')
    def next_page_func()

That means decorator executes when we use it to define a function.
The question is, in this demo, decorator @register is executed but @log not.
Why?

We already know when Python encountered the @ symbol it did an internal equivalent of
    func = decorator(func)

The reason is when the parameter is not function, python will do
    decorator = log('-log message-')
    decorated_func = decorator(fun)
    decorated_func()
At step 2 decorator(fun) was executed and print message!

'''

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
'''

def log(func):
    def wrapper():
        print "##log decorator added"
        return func
    return wrapper

def register(name):
    def wrapper(func):
        print "## register function '{0}' ".format(name)
        return func
        # print "## register function '{0}' ".format(name)
    return wrapper

def register2(name):
    def decorator(func):
        def wrapper():
            print ">> register2 function '{0}' ".format(name)
            return func()
        return wrapper

    return decorator

@log
def fun1():
    print "fun 1"


@register("fun2")
def fun2():
    print "fun 2"

@register2("fun3")
def fun3():
    print "fun 3"

# fun1()

# now2()

# fun3()


