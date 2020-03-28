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

    # method는 class 안에 있는 function

    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 6
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"


class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return "Car with no roof"


class Something(Convertible):
    pass


# print(dir(Car))
porche = Convertible(color="green", price="$40")
print(porche.color, porche.price)  # print(porche) = print(porche.__str__)
print(porche.take_off())
porche.wheels
print(porche.color)

mini = Convertible()
print(mini.color, mini.price)


# def start(self):
#     print(self.doors)
#     print("I started")


# porche = Car()
# porche.color = "R Red"
# porche.start()  # porche.start() = porche.start(porche)

# porche = Car()
# porche.color = "Red"
# print(porche.windows)
# print(porche.color)

# ferrari = Car()
# ferrari.color = "Yellow"
# print(ferrari.color)
