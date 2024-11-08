from abc import ABC, abstractmethod

class Observer(ABC):
    '''
    <description>
        Observer class that is an abstract class.
    </description>
    <return> None </return>
    '''
    def __init__(self, observable, id):
        self.observable = observable
        self.id = id

    '''
    <description>
        Method to update the observer with the data from the observable.
    </description>
    <param name=data> Data from the observable. </param>
    <return> None </return>
    '''
    @abstractmethod
    def update(self, data):
        pass
    
    '''
    <description>
        Method to set the changed property.
    </description>
    <param name=value> Value to set the changed property. </param>
    <return> None </return>
    '''
    @abstractmethod
    def notify(self, message):
        pass

    '''
    <description>
        Method to set the changed property.
    </description>
    <param name=value> Value to set the changed property. </param>
    <return> None </return>
    '''
    def change_data(self, data):
        pass