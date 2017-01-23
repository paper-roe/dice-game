class Shape:
    def __init__(self, type, points):
        self.type = type
        self.points = points

class Circle(Shape):
    def __init__(self):
        super().__init__('Circle', 0)

class Square(Shape):
    def __init__(self):
        super().__init__('Square', 4)

class Triangle(Shape):
    def __init__(self):
        super().__init__('Triangle', 3)