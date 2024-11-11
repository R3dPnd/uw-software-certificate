'''
<description>
    Observable class that is an abstract class.
</description>
'''
class Observable:
    '''
    <description>
        Observable class that is an abstract class.
    </description>
    <return> None </return>
    '''
    def __init__(self):
        self.observers = []
        self.__changed = False
    
    '''
    <description>
        Method to register an observer.
    </description>
    <param name=observer> Observer object. </param>
    <return> None </return>
    '''
    def register(self, observer):
        self.observers.append(observer)
    
    '''
    <description>
        Method to unregister an observer.
    </description>
    <param name=observer> Observer object. </param>
    <return> None </return>
    '''
    def unregister(self, observer):
        self.observers.remove(observer)
    
    '''
    <description>
        Method to notify all the observers.
    </description>
    <param name=message> Message to notify the observers. </param>
    <return> None </return>
    '''
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
    
    '''
    <description>
        Method to set the changed property.
    </description>
    <param name=value> Value to set the changed property. </param>
    <return> None </return>
    '''
    @property
    def changed(self):
        return self.__changed
    
    '''
    <description>
        Method to get the changed property.
    </description>
    <return> None </return>
    '''
    @changed.setter
    def set_changed(self, value):
        self.__changed = value
    
    '''
    <description>
        Method to check if the changed property is True.
    </description>
    <return> None </return>
    '''
    @changed.getter
    def has_changed(self):
        return self.__changed
    
    '''
    <description>
        Method to clear the changed property.
    </description>
    <return> None </return>
    '''
    def clear_changed(self):
        self.set_changed(False)
