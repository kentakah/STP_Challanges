# http://tinyurl.com/hz9qdh3

class Horse:
    def __init__(self, n, c, o):
        self.name = n
        self.coloer = c
        self.owner = o


class Rider:
    def __init__(self, r, nbr):
        self.name = r
        self.number = nbr


rider1 = Rider("John", 15)
horse1 = Horse("Speedstar", "Brown", rider1)

print("{} rides the horse called \"{}\"".format(horse1.owner.name,horse1.name))
