# coding: utf8

# From Intermediate Python

# *args was used as a list
print "----- *args was used as a list:"


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')
# 在这个例子中，第一参数 yasoob 被当作normal arg，因为函数参数列表中*argv前面有一个参数，剩余的参数全被当作 argv

print "----- *kwargs was used as a dictionary:"
# **kwargs was used as dict
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")


#
# Using *args and **kwargs in function call
#
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

print "----- test_args_kwargs with *args:"
'''
使用 *args把参数传入函数，输出
 arg1: "1"
 arg2: 2
 arg3: 3
'''
args = ("1", 2, 3)
test_args_kwargs(*args)

print "----- test_args_kwargs with **kwargs:"
'''
使用 **kwargs 把参数传入函数，输出
 arg1: "1"
 arg2: 2
 arg3: 3
但kwargs 中的key 必须和函数中的参数名保持一致， 不一致的key回报错

test_args_kwargs("normal arg", **kwargs) 也会导致错误：
TypeError: test_args_kwargs() got multiple values for keyword argument 'arg1'
'''
#kwargs = {"arg3": 3, "arg2": 2, "arg8": "1"}  # ERROR
kwargs = {"arg3": 3, "arg2": 2, "arg1": "1"}
test_args_kwargs(**kwargs)

#test_args_kwargs("normal arg", **kwargs)       # ERROR

#  Summary:
#  当传入一堆参数，python会先匹配normal args， 然后用剩余的参数匹配 *args, 最后匹配**kwargs
#  有名字的参数必须在参数列表的末尾，否则报错：SyntaxError: non-keyword arg after keyword arg
#  **kwargs 必须在参数列表的末尾，否则报错：SyntaxError: invalid syntax

def use_together(normal1, normal2, *args, **kwargs):
    print("first normal arg is:", normal1)
    print("second normal arg is:", normal2)

    for arg in args:
        print("arg through *args:", arg)

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
    print args

print "\n---- Demo use all args together with error \n"
# use_together("normal_arg1", 'args_1', 'args_2', 'args_3',karg = "karg", {"arg1": 1, "arg2": "two", "arg2": 2})

print "\n---- Demo use all args together 1\n"
use_together("normal_arg1", 'args_1', 'args_2', 'args_3',{"arg1": 1, "arg2": "two", "arg2": 2}, karg1 = "karg1")

print "\n---- Demo use all args together 2\n"
use_together("agrs1", 'args_1', 'args_2', 'args_3', key1={"arg1": 1, "arg2": "two", "arg2": 2}, key2={"arg1": 1, "arg2": "two", "arg2": 2})

#
# 应用： default parameter
#
def func_with_default_arg(normal1, normal2, normal3="n3", *args, **kwargs):
    print("first normal arg is:", normal1)
    print("second normal arg is:", normal2)
    print("third normal arg is:", normal3)

    for arg in args:
        print("arg through *args:", arg)

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

    print args

print "\n---- Demo function with default args\n"
func_with_default_arg("normal1", 'normal2', "args_1", 'args_2', 'args_3', key1={"arg1": 1, "arg2": "two", "arg2": 2}, key2={"arg1": 1, "arg2": "two", "arg2": 2})


#
# 应用： 避免函数的参数列表过长，难以维护
#
def create_user(**kwargs):
    email = kwargs.get("email", "")
    password = kwargs.get("password", "")
    first_name = kwargs.get("first_name", "")
    for key, value in kwargs.items():
        print("key {0} = value {1}".format(key, value))


def create_user_old(email, password, exp_date):
    pass


if __name__ == "__main__":
    pass
    # use_together("agrs1", 'args_1', 'args_2', 'args_3', {"arg1": 1, "arg2": "two", "arg2": 2})


    # Error: SyntaxError: non-keyword arg after keyword arg
    # All arguments like a=x, b=xx will be deal as **kwargs
    # use_together("agrs1", aaa={"arg1": 1, "arg2": "two", "arg2": 2}, {"arg1": 1, "arg2": "two", "arg2": 2})

    # create_user(email="a@1.com", first_name="tom", exp_date="1233-11-222")
    # create_user_old("1233-11-222")
