'''
http://curiosityhealsthecat.blogspot.in/2013/06/thinking-out-aloud-python-decorators_8528.html

when Python encountered the @ symbol it did an internal equivalent of
    func = decorator(func)
'''


def decorator(func):
    def wrapper():
        print "Decorator calling func"
        func()
        print "Decorator called func"

    return wrapper


@decorator
def func():
    print "In the function"


def decorator_message(message):
    def decorator(func):
        def wrapper():
            print "Decorator calling func " + message
            return func()
            print "Decorator called func " + message

        return wrapper

    return decorator

def decorator_message2(name):
    def wrapper(func):
        print "register function '{0}' ".format(name)
        return func()
    return wrapper


@decorator_message("hello")
def func2():
    print "In the function2"

# func2()
