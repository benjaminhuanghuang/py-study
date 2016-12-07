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