'''
https://www.youtube.com/watch?v=9oyr0mocZTg&t=1s

'''


def make_printer(word):
    def inner():
        print word

    return inner


p = make_printer("Hello")
p()


#
# First decorator
#
def first_decorator(wrapped):
    def inner(*args, **kwargs):
        return wrapped(*args, **kwargs)

    return inner


@first_decorator
def myfunc():
    pass


myfunc = first_decorator(myfunc)


#
#
#
def shout(wrapped):
    def inner(*args, **kwargs):
        print "BEFORE!"
        ret = wrapped(*args, **kwargs)
        print "AFTER!"
        return ret

    return inner


@shout
def myfunc():
    print("wow!")


myfunc()

# How does it work:
myfunc = shout(myfunc)
# myfunc()

# error of function name:
print myfunc.__name__   # 'inner'

