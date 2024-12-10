from Shape import Shape

'''
<author>
    Preston Harms
</author>
<summary>
    Rectangle class that is a subclass of Shape.
</summary>
'''
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
