# http://tinyurl.com/gpqe62e

class Hexagon:
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return(self.length * 8)

try:
    hexagon = Hexagon(float(input("Please type area length:")))
    print(hexagon.calculate_perimeter())
except ValueError:
    print("Please type a float value")
