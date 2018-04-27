class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        if self.x == 0:
            print ("Eixo das ordenadas")
        else:
            print ((self.y)/(self.x))

Point(4, 10).slope_from_origin()
