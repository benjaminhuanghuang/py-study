'''
http://curiosityhealsthecat.blogspot.com/2013/07/using-python-decorators-for-registering_8614.html

when Python encountered the @ symbol it did an internal equivalent of
    func = decorator(func)

using @app.register('/') cause calling to register()

In Flask-Login, we provide a user_loader callback by using decorator
https://flask-login.readthedocs.io/en/latest/
'''


func_map = {}

def register(name):
    def func_wrapper(func):
        print "Add func '{}' to map".format(name)
        func_map[name] = func
        return func

    return func_wrapper

@register('/')
def main_page_func():
    return "This is the main page."


@register('/next_page')
def next_page_func():
    return "This is the next page."

