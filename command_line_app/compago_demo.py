import compago

app = compago.Application()


@app.command
def greet(to="world"):
    print "Hello,", to, "!"


@app.command
def ungreet(to="world"):
    print "Goodbye,", to, "!"


if __name__ == '__main__':
    app.run()

'''
$ ./program greet --to=Mark
Hello, Mark!
!
$ ./program ungreet
Goodbye, world!
'''