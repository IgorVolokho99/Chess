class Coord:
    def __init__(self, y=-1, x=-1):
        self.y = y
        self.x = x
        self.valide = True
        self.check_valid()

    def check_valid(self):
        if self.x in range(8) and self.y in range(8):
            self.valide = True
        else:
            self.valide = False

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __repr__(self):
        return f"y : {self.y} ; x : {self.x}"
