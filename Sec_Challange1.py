# http://tinyurl.com/j9qjnep

class Square:
    square_list = []

    def __init__(self):
        self.square_list.append(self)

a_square = Square()
print(Square.square_list)
