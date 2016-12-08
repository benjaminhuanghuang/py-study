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
        print("key {0} = value {1}".format(key, value))
    print args


def create_user(**args):
    email = args.get("email", "")
    password = args.get("password", "")
    first_name = args.get("first_name", "")
    for key, value in args.items():
        print("key {0} = value {1}".format(key, value))


def create_user_old(email, password, exp_date):
    pass


if __name__ == "__main__":
    # use_together("agrs1", 'args_1', 'args_2', 'args_3', {"arg1": 1, "arg2": "two", "arg2": 2})
    use_together("agrs1", key1={"arg1": 1, "arg2": "two", "arg2": 2}, key2={"arg1": 1, "arg2": "two", "arg2": 2})

    # Error: SyntaxError: non-keyword arg after keyword arg
    # All arguments like a=x, b=xx will be deal as **kwargs
    # use_together("agrs1", aaa={"arg1": 1, "arg2": "two", "arg2": 2}, {"arg1": 1, "arg2": "two", "arg2": 2})

    # create_user(email="a@1.com", first_name="tom", exp_date="1233-11-222")
    # create_user_old("1233-11-222")
