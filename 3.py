# def plus(a, b, *args, **kargs):
#     print(args)
#     print(kargs)
#     return a + b


# plus(1, 2, 1, 1, 1, 1, 1, hello=True, asdf=True,
#      qwre=True, fdsa=True, asdfd=True, qf=True)
def plus(*args):
    result = 0
    for number in args:
        result += number
    print(result)


plus(1, 2, 4, 6, 78, 3, 6, 67, 87, 3, 7, 8)
