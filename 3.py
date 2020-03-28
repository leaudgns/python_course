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

#plus(1, 2, 4, 6, 78, 3, 6, 67, 87, 3, 7, 8)


class Car():
    wheels = 4
    doors = 4
    windows = 6
    seats = 4
    # method는 class 안에 있는 function

    def start(self):
        print(self.doors)
        print("I started")


porche = Car()
porche.color = "R Red"
porche.start()  # porche.start() = porche.start(porche)

# porche = Car()
# porche.color = "Red"
# print(porche.windows)
# print(porche.color)

# ferrari = Car()
# ferrari.color = "Yellow"
# print(ferrari.color)
