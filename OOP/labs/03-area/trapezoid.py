

class Figure:
    def area(self):
        pass

class Trapezoid(Figure):
    _a: float = 0 # base 1
    _b: float = 0 # base 2
    _h: float = 0 # height

    def __init__(self, _a, _b, _h) -> None:
        if a <= 0 or b <= 0 or h <= 0:
            raise Exception('Bases (a and b) and height (h) of trapezoid must be positive numbers!')
        self._a = a
        self._b = b
        self._h = h

    # Area = (a+b)/2 * h, where a and b are bases and h is height
    def area(self):
        return (self._a + self._b) / 2 * self._h


a = int(input("First base of trapezoid: "))
b = int(input("Second base of trapezoid: "))
h = int(input("Height of trapezoid: "))

trapezoid = Trapezoid(a, b, h)
area = trapezoid.area()

print("Area of the trapezoid with bases a = {}, b = {} and height = {} is: {}".format(a, b, h, area))

