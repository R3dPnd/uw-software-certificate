from clock import Clock

class ClockShop():
    def __init__(self):
        self._clocks = []
    '''
    fill_clock_shop(self, list_of_times): the method walks through the list of times (strings
    formatted hh:mm:ss, guaranteed), creates Clock objects, and adds them to your list of 
    clocks. There will be at least one clock time in the list. Clocks should be added in the 
    order they occur in list. If there are already clocks, the new clocks should be appended 
    to the end of the existing list of clocks. To grab the hour, minute and second from each 
    string examine the split function from the string class. You can pass it a string that 
    contains the delimiter you would like to split the data by. The split function will return
    a tuple of strings. Here is how it might look: (hour, minute, second) = time.split(":") . 
    From there you can access hour, minute and second independently and turn them into ints.
    '''
    def fill_clock_shop(self, list_of_times):
        for time in list_of_times:
            hour, minute, second = time.split(":")
            self._clocks.append(Clock(int(hour), int(minute), int(second)))
            
    '''
    sort_clocks(self): sorts the Clocks in ascending (smallest time to largest time) order. 
    You must write the code to sort the array of Clocks
    '''
    def sort_clocks(self):
        self._clocks.sort(key=lambda x: x.hour() * 3600 + x.minute() * 60 + x.second())
    
    '''
    find_clock(self, a_clock): it is passed a Clock object and checks to see if it exists in 
    the Clock If it does exist, return the index of where the first one was found.  If it does
    not exist, return a -1.
    '''
    def find_clock(self, a_clock):
        for i in range(len(self._clocks)):
            if self._clocks[i] == a_clock:
                return i
        return -1
    
    '''
    __str__(self): builds a string containing each Clock object in string format (via the 
    __str(self)__ in the Clock class) and returns that string. Each Clock object should be 
    separated from the others by a newline (\n). The last clock in the list should also have a
    newline following it.
    '''
    def __str__(self):
        return ''.join([str(clock) + '\n' for clock in self._clocks])
    
    '''
    get_clock(self, index): it is passed an integer index of which Clock to retrieve from the
    list of Clock If the index is outside the range of the array, raise an exception with an 
    appropriate message.  If the index falls within the list, return the Clock object at that
    index.
    '''
    def get_clock(self, index):
        if index < 0 or index >= len(self._clocks):
            raise ValueError("Index out of range")
        return self._clocks[index]
    
    '''
    set_clock(self, a_clock, index): it is passed a Clock object and an index. The method places the Clock object at the specified index in the list.  If the index is outside the range of the list, raise an exception with an appropriate message.
    '''
    def set_clock(self, a_clock, index):
        if index < 0 or index >= len(self._clocks):
            raise ValueError("Index out of range")
        self._clocks[index] = a_clock