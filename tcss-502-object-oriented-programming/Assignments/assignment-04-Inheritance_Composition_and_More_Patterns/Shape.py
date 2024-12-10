from abc import ABC, abstractmethod

'''
<author> Preston Harms </author>
<summary> Shape class that is an abstract class. </summary>
'''
class Shape(ABC):
    '''
    <description>
        Shape class that is an abstract class.
    </description>
    '''
    def __init__(self, name):
        self.name = name
        
    '''
    <description>
        Abstract method to get the area of the shape.
    </description>
    <return> The area of the shape. </return>
    '''
    @abstractmethod
    def area(self):
        pass
    
    '''
    <description>
        Abstract method to get the perimeter of the shape.
    </description>
    <return> The perimeter of the shape. </return>
    '''
    @abstractmethod
    def perimeter(self):
        pass
    
    '''
    <description>
        Method to draw the shape.
    </description>
    <return> None </return>
    '''
    def draw(self):
        print(f"{self}")
        
    '''
    <description>
        Method to get the name of the shape.
    </description>
    <return> The name of the shape. </return>
    '''
    def __str__(self):
        return f"{self.name} area ({self.area()}, permitter {self.perimeter()})"