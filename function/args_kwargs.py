# From Intermediate Python

# *args was used as a list
print "-----*args was used as a list:"


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


# **kwargs was used as dict
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


print "-----first with *args:"
args = ("two", 3, 5)
test_args_kwargs(*args)
# arg1: two
# arg2: 3
# arg3: 5

# now with **kwargs:
print "-----now with **kwargs:"
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)


# arg1: 5
# arg2: two
# arg3: 3


def use_together(fargs, *args, **kwargs):
    print "---- Demo use all args together"
    print("first normal arg is:", fargs)
    for arg in args:
        print("arg through *args:", arg)
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


test_var_args('yasoob', 'python', 'eggs', 'test')

if __name__ == "__main__":
    use_together("agrs1", 'args_1', 'args_2', 'args_3', {"arg1": 1, "arg2": "two", "arg2": 2})
    use_together("agrs1", args={"arg1": 1, "arg2": "two", "arg2": 2})
