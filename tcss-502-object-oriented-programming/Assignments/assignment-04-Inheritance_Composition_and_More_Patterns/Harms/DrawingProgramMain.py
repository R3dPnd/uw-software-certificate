from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory, ShapeEnums
'''
<author> Preston Harms </author>
<summary> DrawingProgramMain class that is the main class for the DrawingProgram. </summary>
'''
class DrawingProgramMain:
    '''
    <description>
        Main method that creates a DrawingProgram, adds shapes to it, prints the shapes, sorts the shapes, prints the sorted shapes, and draws the shapes.
    </description>
    <return> None </return>
    '''
    def main():
        # 1-creates a drawing program
        # 2-adds shapes to it
        # 3-prints the shapes
        # 4-sorts the shapes
        # 5-prints the sorted shapes
        drawing_program = DrawingProgram()
        circle_1 = ShapeFactory.create_shape(ShapeEnums.CIRCLE, 10)
        circle_2 = ShapeFactory.create_shape(ShapeEnums.CIRCLE, 5)
        circle_3 = ShapeFactory.create_shape(ShapeEnums.CIRCLE, 30)
        drawing_program.add_shape(circle_1)
        drawing_program.add_shape(circle_2)
        drawing_program.add_shape(circle_3)
        rectangle_1 = ShapeFactory.create_shape(ShapeEnums.RECTANGLE, 20, 10)
        rectangle_2 = ShapeFactory.create_shape(ShapeEnums.RECTANGLE, 30, 10)
        rectangle_3 = ShapeFactory.create_shape(ShapeEnums.RECTANGLE, 2, 10)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_2)
        drawing_program.add_shape(rectangle_3)
        triangle_1 = ShapeFactory.create_shape(ShapeEnums.TRIANGLE, 30, 200)
        triangle_2 = ShapeFactory.create_shape(ShapeEnums.TRIANGLE, 3, 20)
        triangle_3 = ShapeFactory.create_shape(ShapeEnums.TRIANGLE, 30, 2)
        drawing_program.add_shape(triangle_1)
        drawing_program.add_shape(triangle_2)
        drawing_program.add_shape(triangle_3)
        square_1 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 40)
        square_2 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 4)
        square_3 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 10)
        square_4 = ShapeFactory.create_shape(ShapeEnums.SQUARE, 30)
        drawing_program.add_shape(square_1)
        drawing_program.add_shape(square_2)
        drawing_program.add_shape(square_3)
        drawing_program.add_shape(square_4)
        print("Shapes:")
        drawing_program.print_shapes()
        drawing_program.sort_shapes()
        print("\nShapes sorted by area:")
        drawing_program.print_shapes()
        print("\nDrawing shapes:")
        drawing_program.draw()
        shapes = drawing_program.get_shapes()
        print("\nShapes from iterator:")
        drawing_program.set_shapes(shapes)
        for shape in drawing_program:
            print(shape)
    main()