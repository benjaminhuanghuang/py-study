# https://py.windrunner.me/design-patterns/singleton.html
# https://wiki.python.org/moin/PythonDecoratorLibrary#Singleton

def singleton(cls):
    instance = cls()
    #  overwrite __call__ method
    instance.__call__ = lambda: instance
    return instance

@singleton
class Highlander:
    x = 100
    # Other code ...


highlander = Highlander()
another_highlander = Highlander()
assert id(highlander) == id(another_highlander)