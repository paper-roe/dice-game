class Shape:
    def __init__(self, type, points):
        self.type = type
        self.points = points

class Triangle(Shape):
    def __init__(self):                     # function initailise using base
        super().__init__('Triangle', 3)     # classes init function

class Square(Shape):
    def __init__(self):
        super().__init__('Square', 4)

class Circle(Shape):
    def __init__(self):
        super().__init__('Circle', 0)

def describe(tri, sqr, circ):
    print('Shape: ' + tri.type + '\t| Points: ' + str(tri.points))
    print('Shape: ' + sqr.type + '\t\t| Points: ' + str(sqr.points))
    print('Shape: ' + circ.type + '\t\t| Points: ' + str(circ.points))

def main():
    tri = Triangle()
    sqr = Square()
    circ = Circle()

    describe(tri, sqr, circ)

if __name__ == '__main__':
    main()