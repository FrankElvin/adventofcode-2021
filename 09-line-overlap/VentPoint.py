
class VentPoint:
    def __init__(self, x, y, marks=0):
        self.x = x
        self.y = y
        self.marks = marks

    def mark(self):
        self.marks += 1

    def is_marked_times(self, number):
        return self.marks == number

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        if self.marks != 0:
            return "%2d" %self.marks
        else:
            #return " ."
            return "%2d %2d |" %(self.x, self.y)


