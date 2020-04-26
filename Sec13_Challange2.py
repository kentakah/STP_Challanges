# http://tinyurl.com/hz9qdh3

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * self.length

class Square:
    def __init__(self, w, a = 0):
        self.width = w
        self.additional_length = a

    def calculate_perimeter(self):
        return self.width ** 2

    def change_size(self):
        if self.additional_length * -1 > self.width:
            print("cannot deduct that much.")
        else:
            return self.width + self.additional_length
        


rect1 = Rectangle(20,10)
sq1 = Square(8, 2)

print("Rectanble area size is {} * {} = {}".format(rect1.width, rect1.length, rect1.calculate_perimeter()))
print("Square area size is {} ** 2 = {}".format(sq1.width, sq1.calculate_perimeter()))
print("New size is {}".format(sq1.change_size()))
