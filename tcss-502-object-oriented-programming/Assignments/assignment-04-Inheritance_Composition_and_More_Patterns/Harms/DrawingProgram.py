'''
<author>
    Preston Harms
</author>
<summary>
    DrawingProgram class that is an observable class.
</summary>
'''
class DrawingProgram:
    '''
    <description>
        DrawingProgram class that is an observable class.
    </description>
    '''
    def __init__(self):
        self.shapes = []

    '''
    <description>
        Method to add a shape to the DrawingProgram.
    </description>
    <param name=shape> Shape to add to the DrawingProgram. </param>
    <return> None </return>
    '''
    def add_shape(self, shape):
        self.shapes.append(shape)
    
    '''
    <description>
        Method to remove a shape from the DrawingProgram.
    </description>
    <param name=shape> Shape to remove from the DrawingProgram. </param>
    <return> None </return>
    '''
    def remove_shape(self, shape):
        self.shapes.remove(shape)
    
    '''
    <description>
        Method to print the shapes in the DrawingProgram.
    </description>
    <return> None </return>
    '''
    def print_shapes(self):
        for shape in self.shapes:
            print(shape)
    
    '''
    <description>
        Method to sort the shapes in the DrawingProgram.
    </description>
    <return> None </return>
    '''
    def sort_shapes(self):
        self.shapes = self._merge_sort(self.shapes)
    
    '''
    <description>
        Method to merge sort the shapes in the DrawingProgram.
    </description>
    <param name=shapes> Shapes to merge sort. </param>
    <return> The sorted shapes. </return>
    '''
    def _merge_sort(self, shapes):
        if len(shapes) <= 1:
            return shapes
        
        mid = len(shapes) // 2
        left_half = self._merge_sort(shapes[:mid])
        right_half = self._merge_sort(shapes[mid:])
        
        return self._merge(left_half, right_half)
    
    '''
    <description>
        Method to merge the left and right halves of the shapes.
    </description>
    <param name=left> Left half of the shapes. </param>
    <param name=right> Right half of the shapes. </param>
    <return> The sorted list of shapes. </return>
    '''
    def _merge(self, left, right):
        sorted_list = []
        while left and right:
            if left[0].name < right[0].name:
                sorted_list.append(left.pop(0))
            elif left[0].name > right[0].name:
                sorted_list.append(right.pop(0))
            else:
                if left[0].area() <= right[0].area():
                    sorted_list.append(left.pop(0))
                else:
                    sorted_list.append(right.pop(0))
        
        sorted_list.extend(left)
        sorted_list.extend(right)
        
        return sorted_list
    
    ''' 
    <description>
        Method to get the shapes in the DrawingProgram.
    </description>
    <return> The shapes in the DrawingProgram. </return>
    '''
    def get_shapes(self):
        return self.shapes

    '''
    <description>
        Method to set the shapes in the DrawingProgram.
    </description>
    <param name=shapes> Shapes to set in the DrawingProgram. </param>
    <return> None </return>
    '''
    def set_shapes(self, shapes):
        self.shapes = shapes

    ''' 
    <description>
        Method to draw the shapes in the DrawingProgram.
    </description>
    <return> None </return>
    '''
    def draw(self):
        for shape in self.shapes:
            shape.draw()
    
    '''
    <description>
        Method to get the iterator for the DrawingProgram.
    </description>
    <return> The iterator for the DrawingProgram. </return>
    '''     
    def __iter__(self):
        return DrawingProgramIterator(self)

'''
<author>
    Preston Harms  
</author>
<summary>
    DrawingProgramIterator class that is an iterator class.
</summary>
'''
class DrawingProgramIterator:
    '''
    <description>
        DrawingProgramIterator class that is an iterator class.
    </description>
    <param name=drawing_program> DrawingProgram to iterate over. </param>
    '''
    def __init__(self, drawing_program):
        self.drawing_program = drawing_program
        self.index = 0

    '''
    <description>
        Method to get the next shape in the DrawingProgram.
    </description>
    <return> The next shape in the DrawingProgram. </return>
    '''
    def __next__(self):
        if self.index < len(self.drawing_program.shapes):
            result = self.drawing_program.shapes[self.index]
            self.index += 1
            return result
        raise StopIteration

    '''
    <description>
        Method to get the iterator for the DrawingProgram.
    </description>
    <return> The iterator for the DrawingProgram. </return>
    '''
    def __iter__(self):
        return self