from observer import Observer

'''
<description>
    BadGuy class that is an observer of the EyeOfSauron class.
</description>
'''
class BadGuy(Observer):
    '''
    <description> 
        BadGuy class that is an observer of the EyeOfSauron class.
    </description>
    <param name=eye> EyeOfSauron object.</param>
    <param name=name> Name of the bad guy. </param>
    <return> None </return>
    '''
    def __init__(self, eye, name):
        self.eye = eye
        self.name = name
        self.eye.register(self)
    
    '''
    <description>
        Method to remove the bad guy from the list of observers.
    </description>
    <return> None </return>
    '''
    def defeated(self):
        self.eye.unregister(self)
    
    '''
    <description>
        Method to update the bad guy with the data from the EyeOfSauron.
    </description>
    <param name=data> Data from the EyeOfSauron. </param>
    <return> None </return>
    '''
    def update(self, data):
        self.notify(data)
    
    '''
    <description>
        Method to notify the bad guy with the message from the EyeOfSauron.
    </description>
    <param name=message> Message from the EyeOfSauron. </param>
    <return> None </return>
    '''
    def notify(self, message):
        print(f"{self.name} knows about {message['Hobbits']} hobbits, {message['Elves']} elves, {message['Dwarves']} dwarves, and {message['Humans']} humans.")
        return super().notify(message)