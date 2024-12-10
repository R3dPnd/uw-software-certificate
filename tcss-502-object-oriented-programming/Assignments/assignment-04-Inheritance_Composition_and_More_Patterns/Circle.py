from Shape import Shape

'''
<author>
    Preston Harms
</author>
<summary>
    Circle class that is a subclass of Shape.
</summary>
'''
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    '''
    <description>
        Multiply the radius by itself and then multiply the result by 3.14 to get the area of the circle.
    </description>
    <return>
        The area of the circle.
    </return>
    '''
    def area(self):
        return 3.14 * self.radius * self.radius
    
    '''
    <description>
        Multiply the radius by 2 and then multiply the result by 3.14 to get the perimeter of the circle.
    </description>
    <return>
        The perimeter of the circle.
    </return>
    '''
    def perimeter(self):
        return 2 * 3.14 * self.radius
    