from observable import Observable

class EyeOfSauron(Observable):
    '''
    <description> 
        EyeOfSauron class that is an observable class.
    </description>
    <return> None </return>
    '''
    def __init__(self):
        super().__init__()
        self._enemies = {
            "Hobbits": 0,
            "Elves": 0,
            "Dwarves": 0,
        }
    
    '''
    <description>
        Method to set the enemies for the EyeOfSauron.
    </description>
    <param name=hobbits> Number of hobbits. </param>
    <param name=elves> Number of elves. </param>
    <param name=dwarves> Number of dwarves. </param>
    <param name=humans> Number of humans. </param>
    <return> None </return>
    '''
    def setEnemies(self, hobbits, elves, dwarves, humans):
        self._enemies["Hobbits"] = hobbits
        self._enemies["Elves"] = elves
        self._enemies["Dwarves"] = dwarves
        self._enemies["Humans"] = humans
        self.notify(self._enemies)