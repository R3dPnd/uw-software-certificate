import unittest

from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Square import Square

class Shape:
    def __init__(self, name, area):
        self.name = name
        self._area = area

    def draw(self):
        pass

    def area(self):
        return self._area

    def __str__(self):
        return self.name


class TestShapes(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3, 4)  # Base = 3, Height = 4, Area = 6

    def test_triangle_initialization(self):
        self.assertEqual(self.triangle.name, "Triangle")
        self.assertEqual(self.triangle.base, 3)
        self.assertEqual(self.triangle.height, 4)
        self.assertEqual(self.triangle.area(), 6)

    def test_triangle_area(self):
        self.assertEqual(self.triangle.area(), 6)
        
    def test_circle_initialization(self):
        circle = Circle(5)
        self.assertEqual(circle.name, "Circle")
        self.assertEqual(circle.radius, 5)
        self.assertEqual(circle.area(), 78.5)
    
    def test_rectangle_initialization(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.name, "Rectangle")
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.area(), 12)
    
    def test_square_initialization(self):
        square = Square(3)
        self.assertEqual(square.name, "Square")
        self.assertEqual(square.side, 3)
        self.assertEqual(square.area(), 9)

if __name__ == '__main__':
    unittest.main()