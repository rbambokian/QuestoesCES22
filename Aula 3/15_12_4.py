class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        if self.x == 0:
            print ("Eixo das ordenadas")
        else:
            print ((self.y)/(self.x))

    def get_line_to(self, point):
        if (self.x == point.x):
            print ("Coincide com o eixo das ordenadas")
        else:
            a = (point.y - self.y)/(point.x - self.x)
            print(a, (point.y - a*point.x))

print(Point(4, 11).get_line_to(Point(6, 15)))
