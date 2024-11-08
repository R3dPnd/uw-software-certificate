class Clock():
    
    '''
    Clock Constructor __init__(self, hour, minute, second): create a Clock object and specify 
    the starting hour, minute, and second via parameters (we will use integer values for our 
    data)
    it defaults to 00:00:00 (hours, minutes, seconds) (12am) if no values are specified at 
    creation
    '''
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second
    
    '''
    __repr__(self): (same as __str__ for what we are doing) get the current time in String 
    format -- the object will return a String with the hours, minutes and seconds as follows:
    hh:mm:ss (ex: 9:49:59)
    '''
    def __repr__(self):
        return f"{self._hour}:{self._minute}:{self._second}"
    
    '''
    hour(self): -- the object will report as follows: hh (ex: 18 -- which means it is 6pm) --
    the value returned should be the hour
    '''
    def hour(self):
        return self._hour
    
    '''
    minute(self): -- the object will report as follows: mm (ex: 56) -- the value returned 
    should be the minute
    '''
    def minute(self):
        return self._minute
    
    '''
    second(self): -- the object will report as follows: ss (ex: 6) -- the value returned 
    should be the second
    '''
    def second(self):
        return self._second
    '''
    set_hour(self, new_hour): set the current hour (a number from 0 through 23 will be passed
    in to the object from outside) (any value outside this range should raise an exception 
    with an appropriate error message)
    '''
    def set_hour(self, new_hour):
        if new_hour < 0 or new_hour > 23:
            raise ValueError("Hour must be between 0 and 23")
        self._hour = new_hour
    
    '''
    set_minute(self, new_minute): set the current minute (a number from 0 through 59 will be 
    passed in to the object from outside) (any value outside this range should raise an 
    exception with an appropriate message)
    '''
    def set_minute(self, new_minute):
        if new_minute < 0 or new_minute > 59:
            raise ValueError("Minute must be between 0 and 59")
        self._minute = new_minute
    
    '''
    set_second(self, new_second): set the current second (a number from 0 through 59 will be 
    passed in to the object from outside) (any value outside this range should raise an 
    exception with an appropriate message)
    '''
    def set_second(self, new_second):
        if new_second < 0 or new_second > 59:
            raise ValueError("Second must be between 0 and 59")
        self._second = new_second
        
    ''' 
    advance_hour(self, amount_to_advance): advance the current hour (a number 0 or greater 
    will be passed in to the object from outside -- the resulting hour should be represented 
    in the range of 0 to 23) (HINT: % is your friend) (any value less than 0 should raise an 
    exception with an appropriate message)
    '''
    def advance_hour(self, amount_to_advance):
        if amount_to_advance < 0:
            raise ValueError("Amount to advance must be greater than 0")
        self._hour = (self._hour + amount_to_advance) % 24
        
    '''
    advance_minute(self, amount_to_advance): advance the current minute (a number 0 or 
    greater will be passed in to the object from outside -- the resulting minute should be 
    represented in the range of 0 to 59 *AND* the hour should be updated accordingly) (any 
    value less than 0 should raise an exception with an appropriate message)
    '''
    def advance_minute(self, amount_to_advance):
        if amount_to_advance < 0:
            raise ValueError("Amount to advance must be greater than 0")
        self._minute = (self._minute + amount_to_advance) % 60
        self._hour += (amount_to_advance // 60) % 24
        
    '''
    set_to_current_time(self): set the time to the current time (hours, minutes, and seconds) 
    based on what your computer reports.
    '''
    def set_to_current_time(self):
        import datetime
        now = datetime.datetime.now()
        self._hour = now.hour
        self._minute = now.minute
        self._second = now.second
        
    '''
    __eq__(self, other): compare against another Clock object for equality (an equals method) 
    to Make sure the data passed as a parameter is a Clock (isinstance helps with this) then 
    check that the hour, minute, and second of the clocks are the same for equality
    '''
    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self._hour == other._hour and self._minute == other._minute and self._second == other._second
    
    '''
    __lt__(self, other): compare against another Clock to see if current clock’s time is 
    before other clock – make sure the parameter is a Clock then check hour, minute, and 
    second as necessary to determine if the current Clock (self) is less than the other Clock
    '''
    def __lt__(self, other):
        if not isinstance(other, Clock):
            return False
        if self._hour < other.hour():
            return True
        if self._hour == other.hour():
            if self._minute < other.minute():
                return True
            if self._minute == other.minute():
                if self._second < other.second():
                    return True
        return False
    
    '''  
    __gt__(self, other): compare against another Clock to see if current clock’s time is after
    the other clock with the same rules as eq and lt
    '''
    def __gt__(self, other):
        if not isinstance(other, Clock):
            return False
        if self._hour > other.hour():
            return True
        if self._hour == other.hour():
            if self._minute > other.minute():
                return True
            if self._minute == other.minute():
                if self._second > other.second():
                    return True
        return False