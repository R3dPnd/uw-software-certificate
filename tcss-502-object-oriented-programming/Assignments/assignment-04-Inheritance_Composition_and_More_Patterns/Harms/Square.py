from Shape import Shape

'''
<author> Preston Harms </author>
<summary> Square class that is a subclass of Shape. </summary>
'''
class Square(Shape):
    '''
    <description> Constructor for the Square class. </description>
    <param name=side> Side of the square. </param>
    '''
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    '''
    <description> Method to get the area of the square. </description>
    <return> The area of the square. </return>
    '''
    def area(self):
        return self.side * self.side

    '''
    <description> Method to get the perimeter of the square. </description>
    <return> The perimeter of the square. </return>
    '''
    def perimeter(self):
        return 4 * self.side

        