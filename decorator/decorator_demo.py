def testDe1(func):
    def de(a, b, c):
        func(a, b, c)
        print('1')
        print('XX')


    print('2')
    return de


@testDe1
def test2(a, b, c):
    print(a + b + c)


if __name__ == '__main__':
    print "Use decorator"
    test2(1, 2, 3)

    print "Use function"
    de = testDe1(test2)
    de(1, 2, 3)
