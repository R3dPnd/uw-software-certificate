from enum import Enum
from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle

'''
<author>
    Preston Harms
</author>
<summary>
    ShapeFactory class that is a factory class for creating shapes.
</summary>
'''
class ShapeFactory:
    '''
    <description>
        Method to create a shape based on the shape type and arguments.
    </description>
    <param name=shape_type> Type of shape to create. </param>
    <param name=args> Arguments to create the shape. </param>
    <return> The created shape. </return>
    '''
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == ShapeEnums.CIRCLE:
            return Circle(*args)
        elif shape_type == ShapeEnums.RECTANGLE:
            return Rectangle(*args)
        elif shape_type == ShapeEnums.SQUARE:
            return Square(*args)
        elif shape_type == ShapeEnums.TRIANGLE:
            return Triangle(*args)
        else:
            return None
    
class ShapeEnums(Enum):
    CIRCLE = "Circle"
    RECTANGLE = "Rectangle" 
    SQUARE = "Square"
    TRIANGLE = "Triangle"