'''
http://curiosityhealsthecat.blogspot.com/2013/07/using-python-decorators-for-registering_8614.html

when Python encountered the @ symbol it did an internal equivalent of
    func = decorator(func)

using @app.register('/') cause calling to register()

In Flask, decorator was used to register route function like
    @user.route('/next_page')
    def next_page_func()

'''


class MyApp():
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            print "Add func '{}' to map".format(name)
            self.func_map[name] = func
            return func

        return func_wrapper

    def call_registered(self, name=None):
        func = self.func_map.get(name, None)
        if func is None:
            raise Exception("No function registered against - " + str(name))
        return func()


app = MyApp()


@app.register('/')
def main_page_func():
    return "This is the main page."


@app.register('/next_page')
def next_page_func():
    return "This is the next page."


# print app.call_registered('/')
# print app.call_registered('/next_page')
