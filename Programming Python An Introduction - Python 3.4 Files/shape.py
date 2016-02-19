# shape.py
#   Class definition for a shape.

class shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet."
        self.author = "Nobody has claimed to make this shape yet."

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return (self.x + self.y) * 2

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.authorName = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
        
        
