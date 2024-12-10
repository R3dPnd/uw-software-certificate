import unittest
from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory, ShapeEnums

class TestDrawingProgram(unittest.TestCase):
    def setUp(self):
        self.drawing_program = DrawingProgram()
        self.triangle1 = ShapeFactory.create_shape(ShapeEnums.TRIANGLE, 3, 4)  # Area = 6
        self.triangle2 = ShapeFactory.create_shape(ShapeEnums.TRIANGLE, 5, 6)  # Area = 15
        self.triangle3 = ShapeFactory.create_shape(ShapeEnums.TRIANGLE, 2, 8)  # Area = 8
        self.circle1 = ShapeFactory.create_shape(ShapeEnums.CIRCLE, 5)  # Area = 78.54
        self.circle2 = ShapeFactory.create_shape(ShapeEnums.CIRCLE, 10)
        self.circle3 = ShapeFactory.create_shape(ShapeEnums.CIRCLE, 15)
        self.rectangle1 = ShapeFactory.create_shape(ShapeEnums.RECTANGLE, 3, 4)  # Area = 12
        self.rectangle2 = ShapeFactory.create_shape(ShapeEnums.RECTANGLE, 5, 6)  # Area = 30
        self.rectangle3 = ShapeFactory.create_shape(ShapeEnums.RECTANGLE, 2, 8)  # Area = 16
        self.square1 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 3)  # Area = 9
        self.square2 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 5) # Area = 25
        self.square3 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 2) # Area = 4

    def test_add_shape(self):
        self.drawing_program.add_shape(self.triangle1)
        self.assertIn(self.triangle1, self.drawing_program.get_shapes())

    def test_remove_shape(self):
        self.drawing_program.add_shape(self.triangle1)
        self.drawing_program.remove_shape(self.triangle1)
        self.assertNotIn(self.triangle1, self.drawing_program.get_shapes())
    
    def test_sort_shapes(self):
        self.drawing_program.add_shape(self.triangle1)
        self.drawing_program.add_shape(self.triangle2)
        self.drawing_program.add_shape(self.triangle3)
        self.drawing_program.add_shape(self.circle1)
        self.drawing_program.add_shape(self.circle2)
        self.drawing_program.add_shape(self.circle3)
        self.drawing_program.add_shape(self.rectangle1)
        self.drawing_program.add_shape(self.rectangle2)
        self.drawing_program.add_shape(self.rectangle3)
        self.drawing_program.add_shape(self.square1)
        self.drawing_program.add_shape(self.square2)
        self.drawing_program.add_shape(self.square3)
        self.drawing_program.sort_shapes()
        self.assertEqual(self.drawing_program.get_shapes()[0], self.circle1)
        self.assertEqual(self.drawing_program.get_shapes()[1], self.circle2)
        self.assertEqual(self.drawing_program.get_shapes()[2], self.circle3)
        self.assertEqual(self.drawing_program.get_shapes()[3], self.rectangle1)
        self.assertEqual(self.drawing_program.get_shapes()[4], self.rectangle3)
        self.assertEqual(self.drawing_program.get_shapes()[5], self.rectangle2)
        self.assertEqual(self.drawing_program.get_shapes()[6], self.square3)
        self.assertEqual(self.drawing_program.get_shapes()[7], self.square1)
        self.assertEqual(self.drawing_program.get_shapes()[8], self.square2)
        self.assertEqual(self.drawing_program.get_shapes()[9], self.triangle1)
        self.assertEqual(self.drawing_program.get_shapes()[10], self.triangle3)
        self.assertEqual(self.drawing_program.get_shapes()[11], self.triangle2)
    
    def test_iter(self):
        self.drawing_program.add_shape(self.triangle1)
        self.drawing_program.add_shape(self.triangle2)
        self.drawing_program.add_shape(self.triangle3)
        self.drawing_program.add_shape(self.circle1)
        self.drawing_program.add_shape(self.circle2)
        self.drawing_program.add_shape(self.circle3)
        self.drawing_program.add_shape(self.rectangle1)
        self.drawing_program.add_shape(self.rectangle2)
        self.drawing_program.add_shape(self.rectangle3)
        self.drawing_program.add_shape(self.square1)
        self.drawing_program.add_shape(self.square2)
        self.drawing_program.add_shape(self.square3)
        for shape in self.drawing_program:
            self.assertIn(shape, self.drawing_program.get_shapes())
    
if __name__ == '__main__':
    unittest.main()