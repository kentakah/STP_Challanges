# http://tinyurl.com/hz9qdh3

class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w=0, l=0):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * self.length

class Square(Shape):
    def __init__(self, w=0):
        self.width = w

    def calculate_perimeter(self):
        return self.width ** 2

    def change_size(self, a):
        if a * -1 > self.width:
            print("cannot deduct that much.")
        else:
            return self.width + a

shape1 = Shape()
rect1 = Rectangle(20,10)
sq1 = Square(8)

print("Rectanble area size is {} * {} = {}".format(rect1.width, rect1.length, rect1.calculate_perimeter()))
print("Square area size is {} ** 2 = {}".format(sq1.width, sq1.calculate_perimeter()))
print("New size is {}".format(sq1.change_size(2)))

shape1.what_am_i()
rect1.what_am_i()
sq1.what_am_i()
