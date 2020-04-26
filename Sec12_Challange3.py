# http://tinyurl.com/gpqe62e

class Triangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def area(self):
        return (self.height * self.width) / 2

x = input("Please type height: ")
y = input("please type width: ")
try:
    x = float(x)
    y = float(y)
    triangle = Triangle(x, y)
    print(triangle.area())
except ValueError:
    print("Please type float value.")
