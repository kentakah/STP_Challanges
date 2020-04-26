# http://tinyurl.com/gpqe62e
import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def size(self):
        return self.radius ** 2 * math.pi

try:
    circle = Circle(int(input("please type a number:")))
    print(circle.size())
except ValueError:
    print("Please type an integer:")
