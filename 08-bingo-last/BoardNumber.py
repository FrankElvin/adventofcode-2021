
class BoardNumber:
    def __init__(self, value, marked):
        self.value = value
        self.marked = marked

    def mark(self):
        self.marked = True

    def is_marked(self):
        return self.marked

    def is_equal(self, number):
        return self.value == number

    def __str__(self):
        if self.marked:
            return "%2d!" %self.value
        else:
            return "%2d " %self.value

