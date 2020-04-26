# http://tinyurul.com/j9qjnep

class Sqaure:
    slist = []

    def __init__(self, w):
        self.width = w
        self.slist.append(self)
        
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)

s1 = Sqaure(3)
print(s1)
