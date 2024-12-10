from Shape import Shape

'''
<author> Preston Harms </author>
<summary> Triangle class that is a subclass of Shape. </summary>
'''
class Triangle(Shape):
    '''
    <description> Constructor for the Triangle class. </description>
    <param name=base> Base of the triangle. </param>
    <param name=height> Height of the triangle. </param>
    '''
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    '''
    <description> Method to get the area of the triangle. </description>
    <return> The area of the triangle. </return>
    '''
    def area(self):
        return 0.5 * self.base * self.height
    
    '''
    <description> Method to get the perimeter of the triangle. </description>
    <return> The perimeter of the triangle. </return>
    '''
    def perimeter(self):
        return 3 * self.base
    