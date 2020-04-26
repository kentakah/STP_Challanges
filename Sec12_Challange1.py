# http://tinyurl.com/gpqe62e

class Apple:
    def __init__(self, w, c, d, t):
        self.weight = w
        self.color = c
        self.days = d
        self.temp = t
        print("Created!")

apple = Apple(250, "Red", 3, 25)
#apple = Apple()
apple.weight = input("Weight?: ")
apple.color = input("Color?: ")
apple.days = input("How many days past after purchase?: ")
apple.days = input("What is the roome temperature?: ")
print(apple)
print(apple.weight, apple.color, apple.days, apple.temp)
