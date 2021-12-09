
class CipheredDigit:

    def __init__(self, chars):
        self.chars = sorted(chars)
        self.known = False
        self.unciphered = None

    def mark(self, number):
        self.known = True
        self.unciphered = number
    
    def __repr__(self):
        if self.known:
            return "%s:%d" %(''.join(self.chars), self.unciphered)
        else:
            return "%s:" %(''.join(self.chars))

